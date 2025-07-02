"""
This script takes a list of names from an Excel file,
finds their matching OpenAlex author IDs, and retrieves
additional information from local Parquet datasets.
"""
import pandas as pd
import pyalex
from pyalex import Authors
import os
from dotenv import load_dotenv

# Optional: Set your OpenAlex API key if you have one
# from pyalex import config
# config.email = "your_email@example.com"

def read_names_from_excel(file_path):
    """Reads names from an Excel file into a pandas DataFrame."""
    try:
        df = pd.read_excel(file_path, sheet_name=0, engine='openpyxl')
        df.columns = [col.lower() for col in df.columns]
        if 'first name' not in df.columns or 'last name' not in df.columns:
            # Still create the 'name' column for matching, but return the whole df
            df['name'] = df.get('first name', pd.Series(dtype='str')).fillna('') + ' ' + df.get('last name', pd.Series(dtype='str')).fillna('')
        elif 'name' not in df.columns: # If 'name' column is not present, but 'first name' and 'last name' are
            df['name'] = df['first name'].fillna('') + ' ' + df['last name'].fillna('')
        # If 'name' column already exists, use it as is.
        # If none of ('first name', 'last name') or 'name' exist, it will be handled by downstream checks or fail.
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return pd.DataFrame({'name': []})

def get_openalex_author_id(author_name, top_k=1):
    """
    Finds the most likely OpenAlex author ID(s) for a given name.
    Selects author(s) with the highest works_count, then highest relevance_score.
    Returns a list of the top_k matches.
    """
    try:
        authors_list = Authors().search(author_name).get()
        if not authors_list:
            return [] if top_k > 1 else None

        # Sort by works_count (descending) then by relevance_score (descending)
        sorted_authors = sorted(authors_list, key=lambda x: (x.get('works_count', 0), x.get('relevance_score', 0)), reverse=True)

        if top_k == 1:
            return sorted_authors[0]['id'] if sorted_authors else None
        else:
            return [author['id'] for author in sorted_authors[:top_k]]
    except Exception as e:
        print(f"Error querying OpenAlex for '{author_name}': {e}")
        return [] if top_k > 1 else None

def load_parquet_to_dataframe(file_path):
    """Loads a Parquet file from a local path and returns a pandas DataFrame."""
    try:
        return pd.read_parquet(file_path)
    except FileNotFoundError:
        print(f"Error: Parquet file not found at {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading Parquet file from {file_path}: {e}")
        return pd.DataFrame()

def main():
    """Main function to orchestrate the author matching process."""
    load_dotenv()
    excel_file_path = os.getenv('EXCEL_FILE_PATH', 'names.xlsx')
    authors_parquet_path = os.getenv('AUTHORS_PARQUET_PATH')
    author_details_parquet_path = os.getenv('AUTHOR_DETAILS_PARQUET_PATH')
    output_csv_file = 'matched_authors_details.csv'

    if not authors_parquet_path or not author_details_parquet_path:
        print("Error: AUTHORS_PARQUET_PATH and AUTHOR_DETAILS_PARQUET_PATH must be set in .env file.")
        return

    # 1. Read names from Excel
    names_df = read_names_from_excel(excel_file_path)
    if names_df.empty:
        print("No names to process. Exiting.")
        return

    print(f"Read {len(names_df)} names from {excel_file_path}")

    # 2. Get OpenAlex IDs (top_k=1 by default)
    names_df['openalex_id'] = names_df['name'].apply(get_openalex_author_id)
    matched_df = names_df.dropna(subset=['openalex_id']).copy()
    print(f"Found OpenAlex IDs for {len(matched_df)} names.")

    if matched_df.empty:
        print("No OpenAlex IDs found. Cannot proceed to fetch details. Exiting.")
        return

    # 3. Load local Parquet files
    print(f"Loading Parquet files: {authors_parquet_path}, {author_details_parquet_path}")
    authors_df = load_parquet_to_dataframe(authors_parquet_path)
    author_details_df = load_parquet_to_dataframe(author_details_parquet_path)

    if authors_df.empty or author_details_df.empty:
        print("One or both Parquet files failed to load or are empty. Exiting.")
        return

    print(f"Loaded authors_df ({len(authors_df)} rows) and author_details_df ({len(author_details_df)} rows).")

    # Prepare for merge by extracting short ID
    matched_df['openalex_id_short'] = matched_df['openalex_id'].apply(lambda x: x.split('/')[-1] if pd.notnull(x) else None)

    # Merge with authors data
    # Ensure correct column names based on provided schema for authors_df: ['authorid', ...]
    if 'authorid' not in authors_df.columns:
        print("Error: 'authorid' column not found in authors Parquet. Check schema.")
        return
    final_df = pd.merge(matched_df, authors_df, left_on='openalex_id_short', right_on='authorid', how='left')
    print("Merged with authors data.")

    # Merge with author_details data
    # Ensure correct column names for author_details_df: ['authorid', ...]
    if 'authorid' not in author_details_df.columns:
        print("Error: 'authorid' column not found in author_details Parquet. Check schema.")
        # If merging with authors_df failed, final_df might not have 'authorid' from it.
        # However, the check above is for author_details_df itself.
        # If authors_df merge was successful, 'authorid' (from authors_df) is the correct right_on key.
        # If 'authorid' is missing in author_details_df, we cannot merge.
        return

    # If the previous merge added an 'authorid' column (from authors_df), we use that for the next merge.
    # Otherwise, if 'openalex_id_short' is still the primary key from matched_df, use that.
    # Given the schemas, both Parquet files use 'authorid'.
    final_df = pd.merge(final_df, author_details_df, on='authorid', how='left', suffixes=('_authors', '_details'))
    print("Merged with author details data.")

    # Clean up: remove redundant openalex_id_short if authorid exists and is preferred
    if 'authorid' in final_df.columns:
        final_df.drop(columns=['openalex_id_short'], inplace=True, errors='ignore')

    print(f"Resulting DataFrame has {len(final_df)} rows before saving.")

    # 4. Save to CSV
    try:
        final_df.to_csv(output_csv_file, index=False)
        print(f"Successfully saved detailed matched author data to {output_csv_file}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

if __name__ == "__main__":
    main()
