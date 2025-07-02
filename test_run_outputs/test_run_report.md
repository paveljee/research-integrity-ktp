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
- Sampled 100 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Found 100 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 99 matching records from authors parquet.
- Successfully read 99 matching records from author details parquet.
- Collated DataFrame has 100 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Error saving collated data to CSV: NDFrame.to_csv() got an unexpected keyword argument 'line_terminator'

## RDF Graph Generation
- Successfully saved RDF graph to `test_run_outputs/data/collated_sample_data.ttl`.
- RDF Graph contains 2107 triples.

### RDF Triple Statistics
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 100
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 18
  - Top 5 most frequent values:
    - `Cross-Field`: 48 occurrences
    - `Clinical Medicine`: 6 occurrences
    - `Chemistry`: 6 occurrences
    - `Materials Science`: 5 occurrences
    - `Social Sciences`: 5 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `Michael A.`: 1 occurrences
    - `Kira S.`: 1 occurrences
    - `Yves`: 1 occurrences
    - `Rui L.`: 1 occurrences
    - `Kaibin`: 1 occurrences

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
    - `Stanford University, United States`: 4 occurrences
    - `Chinese Academy of Sciences, China Mainland`: 4 occurrences
    - `City University of Hong Kong, Hong Kong SAR`: 3 occurrences
    - `IDIBAPS, Spain`: 2 occurrences
    - `Northwestern University, United States`: 2 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 26
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 25
  - Top 5 most frequent values:
    - `University of Oxford, United Kingdom`: 2 occurrences
    - `University of Toronto, Canada`: 1 occurrences
    - `Institut Pasteur Paris, France`: 1 occurrences
    - `Chinese Academy of Sciences, China Mainland`: 1 occurrences
    - `University of Exeter, United Kingdom`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `2024-12-25 19:52:34.464423`: 1 occurrences
    - `2024-12-26 02:02:46.529767`: 1 occurrences
    - `2024-12-26 14:20:00.923637`: 1 occurrences
    - `2024-12-29 16:44:02.691841`: 1 occurrences
    - `2024-12-26 21:43:54.973884`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `["M Angelo", "Michael Angelo", "R. Michael Angelo", "Mike Angelo", "M. angelo", "Michael R. Angelo", "Robert Michael Angelo", "Robert M. Angelo"]`: 1 occurrences
    - `["Kira Makarova", "Kira S. Makarova", "K. Makarova", "K MAKAROVA", "K. S. Makarova"]`: 1 occurrences
    - `["Yves Van De Peer", "Yves De Peer", "Y. Van De Peer", "Y VANDEPEER", "Yves Van Peer", "Yves Van de Peer§", "Yves Van der Peer", "Yves Peer", "Y. van der Peer"]`: 1 occurrences
    - `["Ricardo Pires Rui L. Reis", "P. R. Kahwage", "Rui. L. Reis", "Rui R Reis", "Rui Luís Reis", "R. L. Reis", "Ruis L. Reis", "R.L Reis", "Rui L. Reis", "Rui L. Reis CEng", "R. Reis", "R. L REIS", "Ricardo Reis", "Rui Reis", "Rui Luis Reis", "Reis Rui", "R.‐L. Reis", "Priscila Reis Kahwage"]`: 1 occurrences
    - `["K. Y. Huang", "Kai‐Bin Huang", "Kaibin Huang ‐", "Kaibin Huang", "K. Huang"]`: 1 occurrences

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
    - `Michael Angelo`: 1 occurrences
    - `Kira Makarova`: 1 occurrences
    - `Yves Van de Peer`: 1 occurrences
    - `Rui Reis`: 1 occurrences
    - `Kaibin Huang`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `ns1:A5003323350`: 1 occurrences
    - `ns1:A5020935277`: 1 occurrences
    - `ns1:A5070738091`: 1 occurrences
    - `ns1:A5081499203`: 1 occurrences
    - `ns1:A5007131492`: 1 occurrences

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
    - `https://orcid.org/0000-0003-1531-5067`: 1 occurrences
    - `https://orcid.org/0000-0001-8593-7692`: 1 occurrences
    - `https://orcid.org/0000-0001-6094-2890`: 1 occurrences
    - `https://orcid.org/0000-0003-4327-3730`: 1 occurrences
    - `https://orcid.org/0000-0002-4295-6129`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 94
- **Numeric Values Statistics:**
  - Count: 94
  - Mean: 0.18
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.25

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 99
- **Numeric Values Statistics:**
  - Count: 99
  - Mean: 642.49
  - Median: 478.00
  - Q1 (25th percentile): 309.00
  - Q3 (75th percentile): 763.00

#### Predicate 18: `rdf:type`
- Total occurrences: 207
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `openalex:Author`: 99 occurrences
    - `sciscinet:Author`: 99 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 108
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 108
  - Top 5 most frequent values:
    - `SciSciNet Author`: 1 occurrences
    - `Author: Jennifer Dan (A5062245393)`: 1 occurrences
    - `Author: Kaibin Huang (A5007131492)`: 1 occurrences
    - `Author: Xu Lian (A5044401413)`: 1 occurrences
    - `Author: Peter Nordlander (A5007101561)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 93
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 93
  - Top 5 most frequent values:
    - `ns2:0000-0003-1531-5067`: 1 occurrences
    - `ns2:0000-0001-8593-7692`: 1 occurrences
    - `ns2:0000-0001-6094-2890`: 1 occurrences
    - `ns2:0000-0003-4327-3730`: 1 occurrences
    - `ns2:0000-0002-4295-6129`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 99
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 99
  - Top 5 most frequent values:
    - `Michael Angelo`: 1 occurrences
    - `Kira S. Makarova`: 1 occurrences
    - `Yves Van de Peer`: 1 occurrences
    - `Rui L. Reis`: 1 occurrences
    - `Kaibin Huang`: 1 occurrences

## Pipeline Execution Timing
- Excel Reading: 1.4974 seconds
- OpenAlex API Interaction: 38.0216 seconds
- Authors Parquet Reading: 7.7420 seconds
- Author Details Parquet Reading: 6.8362 seconds
- Data Collation: 0.0107 seconds
- Collated Parquet Saving: 0.0132 seconds
- Collated CSV Saving: 0.0000 seconds
- RDF Generation and Serialization: 0.0969 seconds
- **Overall Script**: 71.7963 seconds
