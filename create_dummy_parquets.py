import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import numpy as np

# Ensure dummy_data directory exists
os.makedirs("dummy_data", exist_ok=True)

# Dummy Authors Parquet
authors_data = {
    'authorid': ['A5003323350', 'A5023880075', 'A5023390738', 'A5045787356', 'A5000000000'],
    'avg_c10': [1.0, 2.0, 3.0, 4.0, 5.0],
    'avg_logc10': [0.1, 0.2, 0.3, 0.4, 0.5],
    'productivity': [10.0, 20.0, 15.0, 25.0, 30.0],
    'h_index': [5, 10, 8, 12, 15],
    'display_name': ['Michael Angelo', 'Leonardo Vinci', 'Raphael Sanzio', 'Donato Bramante', 'Marie Curie'],
    'inference_sources': [['src1'], ['src2'], ['src1', 'src3'], ['src4'], ['src5']], # List type
    'inference_counts': [[10], [5], [8, 2], [1], [7]], # List type
    'P(gf)': [0.9, 0.8, 0.85, 0.7, 0.95]
}
authors_df = pd.DataFrame(authors_data)
# Convert list columns to pyarrow list arrays for correct Parquet writing
# For PyArrow, when converting from pandas, it's often better to let from_pandas handle list types directly,
# or construct ListArray explicitly if needed.
# authors_df['inference_sources'] = authors_df['inference_sources'].apply(lambda x: pa.array(x, type=pa.string())) # This was problematic
# authors_df['inference_counts'] = authors_df['inference_counts'].apply(lambda x: pa.array(x, type=pa.int64())) # This was problematic

# Option 1: Let from_pandas infer (should work for lists of scalars)
# Option 2: Explicitly create ListArrays (more robust for complex list structures)
schema_authors = pa.schema([
    ('authorid', pa.string()),
    ('avg_c10', pa.float64()),
    ('avg_logc10', pa.float64()),
    ('productivity', pa.float64()),
    ('h_index', pa.int64()),
    ('display_name', pa.string()),
    ('inference_sources', pa.list_(pa.string())),
    ('inference_counts', pa.list_(pa.int64())),
    ('P(gf)', pa.float64())
])
authors_table = pa.Table.from_pandas(authors_df, schema=schema_authors, preserve_index=False)
pq.write_table(authors_table, 'dummy_data/dummy_authors.parquet')
print("Created dummy_data/dummy_authors.parquet")

# Dummy Author Details Parquet
author_details_data = {
    'authorid': ['A5003323350', 'A5023880075', 'A5023390738', 'A5045787356', 'A5000000000'],
    'orcid': ['https://orcid.org/0000-0001-2345-6789', 'https://orcid.org/0000-0002-3456-7890', 'https://orcid.org/0000-0003-4567-8901', 'https://orcid.org/0000-0004-5678-9012', 'https://orcid.org/0000-0005-6789-0123'],
    'display_name_alternatives': [['Michelangelo Buonarroti'], ['Leonardo da Vinci'], ['Raffaello'], ['Bramante'], ['Maria Skłodowska-Curie', 'Madame Curie']], # List type
    'works_count': [138, 100, 200, 50, 300],
    'cited_by_count': [1000, 2000, 1500, 500, 5000],
    'last_known_institution': ['Florence Academy', 'Amboise Royal Court', 'Roman School', 'St. Peter Basilica', 'Sorbonne'],
    'works_api_url': ['url1', 'url2', 'url3', 'url4', 'url5'],
    'updated_date': [pd.Timestamp('2023-01-01'), pd.Timestamp('2023-01-02'), pd.Timestamp('2023-01-03'), pd.Timestamp('2023-01-04'), pd.Timestamp('2023-01-05')]
}
author_details_df = pd.DataFrame(author_details_data)
# Convert list column to pyarrow list array
# author_details_df['display_name_alternatives'] = author_details_df['display_name_alternatives'].apply(lambda x: pa.array(x, type=pa.string())) # Problematic

schema_author_details = pa.schema([
    ('authorid', pa.string()),
    ('orcid', pa.string()),
    ('display_name_alternatives', pa.list_(pa.string())),
    ('works_count', pa.int64()),
    ('cited_by_count', pa.int64()),
    ('last_known_institution', pa.string()),
    ('works_api_url', pa.string()),
    ('updated_date', pa.timestamp('ns'))
])
author_details_table = pa.Table.from_pandas(author_details_df, schema=schema_author_details, preserve_index=False)
pq.write_table(author_details_table, 'dummy_data/dummy_author_details.parquet')
print("Created dummy_data/dummy_author_details.parquet")

# Dummy Excel file (dummy_names.xlsx)
# The script read_names_from_excel expects 'first name' and 'last name'
# or a 'name' column. It will create 'name' if 'first name' and 'last name' exist.
excel_data = {
    'first name': ['Michael', 'Leonardo', 'Raphael', 'Donato', 'Marie', 'Unknown'],
    'last name': ['Angelo', 'Vinci', 'Sanzio', 'Bramante', 'Curie', 'Author'],
    'category': ['Art', 'Science', 'Art', 'Architecture', 'Science', 'Misc'],
    'primary affiliation': ['Vatican', 'Milan', 'Florence', 'Milan', 'Paris Sorbonne', 'Nowhere'],
    'secondary affiliation': ['Florence', 'Amboise', 'Rome', 'Rome', 'Warsaw', '']
}
excel_df = pd.DataFrame(excel_data)
excel_df.to_excel('dummy_data/dummy_names.xlsx', index=False, engine='openpyxl')
print("Created dummy_data/dummy_names.xlsx")
