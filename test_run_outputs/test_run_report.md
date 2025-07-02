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
- Sample size (100) is larger than total names. Using all 10 names.
- Sampled 10 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Processed 10 names:
  - Found in local graph (API call skipped): 9
  - API calls attempted: 1
  - API calls succeeded (found OpenAlex ID): 0
  - API calls failed (no OpenAlex ID found): 1
- Found 9 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 5 matching records from authors parquet.
- Successfully read 5 matching records from author details parquet.
- Collated DataFrame has 9 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Error saving collated data to CSV: NDFrame.to_csv() got an unexpected keyword argument 'line_terminator'

## RDF Graph Generation
- Master graph currently has 163 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.
- Master RDF Graph now contains 178 triples.

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
    - `Andrew W.`: 1 occurrences
    - `Koichi`: 1 occurrences
    - `Yanhong`: 1 occurrences
    - `Charicklea`: 1 occurrences
    - `D.`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `Eckert`: 1 occurrences
    - `Naruse`: 1 occurrences
    - `Tan`: 1 occurrences
    - `Meleti`: 1 occurrences
    - `Simkovic`: 1 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `Scripps Research`: 1 occurrences
    - `Kyoto University`: 1 occurrences
    - `Peking University`: 1 occurrences
    - `Aristotle University of Thessaloniki`: 1 occurrences
    - `Comenius University`: 1 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 3
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3
  - Top 5 most frequent values:
    - `Colombian Clinical Research Group`: 1 occurrences
    - `Coimbra Hospital and University Centre`: 1 occurrences
    - `Antwerp University`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `2024-09-22 04:02:15.105592`: 1 occurrences
    - `2025-02-21 04:02:15.105592`: 1 occurrences
    - `2024-11-08 04:02:15.105592`: 1 occurrences
    - `2024-11-14 04:02:15.105592`: 1 occurrences
    - `2025-01-09 04:02:15.105592`: 1 occurrences

#### Predicate 7: `schema1:affiliation`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Institution F`: 1 occurrences
    - `Institution C`: 1 occurrences
    - `Institution B`: 1 occurrences
    - `Institution E`: 1 occurrences
    - `Institution A`: 1 occurrences

#### Predicate 8: `schema1:alternateName`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `dummy display name alternative`: 5 occurrences

#### Predicate 9: `schema1:citation`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 2753.80
  - Median: 2706.00
  - Q1 (25th percentile): 1224.00
  - Q3 (75th percentile): 4410.00

#### Predicate 10: `schema1:name`
- Total occurrences: 9
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 9
  - Top 5 most frequent values:
    - `Andrew Eckert`: 1 occurrences
    - `Koichi Naruse`: 1 occurrences
    - `Yanhong Tan`: 1 occurrences
    - `Charicklea Meleti`: 1 occurrences
    - `D. Simkovic`: 1 occurrences

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
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
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
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 28.40
  - Median: 31.00
  - Q1 (25th percentile): 11.00
  - Q3 (75th percentile): 45.00

#### Predicate 16: `sciscinet:orcid`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-5463-2017`: 1 occurrences
    - `https://orcid.org/0000-0002-9310-5510`: 1 occurrences
    - `https://orcid.org/0000-0001-3651-2728`: 1 occurrences
    - `https://orcid.org/0000-0002-4272-5375`: 1 occurrences
    - `https://orcid.org/0000-0002-5830-4601`: 1 occurrences

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
    - `Category from HCR`: 1 occurrences
    - `First Name from HCR`: 1 occurrences
    - `Last Name from HCR`: 1 occurrences
    - `Primary Affiliation from HCR`: 1 occurrences
    - `Secondary Affiliation from HCR`: 1 occurrences

#### Predicate 21: `owl:sameAs`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `ns6:0000-0001-5463-2017`: 1 occurrences
    - `ns6:0000-0002-9310-5510`: 1 occurrences
    - `ns6:0000-0001-3651-2728`: 1 occurrences
    - `ns6:0000-0002-4272-5375`: 1 occurrences
    - `ns6:0000-0002-5830-4601`: 1 occurrences

#### Predicate 22: `foaf:name`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Yanhong Tan`: 1 occurrences
    - `Charicklea Meleti`: 1 occurrences
    - `Javier Enrique Rivera Ramon`: 1 occurrences
    - `Jan De Maeyer`: 1 occurrences
    - `Sodai Narumi`: 1 occurrences

## Pipeline Execution Timing
- Excel Reading: 0.2254 seconds
- OpenAlex API Interaction and Graph Lookup: 0.8195 seconds
- Authors Parquet Reading: 0.0088 seconds
- Author Details Parquet Reading: 0.0040 seconds
- Data Collation: 0.0085 seconds
- Collated Parquet Saving: 0.0118 seconds
- Collated CSV Saving: 0.0000 seconds
- RDF Generation and Serialization: 0.0484 seconds
- **Overall Script**: 1.2238 seconds
