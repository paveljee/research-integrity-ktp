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

## Optimized Parquet Loading Details

### Authors Parquet Loading Report (dummy_authors.parquet)
--- Timing Report for dummy_authors.parquet ---
- Strategy 'optimized_pyarrow': 0.0042 seconds (succeeded, 5 rows)
- Strategy 'batched_read': 0.0036 seconds (succeeded, 5 rows)
- Strategy 'parallel_rowgroups': 0.0042 seconds (succeeded, 5 rows)
- Strategy 'stats_filtering': 0.0029 seconds (succeeded, 5 rows)
- Strategy 'indexed_read': 0.0120 seconds (succeeded, 5 rows)
- Successfully loaded 5 records from authors parquet using optimized strategies.

### Author Details Parquet Loading Report (dummy_author_details.parquet)
--- Timing Report for dummy_author_details.parquet ---
- Strategy 'optimized_pyarrow': 0.0040 seconds (succeeded, 5 rows)
- Strategy 'batched_read': 0.0030 seconds (succeeded, 5 rows)
- Strategy 'parallel_rowgroups': 0.0033 seconds (succeeded, 5 rows)
- Strategy 'stats_filtering': 0.0029 seconds (succeeded, 5 rows)
- Strategy 'indexed_read': 0.0100 seconds (succeeded, 5 rows)
- Successfully loaded 5 records from author details parquet using optimized strategies.

- Collated DataFrame has 9 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/collated_sample_data.parquet`.

## RDF Graph Generation
- Successfully saved RDF graph to `test_run_outputs/collated_sample_data.ttl`.
- RDF Graph contains 163 triples.

### RDF Triple Statistics
- Analyzing 22 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `Some Branch of Sciences`: 9 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `Helder Pereira`: 1 occurrences
    - `Javier Enrique`: 1 occurrences
    - `Yanhong`: 1 occurrences
    - `Sodai`: 1 occurrences
    - `Andrew W.`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `Borges`: 1 occurrences
    - `Rivera Ramon`: 1 occurrences
    - `Tan`: 1 occurrences
    - `Narumi`: 1 occurrences
    - `Eckert`: 1 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `University of Coimbra`: 1 occurrences
    - `National University of Colombia`: 1 occurrences
    - `Peking University`: 1 occurrences
    - `University of Tokyo`: 1 occurrences
    - `Scripps Research`: 1 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 3
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3
  - Top 5 most frequent values:
    - `Coimbra Hospital and University Centre`: 1 occurrences
    - `Colombian Clinical Research Group`: 1 occurrences
    - `Antwerp University`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `2024-11-08 04:02:15.105592`: 1 occurrences
    - `2024-09-22 04:02:15.105592`: 1 occurrences
    - `2025-01-09 04:02:15.105592`: 1 occurrences
    - `2025-02-21 04:02:15.105592`: 1 occurrences
    - `2024-11-14 04:02:15.105592`: 1 occurrences

#### Predicate 7: `schema1:affiliation`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Institution B`: 1 occurrences
    - `Institution F`: 1 occurrences
    - `Institution A`: 1 occurrences
    - `Institution C`: 1 occurrences
    - `Institution E`: 1 occurrences

#### Predicate 8: `schema1:alternateName`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `dummy display name alternative`: 5 occurrences

#### Predicate 9: `schema1:citation`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 2753.80
  - Median: 2706.00
  - Q1 (25th percentile): 1224.00
  - Q3 (75th percentile): 4410.00

#### Predicate 10: `schema1:name`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `Helder Borges`: 1 occurrences
    - `Javier Rivera Ramon`: 1 occurrences
    - `Yanhong Tan`: 1 occurrences
    - `Sodai Narumi`: 1 occurrences
    - `Andrew Eckert`: 1 occurrences

#### Predicate 11: `schema1:url`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `ns1:works`: 1 occurrences
    - `ns2:works`: 1 occurrences
    - `ns3:works`: 1 occurrences
    - `ns4:works`: 1 occurrences
    - `ns5:works`: 1 occurrences

#### Predicate 12: `schema1:workExample`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 145.60
  - Median: 156.00
  - Q1 (25th percentile): 131.00
  - Q3 (75th percentile): 164.00

#### Predicate 13: `sciscinet:avg_c10`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 2.68
  - Median: 2.14
  - Q1 (25th percentile): 0.41
  - Q3 (75th percentile): 3.66

#### Predicate 14: `sciscinet:avg_logc10`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 4.11
  - Median: 4.23
  - Q1 (25th percentile): 4.19
  - Q3 (75th percentile): 4.34

#### Predicate 15: `sciscinet:h_index`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 28.40
  - Median: 31.00
  - Q1 (25th percentile): 11.00
  - Q3 (75th percentile): 45.00

#### Predicate 16: `sciscinet:orcid`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-3651-2728`: 1 occurrences
    - `https://orcid.org/0000-0001-5463-2017`: 1 occurrences
    - `https://orcid.org/0000-0002-5830-4601`: 1 occurrences
    - `https://orcid.org/0000-0002-9310-5510`: 1 occurrences
    - `https://orcid.org/0000-0002-4272-5375`: 1 occurrences

#### Predicate 17: `sciscinet:pgf_author`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 0.60
  - Median: 0.70
  - Q1 (25th percentile): 0.52
  - Q3 (75th percentile): 0.70

#### Predicate 18: `sciscinet:productivity`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 2.21
  - Median: 1.89
  - Q1 (25th percentile): 1.64
  - Q3 (75th percentile): 2.50

#### Predicate 19: `rdf:type`
- Total occurrences: 27
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 9 occurrences
    - `openalex:Author`: 9 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 20: `rdfs:label`
- Total occurrences: 18
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 18
  - Top 5 most frequent values:
    - `SciSciNet Author`: 1 occurrences
    - `OpenAlex Author Entity`: 1 occurrences
    - `ORCID`: 1 occurrences
    - `has OpenAlex ID`: 1 occurrences
    - `First Name from HCR`: 1 occurrences

#### Predicate 21: `owl:sameAs`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `ns6:0000-0001-3651-2728`: 1 occurrences
    - `ns6:0000-0001-5463-2017`: 1 occurrences
    - `ns6:0000-0002-5830-4601`: 1 occurrences
    - `ns6:0000-0002-9310-5510`: 1 occurrences
    - `ns6:0000-0002-4272-5375`: 1 occurrences

#### Predicate 22: `foaf:name`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Javier Enrique Rivera Ramon`: 1 occurrences
    - `Yanhong Tan`: 1 occurrences
    - `Sodai Narumi`: 1 occurrences
    - `Charicklea Meleti`: 1 occurrences
    - `Jan De Maeyer`: 1 occurrences

## Pipeline Execution Timing
- Excel Reading: 0.1951 seconds
- OpenAlex API Interaction: 4.0776 seconds
- Authors Parquet Optimized Loading: 0.0276 seconds
- Author Details Parquet Optimized Loading: 0.0238 seconds
- Data Collation: 0.0054 seconds
- Collated Parquet Saving: 0.0054 seconds
- RDF Generation and Serialization: 0.0474 seconds
- **Overall Script**: 4.4416 seconds
