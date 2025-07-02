# Test Run Report

## Input Files Statistics
- Excel File (`dummy_names.xlsx`): SHA256 = `3b3dbe6ec2e2f96a0f0e0dc33d10543205c760b63f86f22fbd48a9afe68722aa`
- Authors Parquet Rows: `10`
- Authors Parquet Columns: `9`
- Authors Parquet Schema:
  - `authorid`: `large_string`
  - `avg_c10`: `double`
  - `avg_logc10`: `double`
  - `productivity`: `double`
  - `h_index`: `int64`
  - `display_name`: `large_string`
  - `inference_counts`: `int64`
  - `P(gf)`: `double`
  - `inference_sources`: `int64`
- Authors Parquet SHA256: `0a77ac78c31362d72fcf13db3f3018d8a4b130a3a9791c056567d4c98cc2023f`
- Author Details Parquet Rows: `10`
- Author Details Parquet Columns: `9`
- Author Details Parquet Schema:
  - `authorid`: `string`
  - `orcid`: `string`
  - `display_name`: `string`
  - `works_count`: `int64`
  - `cited_by_count`: `int64`
  - `last_known_institution`: `string`
  - `works_api_url`: `string`
  - `updated_date`: `string`
  - `display_name_alternatives`: `string`
- Author Details Parquet SHA256: `dcff3f3a88eb0c22f40b0000d4ee4f3fe899af951c9a31eb118f31eef9a190d8`

## Data Sampling and Matching
- Total names in Excel: 10
- Sampled 10 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Found 9 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 7 matching records from authors parquet.
- Successfully read 7 matching records from author details parquet.
- Collated DataFrame has 9 rows and 18 columns.
- Successfully saved collated data to `test_run_outputs/collated_sample_data.parquet`.

## RDF Graph Generation
- Successfully saved RDF graph to `test_run_outputs/collated_sample_data.ttl`.
- RDF Graph contains 142 triples.
