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
- Sampled 3000 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Processed 3000 names:
  - Found in local graph (API call skipped): 2019
  - API calls attempted: 981
  - API calls succeeded (found OpenAlex ID): 979
  - API calls failed (no OpenAlex ID found): 2
- Full API search results saved to: `test_run_outputs/data/api_full_results/1751516859.json`
- Found 2998 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 2898 matching records from authors parquet.
- Successfully read 2898 matching records from author details parquet.
- Collated DataFrame has 2998 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 41193 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.
- Master RDF Graph now contains 67208 triples.

### RDF Triple Statistics
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 2981
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 21
  - Top 5 most frequent values:
    - `Cross-Field`: 1420 occurrences
    - `Clinical Medicine`: 183 occurrences
    - `Biology and Biochemistry`: 124 occurrences
    - `Chemistry`: 104 occurrences
    - `Neuroscience and Behavior`: 99 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 2927
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2337
  - Top 5 most frequent values:
    - `David`: 20 occurrences
    - `Michael`: 18 occurrences
    - `Peter`: 13 occurrences
    - `Wei`: 11 occurrences
    - `Thomas`: 10 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 2906
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2003
  - Top 5 most frequent values:
    - `Zhang`: 69 occurrences
    - `Wang`: 62 occurrences
    - `Li`: 47 occurrences
    - `Liu`: 43 occurrences
    - `Chen`: 39 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 2946
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 852
  - Top 5 most frequent values:
    - `Chinese Academy of Sciences, China Mainland`: 100 occurrences
    - `Harvard University, United States`: 100 occurrences
    - `Stanford University, United States`: 48 occurrences
    - `Tsinghua University, China Mainland`: 40 occurrences
    - `University of California San Francisco, United States`: 34 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 679
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 447
  - Top 5 most frequent values:
    - `Harvard Medical School, United States`: 13 occurrences
    - `Howard Hughes Medical Institute, United States`: 11 occurrences
    - `University of California System, United States`: 10 occurrences
    - `University of Toronto, Canada`: 10 occurrences
    - `Flanders Institute for Biotechnology (VIB), Belgium`: 9 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 2898
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2898
  - Top 5 most frequent values:
    - `2024-12-27 02:44:29.000179`: 1 occurrences
    - `2024-12-30 01:31:41.965183`: 1 occurrences
    - `2024-12-29 23:27:01.579920`: 1 occurrences
    - `2024-12-29 23:56:41.937915`: 1 occurrences
    - `2024-12-30 01:05:48.126962`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 2898
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2898
  - Top 5 most frequent values:
    - `["S.‐L. Piao", "Songyi Piao", "S. Piao", "S. L. Piao", "Shilong Piao", "Shi‐Long Piao"]`: 1 occurrences
    - `["Asbjorn Hrobjartsson", "A. Hrobjartsson", "Asbjørn Hrõbjartsson", "A. Hróbjartsson", "Asbjørn Hróbjartsson", "Asbjorn Hróbjartsson", "Asbjørn Hrobjartsson"]`: 1 occurrences
    - `["Nijuan Xiang", "Ni‐Juan Xiang", "Xiang Ni‐juan", "Xiang Nijuan"]`: 1 occurrences
    - `["Balazs L. Gyorffy", "Balázs L. Györffy", "Balazs L. Györffy", "B. L. Gyorffy", "Balazs Laszlo Gyorffy", "B. L. Györffy", "Balázs L. Gyorffy", "Balazs Gyorffy", "B. L Gyorffy"]`: 1 occurrences
    - `["Guangyan Zhou", "Guang‐yan Zhou"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 4846
- **Numeric Values Statistics:**
  - Count: 4846
  - Mean: 47915.47
  - Median: 33026.50
  - Q1 (25th percentile): 18559.00
  - Q3 (75th percentile): 59280.75

#### Predicate 9: `schema1:name`
- Total occurrences: 2922
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2922
  - Top 5 most frequent values:
    - `Shilong Piao`: 1 occurrences
    - `H. Gibbs`: 1 occurrences
    - `Aaron Cohen`: 1 occurrences
    - `Xuning Feng`: 1 occurrences
    - `Buxing Han`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 2898
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2898
  - Top 5 most frequent values:
    - `ns1:A5000033522`: 1 occurrences
    - `ns1:A5110728949`: 1 occurrences
    - `ns1:A5110760432`: 1 occurrences
    - `ns1:A5110764355`: 1 occurrences
    - `ns1:A5110918844`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 4846
- **Numeric Values Statistics:**
  - Count: 4846
  - Mean: 624.78
  - Median: 457.00
  - Q1 (25th percentile): 249.00
  - Q3 (75th percentile): 788.00

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 2898
- **Numeric Values Statistics:**
  - Count: 2898
  - Mean: 93.32
  - Median: 68.60
  - Q1 (25th percentile): 46.88
  - Q3 (75th percentile): 102.59

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 2898
- **Numeric Values Statistics:**
  - Count: 2898
  - Mean: 2.62
  - Median: 2.59
  - Q1 (25th percentile): 2.23
  - Q3 (75th percentile): 2.97

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 4846
- **Numeric Values Statistics:**
  - Count: 4846
  - Mean: 106.21
  - Median: 97.00
  - Q1 (25th percentile): 70.00
  - Q3 (75th percentile): 133.00

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 2777
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2777
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-8057-2292`: 1 occurrences
    - `https://orcid.org/0000-0001-6860-348X`: 1 occurrences
    - `https://orcid.org/0000-0003-0497-1368`: 1 occurrences
    - `https://orcid.org/0000-0002-7143-7117`: 1 occurrences
    - `https://orcid.org/0000-0001-8626-2148`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 2729
- **Numeric Values Statistics:**
  - Count: 2729
  - Mean: 0.23
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.33

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 2898
- **Numeric Values Statistics:**
  - Count: 2898
  - Mean: 590.19
  - Median: 430.00
  - Q1 (25th percentile): 233.00
  - Q3 (75th percentile): 741.00

#### Predicate 18: `rdf:type`
- Total occurrences: 5809
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 2900 occurrences
    - `openalex:Author`: 2900 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 2931
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2931
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: H. Gibbs (A5111179262)`: 1 occurrences
    - `Author: Aaron Cohen (A5111751045)`: 1 occurrences
    - `Author: Xuning Feng (A5111867296)`: 1 occurrences
    - `Author: Buxing Han (A5111928301)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 2777
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2777
  - Top 5 most frequent values:
    - `ns2:0000-0001-8057-2292`: 1 occurrences
    - `ns2:0000-0001-6860-348X`: 1 occurrences
    - `ns2:0000-0003-0497-1368`: 1 occurrences
    - `ns2:0000-0002-7143-7117`: 1 occurrences
    - `ns2:0000-0001-8626-2148`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 2898
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2897
  - Top 5 most frequent values:
    - `Yu Wang`: 2 occurrences
    - `Harry Campbell`: 1 occurrences
    - `Nijuan Xiang`: 1 occurrences
    - `B. L. Györffy`: 1 occurrences
    - `Guangyan Zhou`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 0.5529 seconds
- Input File Hashing: 0.0020 seconds
- Get Authors Parquet Stats: 1.1593 seconds
- Get Author Details Parquet Stats: 1.9870 seconds
- Excel Reading: 0.1581 seconds
- OpenAlex API Interaction and Graph Lookup: 846.3913 seconds
- Authors Parquet Reading: 1.9366 seconds
- Author Details Parquet Reading: 3.2776 seconds
- Data Collation: 0.0050 seconds
- Collated Parquet Saving: 0.0106 seconds
- Collated CSV Saving: 0.0234 seconds
- RDF Generation and Serialization: 1.8956 seconds
- **Overall Script**: 857.4666 seconds
