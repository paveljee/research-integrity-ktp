"""
This script takes a list of names from an Excel file,
finds their matching OpenAlex author IDs, and retrieves
additional information from HuggingFace Parquet datasets.
"""
import pandas as pd
import pyalex
from pyalex import Authors
import requests
import io

# Optional: Set your OpenAlex API key if you have one
# from pyalex import config
# config.email = "your_email@example.com"

def read_names_from_excel(file_path):
    """Reads names from an Excel file into a pandas DataFrame."""
    try:
        # Read only the first sheet by default, specify engine for xlsx
        df = pd.read_excel(file_path, sheet_name=0, engine='openpyxl')
        # Convert all column names to lowercase for consistency
        df.columns = [col.lower() for col in df.columns]
        if 'name' not in df.columns:
            # If 'name' is not present, try to find a likely candidate or raise error
            # For simplicity, we'll stick to requiring 'name' for now.
            raise ValueError("Excel file must contain a 'name' column (case-insensitive).")
        return df[['name']]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame({'name': []})
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return pd.DataFrame({'name': []})

def get_openalex_author_id(author_name):
    """
    Finds the most likely OpenAlex author ID for a given name.
    Selects the author with the highest works_count.
    If works_count is the same, selects the one with the highest relevance_score.
    """
    try:
        # Using .search() and then .get() to retrieve all results
        # .search(author_name) performs a keyword search
        # .get() retrieves all results from the pager
        authors_list = Authors().search(author_name).get()

        if not authors_list:
            return None

        # Sort by works_count (descending) then by relevance_score (descending)
        # Ensure 'works_count' and 'relevance_score' exist, default to 0 if not
        # The number of results can be large, so we might want to limit how many we sort
        # For now, assume the list isn't excessively large or pyalex handles it efficiently.
        best_match = sorted(authors_list, key=lambda x: (x.get('works_count', 0), x.get('relevance_score', 0)), reverse=True)[0]
        return best_match['id']
    except Exception as e:
        print(f"Error querying OpenAlex for '{author_name}': {e}")
        return None

def download_parquet_to_dataframe(url):
    """Downloads a Parquet file from a URL and returns a pandas DataFrame."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return pd.read_parquet(io.BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        print(f"Error downloading Parquet file from {url}: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading Parquet file from {url}: {e}")
        return pd.DataFrame()

def main():
    """Main function to orchestrate the author matching process."""
    excel_file = 'names.xlsx' # Reverted to default
    output_csv_file = 'matched_authors_details.csv' # Reverted to default

    # 1. Read names from Excel
    names_df = read_names_from_excel(excel_file)
    if names_df.empty:
        print("No names to process. Exiting.")
        return

    print(f"Read {len(names_df)} names from {excel_file}")

    # 2. Get OpenAlex IDs
    names_df['openalex_id'] = names_df['name'].apply(get_openalex_author_id)
    # Explicitly create a copy to avoid SettingWithCopyWarning later
    matched_df = names_df.dropna(subset=['openalex_id']).copy()
    print(f"Found OpenAlex IDs for {len(matched_df)} names.")

    if matched_df.empty:
        print("No OpenAlex IDs found. Cannot proceed to fetch details. Exiting.")
        return

    # 3. Download HuggingFace datasets
    # It's good practice to let users know about potentially large downloads.
    print("Attempting to download Parquet files from HuggingFace. This may take some time...")
    authors_hf_url = "https://huggingface.co/datasets/Northwestern-CSSI/sciscinet-v2/resolve/main/data/authors-00000-of-00001.parquet?download=true"
    author_details_hf_url = "https://huggingface.co/datasets/Northwestern-CSSI/sciscinet-v2/resolve/main/data/author_details-00000-of-00001.parquet?download=true"

    authors_hf_df = download_parquet_to_dataframe(authors_hf_url)
    author_details_hf_df = download_parquet_to_dataframe(author_details_hf_url)

    matched_df['openalex_id_short'] = matched_df['openalex_id'].apply(lambda x: x.split('/')[-1] if pd.notnull(x) else None)
    final_df = matched_df.copy() # Start with OpenAlex data

    if not authors_hf_df.empty:
        print(f"Successfully downloaded authors_hf_df ({len(authors_hf_df)} rows).")
        if 'id' in authors_hf_df.columns:
            final_df = pd.merge(final_df, authors_hf_df, left_on='openalex_id_short', right_on='id', how='left')
            print("Merged with authors_hf_df.")

            # Try to merge with author_details_hf_df if authors_hf_df was successful and details are available
            if not author_details_hf_df.empty:
                print(f"Successfully downloaded author_details_hf_df ({len(author_details_hf_df)} rows).")
                if 'author_id' in author_details_hf_df.columns and 'id' in final_df.columns: # 'id' is now from authors_hf_df
                    final_df = pd.merge(final_df, author_details_hf_df, left_on='id', right_on='author_id', how='left', suffixes=('_author', '_details'))
                    print("Merged with author_details_hf_df.")
                    # Clean up potentially duplicated 'id' column from the merge if it's named 'id_author'
                    if 'id_author' in final_df.columns and 'openalex_id_short' in final_df.columns:
                         # Check if 'id' (original from authors_hf) and 'id_author' (from merge suffix) are the same before dropping
                        if 'id' in final_df.columns and final_df['id'].equals(final_df['id_author']):
                            final_df = final_df.drop(columns=['id_author'])
                        elif 'id_details' in final_df.columns : # if suffix was _details for the id column from author_details
                            pass # keep both if they are different, or decide on specific logic

                elif 'author_id' not in author_details_hf_df.columns:
                    print("Warning: 'author_id' column not found in author_details_hf_df. Skipping merge with author_details_hf_df.")
                elif 'id' not in final_df.columns: # Should not happen if previous merge was successful
                    print("Warning: 'id' column (from authors_hf_df) not found for merging with author_details_hf_df. Skipping.")
            elif author_details_hf_df.empty:
                print("Warning: author_details_hf_df is empty or failed to download. Skipping merge with it.")
        else:
            print("Warning: 'id' column not found in authors_hf_df. Skipping merge with HuggingFace data.")
    else:
        print("Warning: authors_hf_df is empty or failed to download. Skipping all HuggingFace data merging.")
        print("Proceeding with OpenAlex data only.")

    print(f"Resulting DataFrame has {len(final_df)} rows before saving.")

    # 5. Save to CSV
    try:
        final_df.to_csv(output_csv_file, index=False)
        print(f"Successfully saved detailed matched author data to {output_csv_file}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

if __name__ == "__main__":
    main()
