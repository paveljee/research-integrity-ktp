import pandas as pd
import pyarrow.parquet as pq
import json

class AuthorMatcher:
    def __init__(self, author_details_parquet_path):
        """Load and preprocess author data."""
        # Load only required columns
        df = pq.read_table(author_details_parquet_path, 
                          columns=['authorid', 'display_name', 'display_name_alternatives', 'works_count']).to_pandas()
        
        # Parse alternatives and create searchable names
        df['alternatives'] = df['display_name_alternatives'].apply(self._parse_json)
        df['works_count'] = df['works_count'].fillna(0)
        
        # Create lookup dictionary for exact matching
        self.name_lookup = {}
        for _, row in df.iterrows():
            names = [row['display_name']] + row['alternatives']
            for name in names:
                if pd.notna(name) and name.strip():
                    name_key = name.strip().lower()
                    if name_key not in self.name_lookup:
                        self.name_lookup[name_key] = []
                    self.name_lookup[name_key].append({
                        'authorid': row['authorid'],
                        'works_count': row['works_count']
                    })
    
    def _parse_json(self, alt_str):
        """Parse JSON alternatives safely."""
        if pd.isna(alt_str) or not alt_str:
            return []
        try:
            return json.loads(alt_str) if isinstance(alt_str, str) else alt_str
        except:
            return []
    
    def get_openalex_author_id(self, first_name, last_name, top_k=1):
        """Find exact matches and return top_k by works_count."""
        if pd.isna(first_name) or pd.isna(last_name):
            return [] if top_k > 1 else None
        
        # Use only first part of first name
        first_part = str(first_name).split()[0].strip()
        last_part = str(last_name).strip()
        
        # Create search patterns
        patterns = [
            f"{first_part} {last_part}",
            f"{last_part}, {first_part}",
            f"{first_part[0]}. {last_part}" if first_part else ""
        ]
        
        # Find exact matches
        matches = []
        for pattern in patterns:
            if pattern and pattern.lower() in self.name_lookup:
                matches.extend(self.name_lookup[pattern.lower()])
        
        if not matches:
            return [] if top_k > 1 else None
        
        # Sort by works_count (descending) and take top_k
        sorted_matches = sorted(matches, key=lambda x: x['works_count'], reverse=True)
        
        if top_k == 1:
            return sorted_matches[0]['authorid']
        else:
            return [m['authorid'] for m in sorted_matches[:top_k]]

# Usage function
def match_authors(sample_df, author_details_parquet_path):
    """Match authors efficiently."""
    matcher = AuthorMatcher(author_details_parquet_path)
    
    sample_df['openalex_id'] = sample_df.apply(
        lambda row: matcher.get_openalex_author_id(row['first name'], row['last name'], top_k=1), 
        axis=1
    )
    return sample_df