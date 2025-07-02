import pandas as pd
import pyarrow.parquet as pq
import os
import numpy as np
import hashlib
from dotenv import load_dotenv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD, DCTERMS, FOAF, OWL
from match_authors import read_names_from_excel, get_openalex_author_id

# Define Namespaces
SCISCINET = Namespace("http://sciscinet.org/ontology/")
OPENALEX = Namespace("https://openalex.org/")
SCHEMA = Namespace("http://schema.org/") # Using schema.org for general properties

def calculate_sha256(file_path):
    """Calculates the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def get_parquet_stats(file_path, file_name_for_report):
    """Gets basic stats from a Parquet file."""
    try:
        table = pq.read_table(file_path)
        stats = {
            f"{file_name_for_report} Rows": table.num_rows,
            f"{file_name_for_report} Columns": table.num_columns,
            f"{file_name_for_report} Schema": {name: str(table.schema.field(name).type) for name in table.schema.names},
            f"{file_name_for_report} SHA256": calculate_sha256(file_path)
        }
        return stats
    except Exception as e:
        return {
            f"{file_name_for_report} Error": str(e),
            f"{file_name_for_report} SHA256": calculate_sha256(file_path) # Still try to hash
        }

def main_test_run():
    """Main function for the test run."""
    load_dotenv()
    SEED = 42
    SAMPLE_N = 10
    OUTPUT_DIR = "test_run_outputs"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    excel_file_path = os.getenv('EXCEL_FILE_PATH')
    authors_parquet_path = os.getenv('AUTHORS_PARQUET_PATH')
    author_details_parquet_path = os.getenv('AUTHOR_DETAILS_PARQUET_PATH')

    report_content = "# Test Run Report\n\n"

    if not all([excel_file_path, authors_parquet_path, author_details_parquet_path]):
        report_content += "## Error\nMissing one or more environment variables: EXCEL_FILE_PATH, AUTHORS_PARQUET_PATH, AUTHOR_DETAILS_PARQUET_PATH.\n"
        with open(os.path.join(OUTPUT_DIR, "test_run_report.md"), "w") as f:
            f.write(report_content)
        print("Error: Missing environment variables. Check report.")
        return

    # 1. Input File Stats
    report_content += "## Input Files Statistics\n"
    excel_sha256 = calculate_sha256(excel_file_path)
    report_content += f"- Excel File (`{os.path.basename(excel_file_path)}`): SHA256 = `{excel_sha256}`\n"

    authors_stats = get_parquet_stats(authors_parquet_path, "Authors Parquet")
    for key, value in authors_stats.items():
        if isinstance(value, dict): # Schema
            report_content += f"- {key}:\n"
            for k, v in value.items():
                report_content += f"  - `{k}`: `{v}`\n"
        else:
            report_content += f"- {key}: `{value}`\n"

    author_details_stats = get_parquet_stats(author_details_parquet_path, "Author Details Parquet")
    for key, value in author_details_stats.items():
        if isinstance(value, dict): # Schema
            report_content += f"- {key}:\n"
            for k, v in value.items():
                report_content += f"  - `{k}`: `{v}`\n"
        else:
            report_content += f"- {key}: `{value}`\n"
    report_content += "\n"

    # 2. Sample from Excel
    report_content += "## Data Sampling and Matching\n"
    input_df = read_names_from_excel(excel_file_path)
    if input_df.empty or 'name' not in input_df.columns:
        report_content += "- Error: Could not read 'name' column from Excel or Excel is empty.\n"
        with open(os.path.join(OUTPUT_DIR, "test_run_report.md"), "w") as f:
            f.write(report_content)
        print("Error reading Excel. Check report.")
        return

    report_content += f"- Total names in Excel: {len(input_df)}\n"
    if len(input_df) < SAMPLE_N:
        sample_df = input_df.copy()
        report_content += f"- Sample size ({SAMPLE_N}) is larger than total names. Using all {len(input_df)} names.\n"
    else:
        sample_df = input_df.sample(n=SAMPLE_N, random_state=SEED)
    report_content += f"- Sampled {len(sample_df)} names (random_state={SEED}).\n"

    # 3. Find OpenAlex IDs (top_k=1)
    report_content += "- Finding OpenAlex IDs (top_k=1, highest relevance only).\n"
    sample_df['openalex_id'] = sample_df['name'].apply(lambda name: get_openalex_author_id(name, top_k=1))

    matched_sample_df = sample_df.dropna(subset=['openalex_id']).copy()
    matched_ids = [oid.split('/')[-1] for oid in matched_sample_df['openalex_id'].tolist() if oid]
    report_content += f"- Found {len(matched_ids)} unique OpenAlex IDs for the sample.\n"

    if not matched_ids:
        report_content += "- No OpenAlex IDs found for the sample. Cannot proceed.\n"
        with open(os.path.join(OUTPUT_DIR, "test_run_report.md"), "w") as f:
            f.write(report_content)
        print("No OpenAlex IDs matched for the sample. Check report.")
        return

    # 4. Load data from Parquets for matched IDs
    report_content += "- Loading data from Parquet files for matched OpenAlex IDs.\n"

    # Authors Parquet schema: ['authorid', 'avg_c10', 'avg_logc10', 'productivity', 'h_index', 'display_name', 'inference_sources', 'inference_counts', 'P(gf)']
    authors_cols_to_load = ['authorid', 'avg_c10', 'avg_logc10', 'productivity', 'h_index', 'display_name', 'inference_sources', 'inference_counts', 'P(gf)']
    # Author Details Parquet schema: ['authorid', 'orcid', 'display_name', 'display_name_alternatives', 'works_count', 'cited_by_count', 'last_known_institution', 'works_api_url', 'updated_date']
    author_details_cols_to_load = ['authorid', 'orcid', 'display_name_alternatives', 'works_count', 'cited_by_count', 'last_known_institution', 'works_api_url', 'updated_date']
    # Note: 'display_name' is in both, will be suffixed by merge. We'll keep author_details one if different.

    try:
        authors_table = pq.read_table(authors_parquet_path, columns=authors_cols_to_load, filters=[('authorid', 'in', matched_ids)])
        authors_data_df = authors_table.to_pandas()
        report_content += f"- Successfully read {len(authors_data_df)} matching records from authors parquet.\n"
    except Exception as e:
        report_content += f"- Error reading authors Parquet: {e}\n"
        authors_data_df = pd.DataFrame()

    try:
        author_details_table = pq.read_table(author_details_parquet_path, columns=author_details_cols_to_load, filters=[('authorid', 'in', matched_ids)])
        author_details_data_df = author_details_table.to_pandas()
        report_content += f"- Successfully read {len(author_details_data_df)} matching records from author details parquet.\n"
    except Exception as e:
        report_content += f"- Error reading author details Parquet: {e}\n"
        author_details_data_df = pd.DataFrame()

    # 5. Collate information
    # Start with the successfully matched OpenAlex IDs and their original names
    collated_df = matched_sample_df[['name', 'openalex_id']].copy()
    collated_df['authorid'] = collated_df['openalex_id'].apply(lambda x: x.split('/')[-1])

    if not authors_data_df.empty:
        collated_df = pd.merge(collated_df, authors_data_df, on='authorid', how='left')
    if not author_details_data_df.empty:
        # Use suffixes to distinguish display_name if it exists in both and handle potential conflicts
        collated_df = pd.merge(collated_df, author_details_data_df, on='authorid', how='left', suffixes=('_author_stats', '_author_details'))
        # Example of handling display_name: prefer details if available
        if 'display_name_author_details' in collated_df.columns and 'display_name_author_stats' in collated_df.columns:
            collated_df['display_name'] = collated_df['display_name_author_details'].fillna(collated_df['display_name_author_stats'])
            collated_df.drop(columns=['display_name_author_details', 'display_name_author_stats'], inplace=True)
        elif 'display_name_author_details' in collated_df.columns: # if only details has it after merge
             collated_df.rename(columns={'display_name_author_details': 'display_name'}, inplace=True)
        elif 'display_name_author_stats' in collated_df.columns: # if only stats has it
             collated_df.rename(columns={'display_name_author_stats': 'display_name'}, inplace=True)


    report_content += f"- Collated DataFrame has {len(collated_df)} rows and {len(collated_df.columns)} columns.\n"

    # 6. Save collated DataFrame to Parquet
    collated_parquet_path = os.path.join(OUTPUT_DIR, "collated_sample_data.parquet")
    try:
        collated_df.to_parquet(collated_parquet_path, index=False)
        report_content += f"- Successfully saved collated data to `{collated_parquet_path}`.\n"
    except Exception as e:
        report_content += f"- Error saving collated data to Parquet: {e}\n"


    # 7. Save to RDF Turtle
    report_content += "\n## RDF Graph Generation\n"
    g = Graph()
    g.bind("sciscinet", SCISCINET)
    g.bind("openalex", OPENALEX)
    g.bind("schema", SCHEMA)
    g.bind("dcterms", DCTERMS)
    g.bind("foaf", FOAF)
    g.bind("owl", OWL)

    # Basic ontology statements (very minimal)
    g.add((SCISCINET.Author, RDF.type, OWL.Class))
    g.add((SCISCINET.Author, RDFS.label, Literal("SciSciNet Author")))
    g.add((OPENALEX.Author, RDF.type, OWL.Class))
    g.add((OPENALEX.Author, RDFS.label, Literal("OpenAlex Author Entity")))
    g.add((SCISCINET.orcid, RDF.type, OWL.DatatypeProperty)) # Corrected from ObjectProperty
    g.add((SCISCINET.orcid, RDFS.label, Literal("ORCID")))
    g.add((SCISCINET.hasOpenAlexID, RDF.type, OWL.ObjectProperty))
    g.add((SCISCINET.hasOpenAlexID, RDFS.label, Literal("has OpenAlex ID")))


    for _, row in collated_df.iterrows():
        if pd.isna(row.get('openalex_id')):
            continue

        author_uri_str = row['openalex_id']
        # Ensure author_uri is a valid URI. OpenAlex IDs are already URLs.
        author_uri = URIRef(author_uri_str)

        g.add((author_uri, RDF.type, OPENALEX.Author)) # Primary type from OpenAlex
        g.add((author_uri, RDF.type, SCISCINET.Author)) # Also a SciSciNet author concept

        # Original input name
        if pd.notna(row.get('name')):
            g.add((author_uri, SCHEMA.name, Literal(row['name']))) # Original name from input
            g.add((author_uri, RDFS.label, Literal(f"Author: {row['name']} ({row['authorid']})")))


        # From authors parquet (sciscinet specific stats)
        # Use 'display_name' that was resolved from merge conflicts
        if pd.notna(row.get('display_name')):
            g.add((author_uri, FOAF.name, Literal(row['display_name']))) # Official/display name
        if pd.notna(row.get('avg_c10')):
            g.add((author_uri, SCISCINET.avg_c10, Literal(row['avg_c10'], datatype=XSD.float)))
        if pd.notna(row.get('avg_logc10')):
            g.add((author_uri, SCISCINET.avg_logc10, Literal(row['avg_logc10'], datatype=XSD.float)))
        if pd.notna(row.get('productivity')):
            g.add((author_uri, SCISCINET.productivity, Literal(row['productivity'], datatype=XSD.float)))
        if pd.notna(row.get('h_index')):
            g.add((author_uri, SCISCINET.h_index, Literal(row['h_index'], datatype=XSD.integer)))
        if pd.notna(row.get('P(gf)')):
            g.add((author_uri, SCISCINET.pgf_author, Literal(row['P(gf)'], datatype=XSD.float))) # P(gf) for author

        # From author_details parquet
        if pd.notna(row.get('orcid')):
            # ORCID is an identifier, not necessarily an object to link to unless we have ORCID entities
            g.add((author_uri, SCISCINET.orcid, Literal(row['orcid'])))
            g.add((author_uri, OWL.sameAs, URIRef(row['orcid']))) # Link to ORCID URI

        alternatives_data = row.get('display_name_alternatives')
        items_to_process = []

        if alternatives_data is None:
            pass # items_to_process remains empty
        elif isinstance(alternatives_data, np.ndarray):
            # Filter out NaN/None/empty strings from the numpy array
            items_to_process = [str(item).strip() for item in alternatives_data if pd.notna(item) and str(item).strip() and str(item).strip().lower() not in ['none', 'nan']]
        elif isinstance(alternatives_data, list):
            # Filter out NaN/None/empty strings from the list
            items_to_process = [str(item).strip() for item in alternatives_data if pd.notna(item) and str(item).strip() and str(item).strip().lower() not in ['none', 'nan']]
        elif pd.notna(alternatives_data): # Scalar case
            alt_str = str(alternatives_data).strip()
            if alt_str and alt_str.lower() not in ['none', 'nan']:
                items_to_process = [alt_str]
        # If alternatives_data is a scalar NaN, items_to_process remains empty

        for alt_name_str in items_to_process:
            # All items in items_to_process are now guaranteed to be valid, non-empty strings
            g.add((author_uri, SCHEMA.alternateName, Literal(alt_name_str)))

        if pd.notna(row.get('works_count')):
            g.add((author_uri, SCHEMA.workExample, Literal(row['works_count'], datatype=XSD.integer))) # Using workExample as a proxy for works_count
        if pd.notna(row.get('cited_by_count')):
            g.add((author_uri, SCHEMA.citation, Literal(row['cited_by_count'], datatype=XSD.integer))) # Using citation as proxy

        if pd.notna(row.get('last_known_institution')) and row.get('last_known_institution'):
            # Potentially create institution entities later
            g.add((author_uri, SCHEMA.affiliation, Literal(str(row['last_known_institution'])))) # Simplified

        if pd.notna(row.get('works_api_url')):
            g.add((author_uri, SCHEMA.url, URIRef(row['works_api_url']))) # URL to their works list
        if pd.notna(row.get('updated_date')):
            try:
                g.add((author_uri, DCTERMS.modified, Literal(pd.to_datetime(row['updated_date']).isoformat(), datatype=XSD.dateTime)))
            except: # Handle if date is not parsable
                g.add((author_uri, DCTERMS.modified, Literal(str(row['updated_date']))))


    rdf_file_path = os.path.join(OUTPUT_DIR, "collated_sample_data.ttl")
    try:
        g.serialize(destination=rdf_file_path, format="turtle")
        report_content += f"- Successfully saved RDF graph to `{rdf_file_path}`.\n"
        report_content += f"- RDF Graph contains {len(g)} triples.\n"
    except Exception as e:
        report_content += f"- Error saving RDF graph: {e}\n"

    # 8. Save Markdown Report
    report_path = os.path.join(OUTPUT_DIR, "test_run_report.md")
    with open(report_path, "w") as f:
        f.write(report_content)
    print(f"Test run complete. Report saved to {report_path}")

if __name__ == "__main__":
    main_test_run()
