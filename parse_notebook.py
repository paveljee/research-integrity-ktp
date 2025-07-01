import json
import pandas as pd
import re

def extract_names_from_notebook_json(notebook_content_str):
    """
    Parses a Jupyter notebook JSON string to extract author names.
    It looks for names in specific structures identified in the example notebook:
    1. A multiline string variable `csv_data` in a code cell.
    2. A markdown section listing "clearest duplicates".
    """
    names = []
    try:
        notebook_json = json.loads(notebook_content_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding notebook JSON: {e}")
        return []

    for cell in notebook_json.get('cells', []):
        cell_type = cell.get('cell_type')
        source_lines = cell.get('source', [])
        source_str = "".join(source_lines)

        if cell_type == 'code':
            # Look for the csv_data variable
            if 'csv_data = """' in source_str:
                try:
                    csv_content_match = re.search(r'csv_data = """(.*?)"""', source_str, re.DOTALL)
                    if csv_content_match:
                        csv_content = csv_content_match.group(1).strip()
                        # Use pandas to read this in-memory CSV string
                        from io import StringIO
                        temp_df = pd.read_csv(StringIO(csv_content))
                        if 'First Name' in temp_df.columns and 'Last Name' in temp_df.columns:
                            for _, row in temp_df.iterrows():
                                first_name = str(row['First Name']).strip()
                                last_name = str(row['Last Name']).strip()
                                if first_name and last_name and first_name != 'nan' and last_name != 'nan':
                                    names.append(f"{first_name} {last_name}")
                except Exception as e:
                    print(f"Error parsing csv_data from code cell: {e}")

        elif cell_type == 'markdown':
            # Look for the "clearest duplicates" section
            if "### Most Probable Duplicates:" in source_str or "### Clearest Duplicates" in source_str.title(): # Making it more robust
                # Regex to find lines like "- **Author Name** (Affiliation)" or "- **Author Name**"
                # This regex captures names that are bolded and at the start of a list item.
                # It tries to capture up to the first parenthesis, comma, or end of line if no affiliation detail.
                # Example: "- **Bin Liu**, City..." or "- **Chris Sander** (Harvard..."
                # It can be tricky if names themselves contain parentheses or commas not related to affiliation.

                # Simpler approach for the specific format: "- **Name**," or "- **Name** ("
                # Pattern: "- **(Anything not a `*` or `(`)**"
                # Then clean up trailing commas or spaces.

                # Let's try to find lines starting with "- **" and extract the name part
                # This will be a bit heuristic.
                for line in source_lines:
                    line = line.strip()
                    if line.startswith("- **"): # Names like "- **Chris Sander** (Harvard..."
                        match = re.search(r'- \*\*(.*?)\*\*', line)
                        if match:
                            name_part = match.group(1)
                            # Remove trailing details like affiliation starting with ( or ,
                            name_part = re.split(r'\(|,', name_part)[0].strip()
                            if name_part and len(name_part.split()) >= 2: # Basic check for a full name
                                names.append(name_part)
                    elif re.match(r'\d+\\?\.\s*\*\*(.*?)\*\*', line): # Names like "1. **Bin Liu**"
                        match = re.search(r'\d+\\?\.\s*\*\*(.*?)\*\*', line)
                        if match:
                            name_part = match.group(1)
                            name_part = re.split(r'\(|,', name_part)[0].strip()
                            if name_part and len(name_part.split()) >= 2:
                                names.append(name_part)


    # Deduplicate
    return sorted(list(set(name for name in names if name)))

if __name__ == '__main__':
    # This part is for testing the parser script itself.
    # In the main workflow, match_authors.py will call the function.
    gist_url = "https://gist.github.com/pvzhelnov/aa2a93ff3d3128622dcf352b45ff9faf/raw/d76988a3a5e323a8342125689895544cec6962ac/extract_clarivate_hcr_2025-06-08.ipynb"

    try:
        import requests
        response = requests.get(gist_url)
        response.raise_for_status()
        notebook_content = response.text
    except Exception as e:
        print(f"Error fetching notebook content for testing parser: {e}")
        notebook_content = ""

    if notebook_content:
        extracted_names = extract_names_from_notebook_json(notebook_content)
        print(f"Extracted {len(extracted_names)} unique names:")
        for name in extracted_names:
            print(name)

        # Create a DataFrame and save to Excel
        if extracted_names:
            df = pd.DataFrame({'name': extracted_names})
            try:
                # Requires openpyxl
                df.to_excel("clarivate_extracted_names.xlsx", index=False, engine='openpyxl')
                print("\nSuccessfully saved extracted names to clarivate_extracted_names.xlsx")
            except Exception as e:
                print(f"\nError saving to Excel: {e}. Make sure 'openpyxl' is installed.")
        else:
            print("\nNo names extracted to save.")
    else:
        print("No notebook content to parse.")
