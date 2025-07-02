import pandas as pd
import pyarrow.parquet as pq
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.stem import PorterStemmer
import nltk
from functools import lru_cache

# Download required NLTK data (run once)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords

class AuthorMatcher:
    def __init__(self, author_details_parquet_path):
        """Initialize with author data from parquet file."""
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.update(['jr', 'sr', 'iii', 'iv', 'van', 'de', 'la', 'von', 'del'])
        
        # Load author data efficiently
        self.author_df = self._load_author_data(author_details_parquet_path)
        
        # Preprocess all author names for efficient matching
        self._preprocess_author_data()
    
    def _load_author_data(self, parquet_path):
        """Load author data from parquet file using pyarrow."""
        # Load only required columns for efficiency
        columns = ['authorid', 'display_name', 'display_name_alternatives', 'works_count']
        df = pq.read_table(parquet_path, columns=columns).to_pandas()
        
        # Handle missing works_count
        df['works_count'] = df['works_count'].fillna(0)
        
        return df
    
    def _preprocess_text(self, text):
        """Preprocess text following OpenAlex approach."""
        if pd.isna(text) or not text:
            return ""
        
        # Normalize case and remove punctuation except hyphens
        text = re.sub(r'[^\w\s\-]', ' ', text.lower())
        
        # Split into words
        words = text.split()
        
        # Remove stop words and apply stemming
        processed_words = []
        for word in words:
            if word not in self.stop_words and len(word) > 1:
                stemmed = self.stemmer.stem(word)
                processed_words.append(stemmed)
        
        return ' '.join(processed_words)
    
    def _create_name_variants(self, first_name, last_name):
        """Create name variants similar to OpenAlex display_name_alternatives."""
        variants = []
        
        if pd.notna(first_name) and pd.notna(last_name):
            first_name = str(first_name).strip()
            last_name = str(last_name).strip()
            
            # Main combinations
            variants.extend([
                f"{first_name} {last_name}",
                f"{last_name}, {first_name}",
                f"{last_name} {first_name}"
            ])
            
            # Initial variants
            if first_name:
                variants.extend([
                    f"{first_name[0]}. {last_name}",
                    f"{first_name[0]} {last_name}",
                    f"{last_name}, {first_name[0]}."
                ])
        
        return list(set(variants))  # Remove duplicates
    
    def _preprocess_author_data(self):
        """Preprocess all author data for efficient matching."""
        # Parse display_name_alternatives JSON
        def parse_alternatives(alt_str):
            if pd.isna(alt_str) or not alt_str:
                return []
            try:
                return json.loads(alt_str) if isinstance(alt_str, str) else alt_str
            except:
                return []
        
        self.author_df['alternatives_list'] = self.author_df['display_name_alternatives'].apply(parse_alternatives)
        
        # Create combined searchable text for each author
        def create_searchable_text(row):
            texts = [row['display_name']]
            texts.extend(row['alternatives_list'])
            return ' | '.join([t for t in texts if t])
        
        self.author_df['searchable_text'] = self.author_df.apply(create_searchable_text, axis=1)
        self.author_df['processed_text'] = self.author_df['searchable_text'].apply(self._preprocess_text)
        
        # Remove empty processed texts
        self.author_df = self.author_df[self.author_df['processed_text'].str.len() > 0].copy()
    
    def _calculate_relevance_score(self, query_processed, author_processed_text, works_count):
        """Calculate relevance score combining text similarity and works count."""
        if not query_processed or not author_processed_text:
            return 0.0
        
        # TF-IDF similarity
        vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1, 2))
        try:
            tfidf_matrix = vectorizer.fit_transform([query_processed, author_processed_text])
            text_similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        except:
            text_similarity = 0.0
        
        # Exact match bonus
        exact_bonus = 1.5 if query_processed in author_processed_text else 1.0
        
        # Works count weighting (log scale to prevent domination)
        works_weight = 1 + np.log1p(works_count) * 0.1
        
        # Combined score
        relevance_score = text_similarity * exact_bonus * works_weight
        
        return relevance_score
    
    def get_openalex_author_id(self, first_name, last_name, top_k=1):
        """
        Find the most likely OpenAlex author ID(s) for given first and last name.
        Returns top_k matches sorted by relevance_score then works_count.
        """
        try:
            # Create query variants
            query_variants = self._create_name_variants(first_name, last_name)
            query_text = ' | '.join(query_variants)
            query_processed = self._preprocess_text(query_text)
            
            if not query_processed:
                return [] if top_k > 1 else None
            
            # Calculate relevance scores for all authors
            relevance_scores = []
            for idx, row in self.author_df.iterrows():
                score = self._calculate_relevance_score(
                    query_processed, 
                    row['processed_text'], 
                    row['works_count']
                )
                if score > 0:  # Only include non-zero matches
                    relevance_scores.append({
                        'authorid': row['authorid'],
                        'display_name': row['display_name'],
                        'relevance_score': score,
                        'works_count': row['works_count']
                    })
            
            if not relevance_scores:
                return [] if top_k > 1 else None
            
            # Sort by relevance_score (desc) then works_count (desc)
            sorted_matches = sorted(
                relevance_scores, 
                key=lambda x: (x['relevance_score'], x['works_count']), 
                reverse=True
            )
            
            if top_k == 1:
                return sorted_matches[0]['authorid'] if sorted_matches else None
            else:
                return [match['authorid'] for match in sorted_matches[:top_k]]
                
        except Exception as e:
            print(f"Error matching author '{first_name} {last_name}': {e}")
            return [] if top_k > 1 else None

def get_openalex_author_id(first_name, last_name, top_k=1):
    """
    Global function to match the existing interface.
    Note: This creates a new matcher instance each time, which is inefficient.
    Better to create one AuthorMatcher instance and reuse it.
    """
    # You need to set this path
    author_details_parquet_path = "path/to/your/author_details.parquet"
    matcher = AuthorMatcher(author_details_parquet_path)
    return matcher.get_openalex_author_id(first_name, last_name, top_k)

# Efficient usage example:
def match_authors_efficiently(sample_df, author_details_parquet_path):
    """
    Efficient way to match all authors at once by reusing the matcher instance.
    """
    # Create matcher once
    matcher = AuthorMatcher(author_details_parquet_path)
    
    # Apply matching
    def match_row(row):
        return matcher.get_openalex_author_id(row['first name'], row['last name'], top_k=1)
    
    sample_df['openalex_id'] = sample_df.apply(match_row, axis=1)
    return sample_df

# Usage:
# sample_df = match_authors_efficiently(sample_df, "path/to/author_details.parquet")
# 
# Or if you want to keep the existing interface:
# sample_df['openalex_id'] = sample_df.apply(lambda row: get_openalex_author_id(row['first name'], row['last name'], top_k=1), axis=1)