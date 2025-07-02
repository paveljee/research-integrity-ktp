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
- Sampled 50 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Found 50 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 50 matching records from authors parquet.
- Successfully read 50 matching records from author details parquet.
- Collated DataFrame has 50 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/collated_sample_data.parquet`.

## RDF Graph Generation
- Successfully saved RDF graph to `test_run_outputs/collated_sample_data.ttl`.
- RDF Graph contains 1074 triples.

### RDF Triple Statistics
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 12
  - Top 5 most frequent values:
    - `Cross-Field`: 28 occurrences
    - `Materials Science`: 4 occurrences
    - `Clinical Medicine`: 4 occurrences
    - `Social Sciences`: 3 occurrences
    - `Plant and Animal Science`: 2 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 50
  - Top 5 most frequent values:
    - `Michael A.`: 1 occurrences
    - `Mohammad Hassan`: 1 occurrences
    - `Jean Claude`: 1 occurrences
    - `Xiangming`: 1 occurrences
    - `Paul D.`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 48
  - Top 5 most frequent values:
    - `Li`: 2 occurrences
    - `Wang`: 2 occurrences
    - `Angelo`: 1 occurrences
    - `Xie`: 1 occurrences
    - `Moubarac`: 1 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 43
  - Top 5 most frequent values:
    - `Stanford University, United States`: 4 occurrences
    - `Chinese Academy of Sciences, China Mainland`: 3 occurrences
    - `King's College London, United Kingdom`: 2 occurrences
    - `City University of Hong Kong, Hong Kong SAR`: 2 occurrences
    - `University of Technology Sydney, Australia`: 1 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 12
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 12
  - Top 5 most frequent values:
    - `University of Oxford, United Kingdom`: 1 occurrences
    - `Utrecht University, Netherlands`: 1 occurrences
    - `Guy's & St Thomas' NHS Foundation Trust, United Kingdom`: 1 occurrences
    - `Centre Hospitalier Universitaire Vaudois (CHUV), Switzerland`: 1 occurrences
    - `FACIT.org, United States`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 50
  - Top 5 most frequent values:
    - `2024-12-25 19:52:34.464423`: 1 occurrences
    - `2024-12-29 13:55:16.280992`: 1 occurrences
    - `2024-12-27 23:52:27.985217`: 1 occurrences
    - `2024-12-30 13:12:20.673982`: 1 occurrences
    - `2024-12-28 14:50:45.720831`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 50
  - Top 5 most frequent values:
    - `["M Angelo", "Michael Angelo", "R. Michael Angelo", "Mike Angelo", "M. angelo", "Michael R. Angelo", "Robert Michael Angelo", "Robert M. Angelo"]`: 1 occurrences
    - `["M. H. Murad", "Mohammed Murad", "Mohammed Hassan Murad", "M H. Murad", "Murad M. Hassan", "Muhammad Hiqmal Murad", "M. Hassan Murad", "Murad Mh", "Mchammad Hassan Murad", "Hassan Murad", "Mohammad Murad", "H. Murad", "MohammadHassan. Murad", "Mohammad Hassan Murad", "MohammadH Murad", "Hassan M. Murad", "Mohammed H. Murad", "Mohammad H. Murad", "M. Murad"]`: 1 occurrences
    - `["Moubarac Jean‐Claude", "Jean‐Claude Moubarac"]`: 1 occurrences
    - `["Lulin Shen", "HE Xiang‐Ming", "Mu Xin Gao Jian", "Cheng Xin‐Qun", "HE Xiang‐ming", "Musheng Yin", "X. He", "X. ‐M. He", "Xiang‐Ming He", "L. Shen", "Zhenjiang He", "He", "Zhengping Luo", "Xiangming He", "Zhong ShengKui", "Xiang He", "Xiang Ming He", "X. M. He", "He Xiangming", "He, X. M."]`: 1 occurrences
    - `["P. D. Robbins", "P.D Robbins", "P D. Robbins", "P. Robbins", "Paul Robbins", "P. David Robbins", "Pd Robbins", "Paul D. Robbins"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 50
- **Numeric Values Statistics:**
  - Count: 50
  - Mean: 50795.38
  - Median: 31698.50
  - Q1 (25th percentile): 16124.50
  - Q3 (75th percentile): 73697.50

#### Predicate 9: `schema1:name`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 50
  - Top 5 most frequent values:
    - `Michael Angelo`: 1 occurrences
    - `Mohammad Murad`: 1 occurrences
    - `Jean Moubarac`: 1 occurrences
    - `Xiangming He`: 1 occurrences
    - `Paul Robbins`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 50
  - Top 5 most frequent values:
    - `ns1:A5003323350`: 1 occurrences
    - `ns1:A5054802858`: 1 occurrences
    - `ns1:A5027132612`: 1 occurrences
    - `ns1:A5100637063`: 1 occurrences
    - `ns1:A5040467127`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 50
- **Numeric Values Statistics:**
  - Count: 50
  - Mean: 672.00
  - Median: 468.00
  - Q1 (25th percentile): 324.75
  - Q3 (75th percentile): 861.50

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 50
- **Numeric Values Statistics:**
  - Count: 50
  - Mean: 83.46
  - Median: 58.68
  - Q1 (25th percentile): 39.43
  - Q3 (75th percentile): 93.31

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 50
- **Numeric Values Statistics:**
  - Count: 50
  - Mean: 2.61
  - Median: 2.50
  - Q1 (25th percentile): 2.18
  - Q3 (75th percentile): 2.97

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 50
- **Numeric Values Statistics:**
  - Count: 50
  - Mean: 111.76
  - Median: 98.50
  - Q1 (25th percentile): 70.00
  - Q3 (75th percentile): 148.75

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 48
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 48
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0003-1531-5067`: 1 occurrences
    - `https://orcid.org/0000-0002-7508-251X`: 1 occurrences
    - `https://orcid.org/0000-0001-8409-7855`: 1 occurrences
    - `https://orcid.org/0000-0001-7146-4097`: 1 occurrences
    - `https://orcid.org/0000-0003-1068-7099`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 48
- **Numeric Values Statistics:**
  - Count: 48
  - Mean: 0.17
  - Median: 0.00
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.26

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 50
- **Numeric Values Statistics:**
  - Count: 50
  - Mean: 646.12
  - Median: 449.50
  - Q1 (25th percentile): 316.00
  - Q3 (75th percentile): 810.50

#### Predicate 18: `rdf:type`
- Total occurrences: 109
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `openalex:Author`: 50 occurrences
    - `sciscinet:Author`: 50 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 59
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 59
  - Top 5 most frequent values:
    - `SciSciNet Author`: 1 occurrences
    - `Author: Wolfgang Fendler (A5062907808)`: 1 occurrences
    - `Author: Hin-Lap Yip (A5006899454)`: 1 occurrences
    - `Author: Yu-Guo Guo (A5070372567)`: 1 occurrences
    - `Author: Xiong Lou (A5032280861)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 48
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 48
  - Top 5 most frequent values:
    - `ns2:0000-0003-1531-5067`: 1 occurrences
    - `ns2:0000-0002-7508-251X`: 1 occurrences
    - `ns2:0000-0001-8409-7855`: 1 occurrences
    - `ns2:0000-0001-7146-4097`: 1 occurrences
    - `ns2:0000-0003-1068-7099`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 50
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 50
  - Top 5 most frequent values:
    - `Michael Angelo`: 1 occurrences
    - `M. Hassan Murad`: 1 occurrences
    - `Jean‐Claude Moubarac`: 1 occurrences
    - `Xiangming He`: 1 occurrences
    - `Paul D. Robbins`: 1 occurrences

## Pipeline Execution Timing
- Excel Reading: 0.3086 seconds
- OpenAlex API Interaction: 23.6355 seconds
- Authors Parquet Reading: 4.7659 seconds
- Author Details Parquet Reading: 5.3097 seconds
- Data Collation: 0.0273 seconds
- Collated Parquet Saving: 0.0287 seconds
- RDF Generation and Serialization: 0.0621 seconds
- **Overall Script**: 47.1517 seconds
