"""
This script takes a list of names from an Excel file,
finds their matching OpenAlex author IDs, and retrieves
additional information from local Parquet datasets.
"""
import pandas as pd
import pyalex
from pyalex import Authors
import os
import json # Added import
from dotenv import load_dotenv
from time import sleep
from loggers import get_logger

logger = get_logger(__name__)

# Optional: Set your email for OpenAlex API polite pool
pyalex.config.email = os.getenv('OPENALEX_EMAIL')

def read_names_from_excel(file_path):
    """Reads names from an Excel file into a pandas DataFrame."""
    try:
        df = pd.read_excel(file_path, sheet_name=0, engine='openpyxl')
        df.columns = [col.lower() for col in df.columns]
        if 'first name' not in df.columns or 'last name' not in df.columns:
            # Still create the 'name' column for matching, but return the whole df
            raise Exception('Expected columns were not found in the Excel file.')
        elif 'name' not in df.columns: # If 'name' column is not present, but 'first name' and 'last name' are
            first_name_series = df.get('first name', pd.Series(dtype='str')).fillna('')
            # The next line is quite important because otherwise known to return inappropriate matches from OpenAlex. Example: 'Michael A. Angelo' returns:
            # {'id': 'https://openalex.org/A5000260833', 'display_name': 'Michael A. Palladino', 'relevance_score': 5914.333, 'works_count': 303}
            # {'id': 'https://openalex.org/A5084307622', 'display_name': 'Michael A. Angelo', 'relevance_score': 5638.3184, 'works_count': 22}
            # NOT returns the actual correct author:
            # {'id': 'https://openalex.org/A5003323350', 'display_name': 'Michael Angelo', 'relevance_score': 11336.466, 'works_count': 138}
            # It MAY still be the case that for some other authors, removing the middle name can actually lead to the same thing, but saw no evidence of that yet.
            cleaned_first_name_series = first_name_series.str.split().str[0]
            last_name_series = df.get('last name', pd.Series(dtype='str')).fillna('')
            cleaned_last_name_series = last_name_series  # no cleaning ops
            df['name'] = cleaned_first_name_series + ' ' + cleaned_last_name_series
        # If 'name' column already exists, use it as is.
        # If none of ('first name', 'last name') or 'name' exist, it will be handled by downstream checks or fail.
        return df
    except FileNotFoundError:
        logger.error(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return pd.DataFrame({'name': []})

def get_openalex_author_id(author_name, all_search_results_accumulator, top_k=1):
    """
    Finds the most likely OpenAlex author ID(s) for a given name.
    Selects author(s) with the highest works_count, then highest relevance_score.
    Returns a list of the top_k matches.
    Also, it accumulates all search results into all_search_results_accumulator.
    """
    try:
        sleep(pyalex.config.retry_backoff_factor)  # Not sure pyalex does this *between* queries, so better add to be polite
        # Perform the search using pyalex
        authors_pager = Authors().search(author_name)
        raw_results = authors_pager.get() # Get all results from the pager

        # Ensure raw_results is a list, even if it's empty or contains non-dict items
        # This was the original structure expected by sorted()
        authors_list = [author for author in raw_results if isinstance(author, dict)] if raw_results else []


        if not authors_list:
            all_search_results_accumulator[author_name] = []
            return [] if top_k > 1 else None

        # Sort by relevance_score (descending) then by works_count (descending)
        sorted_authors = sorted(authors_list, key=lambda x: (x.get('relevance_score', 0), x.get('works_count', 0)), reverse=True)

        # Accumulate all sorted results for the current author name
        all_search_results_accumulator[author_name] = sorted_authors

        # For debug - original logging
        # logger.info("DEBUG: Full authors list for %s:", author_name, *([{k: a.get(k) for k in ['id', 'display_name', 'relevance_score', 'works_count']} for a in sorted_authors]), sep='\n')

        if top_k == 1:
            return sorted_authors[0]['id'] if sorted_authors else None
        else:
            return [author['id'] for author in sorted_authors[:top_k]]
    except Exception as e:
        logger.error(f"Error querying OpenAlex for '{author_name}': {e}")
        all_search_results_accumulator[author_name] = [] # Ensure key exists even on error
        return [] if top_k > 1 else None

def load_parquet_to_dataframe(file_path):
    """Loads a Parquet file from a local path and returns a pandas DataFrame."""
    try:
        return pd.read_parquet(file_path)
    except FileNotFoundError:
        logger.error(f"Error: Parquet file not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        logger.error(f"Error reading Parquet file from {file_path}: {e}")
        return pd.DataFrame()
