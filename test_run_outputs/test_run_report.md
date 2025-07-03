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
- Sampled 5 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Processed 5 names:
  - Found in local graph (API call skipped): 0
  - API calls attempted: 5
  - API calls succeeded (found OpenAlex ID): 5
  - API calls failed (no OpenAlex ID found): 0
- Full API search results saved to: `test_run_outputs/data/api_full_results/1751500961.json`
- Found 5 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 5 matching records from authors parquet.
- Successfully read 5 matching records from author details parquet.
- Collated DataFrame has 5 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 0 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.
- Master RDF Graph now contains 123 triples.

### RDF Triple Statistics
- Analyzing 20 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2
  - Top 5 most frequent values:
    - `Cross-Field`: 4 occurrences
    - `Economics and Business`: 1 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Michael A.`: 1 occurrences
    - `Ajayan`: 1 occurrences
    - `James E.`: 1 occurrences
    - `Yi`: 1 occurrences
    - `Vinit`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Angelo`: 1 occurrences
    - `Vinu`: 1 occurrences
    - `Crowe Jr.`: 1 occurrences
    - `Luo`: 1 occurrences
    - `Parida`: 1 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Stanford University, United States`: 1 occurrences
    - `University of Newcastle, Australia`: 1 occurrences
    - `Universite Paris Cite, France`: 1 occurrences
    - `University of Science & Technology of China CAS, China Mainland`: 1 occurrences
    - `Lulea University of Technology, Sweden`: 1 occurrences

#### Predicate 5: `dcterms:modified`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `2024-12-25 19:52:34.464423`: 1 occurrences
    - `2024-12-28 11:49:58.992909`: 1 occurrences
    - `2024-12-28 02:03:56.614912`: 1 occurrences
    - `2024-12-29 19:40:05.347147`: 1 occurrences
    - `2024-12-29 18:07:02.152738`: 1 occurrences

#### Predicate 6: `schema1:alternateName`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `["M Angelo", "Michael Angelo", "R. Michael Angelo", "Mike Angelo", "M. angelo", "Michael R. Angelo", "Robert Michael Angelo", "Robert M. Angelo"]`: 1 occurrences
    - `["A. Vinu", "A. K. Vinu", "Ajayan Vinu"]`: 1 occurrences
    - `["JamesE. Crowe", "J. Crowe", "James. E. Crowe", "James E. Crowe", "J CROWEJR", "James Crowe", "J. E. Crowe", "J.E Crowe", "Crowe Je", "Jim Crowe", "James E. Crowe, Jr."]`: 1 occurrences
    - `["Luo Y", "Yi Luo", "Y. Luo", "罗毅", "Luo Yi", "Y.M. Luo"]`: 1 occurrences
    - `["V. Parida", "Vinit Parida", "Vinit Parida"]`: 1 occurrences

#### Predicate 7: `schema1:citation`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 25658.20
  - Median: 32852.00
  - Q1 (25th percentile): 16871.00
  - Q3 (75th percentile): 33772.00

#### Predicate 8: `schema1:name`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Michael Angelo`: 1 occurrences
    - `Ajayan Vinu`: 1 occurrences
    - `James Crowe Jr.`: 1 occurrences
    - `Yi Luo`: 1 occurrences
    - `Vinit Parida`: 1 occurrences

#### Predicate 9: `schema1:url`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `ns1:A5003323350`: 1 occurrences
    - `ns1:A5015562487`: 1 occurrences
    - `ns1:A5046971682`: 1 occurrences
    - `ns1:A5057282533`: 1 occurrences
    - `ns1:A5090362709`: 1 occurrences

#### Predicate 10: `schema1:workExample`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 760.00
  - Median: 655.00
  - Q1 (25th percentile): 318.00
  - Q3 (75th percentile): 1333.00

#### Predicate 11: `sciscinet:avg_c10`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 44.99
  - Median: 50.08
  - Q1 (25th percentile): 29.65
  - Q3 (75th percentile): 54.43

#### Predicate 12: `sciscinet:avg_logc10`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 2.14
  - Median: 1.99
  - Q1 (25th percentile): 1.84
  - Q3 (75th percentile): 2.55

#### Predicate 13: `sciscinet:h_index`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 88.60
  - Median: 98.00
  - Q1 (25th percentile): 92.00
  - Q3 (75th percentile): 105.00

#### Predicate 14: `sciscinet:orcid`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0003-1531-5067`: 1 occurrences
    - `https://orcid.org/0000-0002-7508-251X`: 1 occurrences
    - `https://orcid.org/0000-0002-0049-1079`: 1 occurrences
    - `https://orcid.org/0000-0003-0007-0394`: 1 occurrences
    - `https://orcid.org/0000-0003-3255-414X`: 1 occurrences

#### Predicate 15: `sciscinet:pgf_author`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 0.01
  - Median: 0.00
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.00

#### Predicate 16: `sciscinet:productivity`
- Total occurrences: 5
- **Numeric Values Statistics:**
  - Count: 5
  - Mean: 738.00
  - Median: 639.00
  - Q1 (25th percentile): 319.00
  - Q3 (75th percentile): 1261.00

#### Predicate 17: `rdf:type`
- Total occurrences: 19
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `owl:DatatypeProperty`: 6 occurrences
    - `openalex:Author`: 5 occurrences
    - `sciscinet:Author`: 5 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 18: `rdfs:label`
- Total occurrences: 14
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 14
  - Top 5 most frequent values:
    - `SciSciNet Author`: 1 occurrences
    - `OpenAlex Author Entity`: 1 occurrences
    - `ORCID`: 1 occurrences
    - `has OpenAlex ID`: 1 occurrences
    - `First Name from HCR`: 1 occurrences

#### Predicate 19: `owl:sameAs`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `ns2:0000-0003-1531-5067`: 1 occurrences
    - `ns2:0000-0002-7508-251X`: 1 occurrences
    - `ns2:0000-0002-0049-1079`: 1 occurrences
    - `ns2:0000-0003-0007-0394`: 1 occurrences
    - `ns2:0000-0003-3255-414X`: 1 occurrences

#### Predicate 20: `foaf:name`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Michael Angelo`: 1 occurrences
    - `Ajayan Vinu`: 1 occurrences
    - `James E. Crowe`: 1 occurrences
    - `Yi Luo`: 1 occurrences
    - `Vinit Parida`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 0.0004 seconds
- Input File Hashing: 0.0002 seconds
- Get Authors Parquet Stats: 1.0812 seconds
- Get Author Details Parquet Stats: 1.8087 seconds
- Excel Reading: 0.1263 seconds
- OpenAlex API Interaction and Graph Lookup: 1.5320 seconds
- Authors Parquet Reading: 1.3533 seconds
- Author Details Parquet Reading: 1.8239 seconds
- Data Collation: 0.0015 seconds
- Collated Parquet Saving: 0.0023 seconds
- Collated CSV Saving: 0.0016 seconds
- RDF Generation and Serialization: 0.0087 seconds
- **Overall Script**: 7.7461 seconds
