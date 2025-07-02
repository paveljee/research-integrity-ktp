# Test Run Report

## Input Files Statistics
- Excel File (`2024_HCR.xlsx`): SHA256 = `dabf094643254a8c6de84f08f6d6774388e1b9d2f090935a85084bdde44ec294`
- Authors Parquet Rows: `100418971`
- Authors Parquet Columns: `9`
- Authors Parquet Schema:
  - `authorid`: `large_string`
  - `avg_c10`: `double`
  - `avg_logc10`: `double`
  - `productivity`: `uint32`
  - `h_index`: `uint32`
  - `display_name`: `large_string`
  - `inference_sources`: `int64`
  - `inference_counts`: `int64`
  - `P(gf)`: `double`
- Authors Parquet SHA256: `17669bf36ddfe2c6fcebd759bdbc292269d3651292792babe0211a6161ae492e`
- Author Details Parquet Rows: `100418971`
- Author Details Parquet Columns: `9`
- Author Details Parquet Schema:
  - `authorid`: `large_string`
  - `orcid`: `large_string`
  - `display_name`: `large_string`
  - `display_name_alternatives`: `large_string`
  - `works_count`: `int64`
  - `cited_by_count`: `int64`
  - `last_known_institution`: `large_string`
  - `works_api_url`: `large_string`
  - `updated_date`: `large_string`
- Author Details Parquet SHA256: `62c373c747d74879585c3b1cfbbe70971c86927ec4fbc601482d3c2513ad9c1a`

## Data Sampling and Matching
- Total names in Excel: 6886
- Sampled 10 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Processed 10 names:
  - Found in local graph (API call skipped): 10
  - API calls attempted: 0
  - API calls succeeded (found OpenAlex ID): 0
  - API calls failed (no OpenAlex ID found): 0
- Found 10 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 10 matching records from authors parquet.
- Successfully read 10 matching records from author details parquet.
- Collated DataFrame has 10 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 228 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.
- Master RDF Graph now contains 238 triples.

### RDF Triple Statistics
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3
  - Top 5 most frequent values:
    - `Cross-Field`: 7 occurrences
    - `Materials Science`: 2 occurrences
    - `Economics and Business`: 1 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Ayyoob`: 1 occurrences
    - `Michael A.`: 1 occurrences
    - `Ajayan`: 1 occurrences
    - `Sanjiv Sam`: 1 occurrences
    - `Iain`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Sharifi`: 1 occurrences
    - `Angelo`: 1 occurrences
    - `Vinu`: 1 occurrences
    - `Gambhir`: 1 occurrences
    - `McCulloch`: 1 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 8
  - Top 5 most frequent values:
    - `Stanford University, United States`: 3 occurrences
    - `Hiroshima University, Japan`: 1 occurrences
    - `University of Newcastle, Australia`: 1 occurrences
    - `Princeton University, United States`: 1 occurrences
    - `Universite Paris Cite, France`: 1 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `University of Oxford, United Kingdom`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `2024-12-26 00:18:25.687592`: 1 occurrences
    - `2024-12-25 19:52:34.464423`: 1 occurrences
    - `2024-12-28 11:49:58.992909`: 1 occurrences
    - `2024-12-31 12:33:10.460061`: 1 occurrences
    - `2024-12-30 22:39:13.966263`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `["Ayyoob Sharifi", "A. Sharifi", "シャリフィ　アユーブ"]`: 1 occurrences
    - `["M Angelo", "Michael Angelo", "R. Michael Angelo", "Mike Angelo", "M. angelo", "Michael R. Angelo", "Robert Michael Angelo", "Robert M. Angelo"]`: 1 occurrences
    - `["A. Vinu", "A. K. Vinu", "Ajayan Vinu"]`: 1 occurrences
    - `["S.S Gambhir", "S. Gambhir", "S. S. Gambhir", "S. Sam Gambhir", "Sanjiv S. Gambhir", "Sanjiv Sam Gambhir", "Sanjiv Gambhir"]`: 1 occurrences
    - `["I. Mcculloch", "l. McCulloch", "Iain Mcculloch", "Ian McCulloch", "Iain A. McCulloch", "I. A. McCulloch"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 34830.20
  - Median: 33312.00
  - Q1 (25th percentile): 18877.00
  - Q3 (75th percentile): 37709.75

#### Predicate 9: `schema1:name`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Ayyoob Sharifi`: 1 occurrences
    - `Michael Angelo`: 1 occurrences
    - `Ajayan Vinu`: 1 occurrences
    - `Sanjiv Gambhir`: 1 occurrences
    - `Iain McCulloch`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `ns1:A5002835698`: 1 occurrences
    - `ns1:A5003323350`: 1 occurrences
    - `ns1:A5015562487`: 1 occurrences
    - `ns1:A5019955301`: 1 occurrences
    - `ns1:A5034296749`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 702.80
  - Median: 624.00
  - Q1 (25th percentile): 321.25
  - Q3 (75th percentile): 1196.75

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 62.42
  - Median: 56.37
  - Q1 (25th percentile): 42.82
  - Q3 (75th percentile): 65.53

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 2.50
  - Median: 2.42
  - Q1 (25th percentile): 2.05
  - Q3 (75th percentile): 2.92

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 101.90
  - Median: 101.50
  - Q1 (25th percentile): 75.50
  - Q3 (75th percentile): 135.25

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0002-8983-8613`: 1 occurrences
    - `https://orcid.org/0000-0003-1531-5067`: 1 occurrences
    - `https://orcid.org/0000-0002-7508-251X`: 1 occurrences
    - `https://orcid.org/0000-0002-2711-7554`: 1 occurrences
    - `https://orcid.org/0000-0002-6340-7217`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 9
- **Numeric Values Statistics:**
  - Count: 9
  - Mean: 0.04
  - Median: 0.00
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.00

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 20
- **Numeric Values Statistics:**
  - Count: 20
  - Mean: 681.50
  - Median: 606.50
  - Q1 (25th percentile): 319.00
  - Q3 (75th percentile): 1261.00

#### Predicate 18: `rdf:type`
- Total occurrences: 29
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 10 occurrences
    - `openalex:Author`: 10 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 19
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 19
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: Sanjiv Gambhir (A5019955301)`: 1 occurrences
    - `SciSciNet Author`: 1 occurrences
    - `Author: Vinit Parida (A5090362709)`: 1 occurrences
    - `Author: Jeffrey Tok (A5081575390)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `ns2:0000-0002-8983-8613`: 1 occurrences
    - `ns2:0000-0003-1531-5067`: 1 occurrences
    - `ns2:0000-0002-7508-251X`: 1 occurrences
    - `ns2:0000-0002-2711-7554`: 1 occurrences
    - `ns2:0000-0002-6340-7217`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Ayyoob Sharifi`: 1 occurrences
    - `Michael Angelo`: 1 occurrences
    - `Ajayan Vinu`: 1 occurrences
    - `Sanjiv S. Gambhir`: 1 occurrences
    - `Iain McCulloch`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 0.0039 seconds
- Input File Hashing: 0.0002 seconds
- Get Authors Parquet Stats: 1.0803 seconds
- Get Author Details Parquet Stats: 1.8012 seconds
- Excel Reading: 0.1283 seconds
- OpenAlex API Interaction and Graph Lookup: 0.0823 seconds
- Authors Parquet Reading: 1.3462 seconds
- Author Details Parquet Reading: 1.8515 seconds
- Data Collation: 0.0014 seconds
- Collated Parquet Saving: 0.0019 seconds
- Collated CSV Saving: 0.0009 seconds
- RDF Generation and Serialization: 0.0106 seconds
- **Overall Script**: 6.3094 seconds
