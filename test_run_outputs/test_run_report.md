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
- Master graph currently has 2107 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.
- Master RDF Graph now contains 2117 triples.

### RDF Triple Statistics
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 100
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 18
  - Top 5 most frequent values:
    - `Cross-Field`: 48 occurrences
    - `Chemistry`: 6 occurrences
    - `Clinical Medicine`: 6 occurrences
    - `Social Sciences`: 5 occurrences
    - `Materials Science`: 5 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `Holger`: 1 occurrences
    - `Bas E.`: 1 occurrences
    - `Adam A.`: 1 occurrences
    - `Jeffrey B. -H.`: 1 occurrences
    - `Rui L.`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 91
  - Top 5 most frequent values:
    - `Wang`: 4 occurrences
    - `Li`: 3 occurrences
    - `Peng`: 2 occurrences
    - `Liu`: 2 occurrences
    - `Lin`: 2 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 84
  - Top 5 most frequent values:
    - `Chinese Academy of Sciences, China Mainland`: 4 occurrences
    - `Stanford University, United States`: 4 occurrences
    - `City University of Hong Kong, Hong Kong SAR`: 3 occurrences
    - `IDIBAPS, Spain`: 2 occurrences
    - `King's College London, United Kingdom`: 2 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 26
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 25
  - Top 5 most frequent values:
    - `University of Oxford, United Kingdom`: 2 occurrences
    - `Guy's & St Thomas' NHS Foundation Trust, United Kingdom`: 1 occurrences
    - `University of Toronto, Canada`: 1 occurrences
    - `University of North Carolina, United States`: 1 occurrences
    - `University of Johannesburg, South Africa`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `2024-12-28 19:03:33.802513`: 1 occurrences
    - `2024-12-28 20:29:34.221575`: 1 occurrences
    - `2024-12-30 07:14:29.200566`: 1 occurrences
    - `2024-12-25 22:35:35.396265`: 1 occurrences
    - `2024-12-29 16:44:02.691841`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `["H. K Eltzschig", "Holger Eltzschig", "Holger Klaus Eltzschig", "Holger K. Eltzschig", "H. K. Eltzschig", "H. Eltzschig"]`: 1 occurrences
    - `["E. Bas Dutilh", "Bas Dutilh", "B Dutilh", "Bas E. Dutilh", "B. E. Dutilh"]`: 1 occurrences
    - `["Adam A. Scaife", "A. Scaife", "Adam Arthur Scaife", "Adam Scaife", "A. A. Scaife"]`: 1 occurrences
    - `["Jeffery B.‐H. Tok", "J Tok", "Jeffrey B.‐H. Tok", "J. B.‐H. Tok", "Jeffrey Tok", "Jeffrey B.H. Tok", "J B Tok", "Jeffrey B. Tok", "Jeffrey B.‐H Tok"]`: 1 occurrences
    - `["Ricardo Pires Rui L. Reis", "P. R. Kahwage", "Rui. L. Reis", "Rui R Reis", "Rui Luís Reis", "R. L. Reis", "Ruis L. Reis", "R.L Reis", "Rui L. Reis", "Rui L. Reis CEng", "R. Reis", "R. L REIS", "Ricardo Reis", "Rui Reis", "Rui Luis Reis", "Reis Rui", "R.‐L. Reis", "Priscila Reis Kahwage"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 99
- **Numeric Values Statistics:**
  - Count: 99
  - Mean: 53375.05
  - Median: 36401.00
  - Q1 (25th percentile): 21543.00
  - Q3 (75th percentile): 74503.00

#### Predicate 9: `schema1:name`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `Holger Eltzschig`: 1 occurrences
    - `Bas Dutilh`: 1 occurrences
    - `Adam Scaife`: 1 occurrences
    - `Jeffrey Tok`: 1 occurrences
    - `Rui Reis`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `ns1:A5001509341`: 1 occurrences
    - `ns1:A5084321697`: 1 occurrences
    - `ns1:A5081992122`: 1 occurrences
    - `ns1:A5081575390`: 1 occurrences
    - `ns1:A5081499203`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 99
- **Numeric Values Statistics:**
  - Count: 99
  - Mean: 669.16
  - Median: 486.00
  - Q1 (25th percentile): 318.00
  - Q3 (75th percentile): 776.00

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 99
- **Numeric Values Statistics:**
  - Count: 99
  - Mean: 87.55
  - Median: 64.99
  - Q1 (25th percentile): 43.41
  - Q3 (75th percentile): 101.74

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 99
- **Numeric Values Statistics:**
  - Count: 99
  - Mean: 2.63
  - Median: 2.61
  - Q1 (25th percentile): 2.25
  - Q3 (75th percentile): 2.96

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 99
- **Numeric Values Statistics:**
  - Count: 99
  - Mean: 113.68
  - Median: 105.00
  - Q1 (25th percentile): 77.50
  - Q3 (75th percentile): 141.50

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 93
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 93
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0002-5676-6473`: 1 occurrences
    - `https://orcid.org/0000-0003-2954-3896`: 1 occurrences
    - `https://orcid.org/0000-0002-4295-6129`: 1 occurrences
    - `https://orcid.org/0000-0002-9826-0753`: 1 occurrences
    - `https://orcid.org/0000-0002-7563-4046`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 94
- **Numeric Values Statistics:**
  - Count: 94
  - Mean: 0.18
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.25

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 109
- **Numeric Values Statistics:**
  - Count: 109
  - Mean: 646.07
  - Median: 504.00
  - Q1 (25th percentile): 311.00
  - Q3 (75th percentile): 766.00

#### Predicate 18: `rdf:type`
- Total occurrences: 207
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 99 occurrences
    - `openalex:Author`: 99 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 108
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 108
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: Xiaoxiong Zeng (A5069635671)`: 1 occurrences
    - `Author: Adam Scaife (A5081992122)`: 1 occurrences
    - `Author: Jeffrey Tok (A5081575390)`: 1 occurrences
    - `Author: Rui Reis (A5081499203)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 93
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 93
  - Top 5 most frequent values:
    - `ns2:0000-0002-5676-6473`: 1 occurrences
    - `ns2:0000-0003-2954-3896`: 1 occurrences
    - `ns2:0000-0002-4295-6129`: 1 occurrences
    - `ns2:0000-0002-9826-0753`: 1 occurrences
    - `ns2:0000-0002-7563-4046`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `Holger K. Eltzschig`: 1 occurrences
    - `Bas E. Dutilh`: 1 occurrences
    - `Adam A. Scaife`: 1 occurrences
    - `Jeffrey B.‐H. Tok`: 1 occurrences
    - `Rui L. Reis`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 0.0255 seconds
- Input File Hashing: 0.0002 seconds
- Get Authors Parquet Stats: 1.0913 seconds
- Get Author Details Parquet Stats: 1.8065 seconds
- Excel Reading: 0.1264 seconds
- OpenAlex API Interaction and Graph Lookup: 0.0967 seconds
- Authors Parquet Reading: 1.4463 seconds
- Author Details Parquet Reading: 1.9572 seconds
- Data Collation: 0.0019 seconds
- Collated Parquet Saving: 0.0022 seconds
- Collated CSV Saving: 0.0012 seconds
- RDF Generation and Serialization: 0.0395 seconds
- **Overall Script**: 6.5964 seconds
