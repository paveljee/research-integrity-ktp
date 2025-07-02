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
- Collated DataFrame has 9 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/collated_sample_data.parquet`.

## RDF Graph Generation
- Successfully saved RDF graph to `test_run_outputs/collated_sample_data.ttl`.
- RDF Graph contains 142 triples.

### RDF Triple Statistics
- Analyzing 17 unique predicates:

#### Predicate 1: `dcterms:modified`
- Total occurrences: 7
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 7
  - Top 5 most frequent values:
    - `2024-12-13 04:02:15.105592`: 1 occurrences
    - `2024-11-08 04:02:15.105592`: 1 occurrences
    - `2024-09-22 04:02:15.105592`: 1 occurrences
    - `2025-01-09 04:02:15.105592`: 1 occurrences
    - `2024-08-30 04:02:15.105592`: 1 occurrences

#### Predicate 2: `schema1:affiliation`
- Total occurrences: 7
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 7
  - Top 5 most frequent values:
    - `Institution I`: 1 occurrences
    - `Institution B`: 1 occurrences
    - `Institution F`: 1 occurrences
    - `Institution A`: 1 occurrences
    - `Institution H`: 1 occurrences

#### Predicate 3: `schema1:alternateName`
- Total occurrences: 7
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `dummy display name alternative`: 7 occurrences

#### Predicate 4: `schema1:citation`
- Total occurrences: 7
- **Numeric Values Statistics:**
  - Count: 7
  - Mean: 3151.86
  - Median: 3892.00
  - Q1 (25th percentile): 1965.00
  - Q3 (75th percentile): 4406.00

#### Predicate 5: `schema1:name`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `Helder Pereira Borges`: 1 occurrences
    - `Javier Enrique Rivera Ramon`: 1 occurrences
    - `Yanhong Tan`: 1 occurrences
    - `Sodai Narumi`: 1 occurrences
    - `Andrew W. Eckert`: 1 occurrences

#### Predicate 6: `schema1:url`
- Total occurrences: 7
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 7
  - Top 5 most frequent values:
    - `ns1:works`: 1 occurrences
    - `ns2:works`: 1 occurrences
    - `ns3:works`: 1 occurrences
    - `ns4:works`: 1 occurrences
    - `ns5:works`: 1 occurrences

#### Predicate 7: `schema1:workExample`
- Total occurrences: 7
- **Numeric Values Statistics:**
  - Count: 7
  - Mean: 120.86
  - Median: 131.00
  - Q1 (25th percentile): 84.00
  - Q3 (75th percentile): 160.00

#### Predicate 8: `sciscinet:avg_c10`
- Total occurrences: 7
- **Numeric Values Statistics:**
  - Count: 7
  - Mean: 4.74
  - Median: 3.66
  - Q1 (25th percentile): 1.28
  - Q3 (75th percentile): 8.30

#### Predicate 9: `sciscinet:avg_logc10`
- Total occurrences: 7
- **Numeric Values Statistics:**
  - Count: 7
  - Mean: 3.98
  - Median: 4.23
  - Q1 (25th percentile): 3.70
  - Q3 (75th percentile): 4.42

#### Predicate 10: `sciscinet:h_index`
- Total occurrences: 7
- **Numeric Values Statistics:**
  - Count: 7
  - Mean: 26.43
  - Median: 31.00
  - Q1 (25th percentile): 8.50
  - Q3 (75th percentile): 41.50

#### Predicate 11: `sciscinet:orcid`
- Total occurrences: 7
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 7
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-5077-9714`: 1 occurrences
    - `https://orcid.org/0000-0001-3651-2728`: 1 occurrences
    - `https://orcid.org/0000-0001-5463-2017`: 1 occurrences
    - `https://orcid.org/0000-0002-5830-4601`: 1 occurrences
    - `https://orcid.org/0000-0002-8821-9904`: 1 occurrences

#### Predicate 12: `sciscinet:pgf_author`
- Total occurrences: 7
- **Numeric Values Statistics:**
  - Count: 7
  - Mean: 0.60
  - Median: 0.70
  - Q1 (25th percentile): 0.42
  - Q3 (75th percentile): 0.74

#### Predicate 13: `sciscinet:productivity`
- Total occurrences: 7
- **Numeric Values Statistics:**
  - Count: 7
  - Mean: 2.72
  - Median: 2.50
  - Q1 (25th percentile): 1.77
  - Q3 (75th percentile): 3.64

#### Predicate 14: `rdf:type`
- Total occurrences: 22
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 9 occurrences
    - `openalex:Author`: 9 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences
    - `owl:DatatypeProperty`: 1 occurrences

#### Predicate 15: `rdfs:label`
- Total occurrences: 13
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 13
  - Top 5 most frequent values:
    - `SciSciNet Author`: 1 occurrences
    - `OpenAlex Author Entity`: 1 occurrences
    - `ORCID`: 1 occurrences
    - `has OpenAlex ID`: 1 occurrences
    - `Author: Helder Pereira Borges (A5027521767)`: 1 occurrences

#### Predicate 16: `owl:sameAs`
- Total occurrences: 7
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 7
  - Top 5 most frequent values:
    - `ns8:0000-0001-5077-9714`: 1 occurrences
    - `ns8:0000-0001-3651-2728`: 1 occurrences
    - `ns8:0000-0001-5463-2017`: 1 occurrences
    - `ns8:0000-0002-5830-4601`: 1 occurrences
    - `ns8:0000-0002-8821-9904`: 1 occurrences

#### Predicate 17: `foaf:name`
- Total occurrences: 7
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 7
  - Top 5 most frequent values:
    - `Hélder Pereira Borges`: 1 occurrences
    - `Javier Enrique Rivera Ramon`: 1 occurrences
    - `Yanhong Tan`: 1 occurrences
    - `Sodai Narumi`: 1 occurrences
    - `Andrew W. Eckert`: 1 occurrences

## Pipeline Execution Timing
- Excel Reading: 0.1990 seconds
- OpenAlex API Interaction: 2.4521 seconds
- Authors Parquet Reading: 0.0040 seconds
- Author Details Parquet Reading: 0.0035 seconds
- Data Collation: 0.0057 seconds
- Collated Parquet Saving: 0.0060 seconds
- RDF Generation and Serialization: 0.0453 seconds
- **Overall Script**: 2.7677 seconds
