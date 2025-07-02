# Test Run Report

## Input Files Statistics
- Excel File (`dummy_names.xlsx`): SHA256 = `2872ffe96eeaf308b38226184308ba6c48af034ed15a80f933979a754b9aa816`
- Authors Parquet Rows: `10`
- Authors Parquet Columns: `9`
- Authors Parquet Schema:
  - `authorid`: `string`
  - `avg_c10`: `double`
  - `avg_logc10`: `double`
  - `productivity`: `double`
  - `h_index`: `int64`
  - `display_name`: `string`
  - `inference_sources`: `list<element: string>`
  - `inference_counts`: `int64`
  - `P(gf)`: `double`
- Authors Parquet SHA256: `bda99f5f9794ed04cd98d773866759beb7c6ca0cffd5b6b7f7be23c0cb1eca4a`
- Author Details Parquet Rows: `10`
- Author Details Parquet Columns: `9`
- Author Details Parquet Schema:
  - `authorid`: `string`
  - `orcid`: `string`
  - `display_name`: `string`
  - `display_name_alternatives`: `list<element: string>`
  - `works_count`: `int64`
  - `cited_by_count`: `int64`
  - `last_known_institution`: `string`
  - `works_api_url`: `string`
  - `updated_date`: `string`
- Author Details Parquet SHA256: `1b6d3398d311db41010695457ff7c4bdac71e7721ea8e95d139121838d1b5549`

## Data Sampling and Matching
- Total names in Excel: 10
- Sampled 10 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Found 10 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 9 matching records from authors parquet.
- Successfully read 9 matching records from author details parquet.
- Collated DataFrame has 10 rows and 18 columns.
- Successfully saved collated data to `test_run_outputs/collated_sample_data.parquet`.

## RDF Graph Generation
- Successfully saved RDF graph to `test_run_outputs/collated_sample_data.ttl`.
- RDF Graph contains 183 triples.
