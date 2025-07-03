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
- Sampled 6000 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only, secondary sort by works count).
- OpenAlex API will be used to match the combination of `First Name`, `Last Name` from HCR list to OpenAlex ID using [Search authors](https://docs.openalex.org/api-entities/authors/search-authors) endpoint ([permalink](https://perma.cc/8ZJ8-DN4U)). Implementing the matching mechanism from [source](https://github.com/ourresearch/openalex-elastic-api) is considered for future iterations for better control and reproducibility.
- `First Name` in HCR lists may also contain middle name(s), so it is split by spaces, if any, and only the first term is used for matching.
- Executed a parametrized alternative to the following SPARQL query against the master graph:
    ```
    SELECT ?author_uri ?fn ?ln WHERE {
            ?author_uri hcr:firstName ?fn ;
                        hcr:lastName ?ln .
        }
    ```
- Query results: 4865 unique `hcr:firstName`, `hcr:lastName` pairs found
- Processed 6000 names:
  - Found in local graph (API call skipped): 5066
  - API calls attempted: 934
  - API calls succeeded (found OpenAlex ID): 930
  - API calls failed (no OpenAlex ID found): 4
- Full API search results saved to: `test_run_outputs/data/api_full_results/1751560833.json`
- Found 5996 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 5678 matching records from authors parquet.
- Successfully read 5678 matching records from author details parquet.
- Collated DataFrame has 5996 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 119916 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.

### RDF Triple Statistics
- Master RDF Graph now contains 141221 triples.
- Analyzing 24 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 5935
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 21
  - Top 5 most frequent values:
    - `Cross-Field`: 2853 occurrences
    - `Clinical Medicine`: 385 occurrences
    - `Biology and Biochemistry`: 219 occurrences
    - `Neuroscience and Behavior`: 196 occurrences
    - `Materials Science`: 190 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 5746
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 4190
  - Top 5 most frequent values:
    - `David`: 38 occurrences
    - `Michael`: 33 occurrences
    - `Peter`: 23 occurrences
    - `Wei`: 19 occurrences
    - `Thomas`: 18 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 5701
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3651
  - Top 5 most frequent values:
    - `Wang`: 127 occurrences
    - `Zhang`: 117 occurrences
    - `Li`: 84 occurrences
    - `Chen`: 78 occurrences
    - `Liu`: 75 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 5812
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1198
  - Top 5 most frequent values:
    - `Chinese Academy of Sciences, China Mainland`: 205 occurrences
    - `Harvard University, United States`: 200 occurrences
    - `Stanford University, United States`: 102 occurrences
    - `Tsinghua University, China Mainland`: 71 occurrences
    - `Massachusetts Institute of Technology (MIT), United States`: 65 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 1278
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 719
  - Top 5 most frequent values:
    - `Harvard Medical School, United States`: 22 occurrences
    - `Howard Hughes Medical Institute, United States`: 21 occurrences
    - `Centre National de la Recherche Scientifique (CNRS), France`: 16 occurrences
    - `University of Toronto, Canada`: 15 occurrences
    - `Flanders Institute for Biotechnology (VIB), Belgium`: 14 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 5678
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5678
  - Top 5 most frequent values:
    - `2024-12-27 08:00:36.703471`: 1 occurrences
    - `2024-12-30 09:11:19.158549`: 1 occurrences
    - `2024-12-31 14:29:54.630289`: 1 occurrences
    - `2024-12-25 18:48:59.629879`: 1 occurrences
    - `2024-12-25 10:13:47.122837`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 5678
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5678
  - Top 5 most frequent values:
    - `["Helen J. Cross", "J.H CROSS", "Judith Cross", "J. H. Cross", "Jh Cross", "J. Cross", "J. H Cross", "Helen Cross", "Helen HJ Cross", "Harold Cross", "H. Cross", "J. Helen Cross", "Judith Helen Cross", "Cross Jh"]`: 1 occurrences
    - `["M. Merad", "Miriam Merad", "Miriam M. Merad", "Miriam Mérad"]`: 1 occurrences
    - `["Mauricio Terrones.", "M. Terrones", "Maria Vanessa Laureano Terrones", "M. M. Terrones"]`: 1 occurrences
    - `["Nanfeng Zheng", "Nan‐Feng Zheng", "N. W. Zheng", "N. Zheng"]`: 1 occurrences
    - `["P. Ellinor", "Patrick Ellinor", "Patrick Thomas Ellinor", "P E Ellinor", "Patric T. Ellinor", "Patrick T. Ellinor", "P. T. Ellinor", "P.T Ellinor"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 7626
- **Numeric Values Statistics:**
  - Count: 7626
  - Mean: 47282.84
  - Median: 32422.00
  - Q1 (25th percentile): 18400.00
  - Q3 (75th percentile): 58647.75

#### Predicate 9: `schema1:name`
- Total occurrences: 5741
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5741
  - Top 5 most frequent values:
    - `J. Cross`: 1 occurrences
    - `Patrick Ellinor`: 1 occurrences
    - `Craig Allen`: 1 occurrences
    - `Tandong Yao`: 1 occurrences
    - `Peter Simmonds`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 5678
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5678
  - Top 5 most frequent values:
    - `ns1:A5000013257`: 1 occurrences
    - `ns1:A5070354041`: 1 occurrences
    - `ns1:A5069865883`: 1 occurrences
    - `ns1:A5069825601`: 1 occurrences
    - `ns1:A5069822855`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 7626
- **Numeric Values Statistics:**
  - Count: 7626
  - Mean: 615.67
  - Median: 457.00
  - Q1 (25th percentile): 246.25
  - Q3 (75th percentile): 786.00

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 5678
- **Numeric Values Statistics:**
  - Count: 5678
  - Mean: 94.75
  - Median: 67.29
  - Q1 (25th percentile): 46.77
  - Q3 (75th percentile): 100.76

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 5678
- **Numeric Values Statistics:**
  - Count: 5678
  - Mean: 2.61
  - Median: 2.58
  - Q1 (25th percentile): 2.22
  - Q3 (75th percentile): 2.96

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 7626
- **Numeric Values Statistics:**
  - Count: 7626
  - Mean: 105.38
  - Median: 96.00
  - Q1 (25th percentile): 69.00
  - Q3 (75th percentile): 132.00

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 5445
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5445
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-7345-4829`: 1 occurrences
    - `https://orcid.org/0000-0003-1621-0419`: 1 occurrences
    - `https://orcid.org/0000-0003-4175-6798`: 1 occurrences
    - `https://orcid.org/0000-0002-6338-7340`: 1 occurrences
    - `https://orcid.org/0000-0002-2733-0689`: 1 occurrences

#### Predicate 16: `sciscinet:p_gf`
- Total occurrences: 5333
- **Numeric Values Statistics:**
  - Count: 5333
  - Mean: 0.23
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.35

#### Predicate 17: `sciscinet:p_gf_inference_counts`
- Total occurrences: 5678
- **Numeric Values Statistics:**
  - Count: 5678
  - Mean: 631283.55
  - Median: 17752.00
  - Q1 (25th percentile): 34.25
  - Q3 (75th percentile): 576522.75

#### Predicate 18: `sciscinet:p_gf_inference_sources`
- Total occurrences: 5678
- **Numeric Values Statistics:**
  - Count: 5678
  - Mean: 19.55
  - Median: 25.00
  - Q1 (25th percentile): 5.00
  - Q3 (75th percentile): 32.00

#### Predicate 19: `sciscinet:pgf_author`
- Total occurrences: 3684
- **Numeric Values Statistics:**
  - Count: 3684
  - Mean: 0.23
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.33

#### Predicate 20: `sciscinet:productivity`
- Total occurrences: 5678
- **Numeric Values Statistics:**
  - Count: 5678
  - Mean: 580.63
  - Median: 433.50
  - Q1 (25th percentile): 234.00
  - Q3 (75th percentile): 746.00

#### Predicate 21: `rdf:type`
- Total occurrences: 11371
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 5681 occurrences
    - `openalex:Author`: 5681 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 22: `rdfs:label`
- Total occurrences: 5750
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5750
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: Daniel Lunt (A5069811512)`: 1 occurrences
    - `Author: Tandong Yao (A5070303297)`: 1 occurrences
    - `Author: Peter Simmonds (A5070291466)`: 1 occurrences
    - `Author: Chong Yoon (A5070232525)`: 1 occurrences

#### Predicate 23: `owl:sameAs`
- Total occurrences: 5445
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5445
  - Top 5 most frequent values:
    - `ns2:0000-0001-7345-4829`: 1 occurrences
    - `ns2:0000-0003-1621-0419`: 1 occurrences
    - `ns2:0000-0003-4175-6798`: 1 occurrences
    - `ns2:0000-0002-6338-7340`: 1 occurrences
    - `ns2:0000-0002-2733-0689`: 1 occurrences

#### Predicate 24: `foaf:name`
- Total occurrences: 5678
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5674
  - Top 5 most frequent values:
    - `Jian Zhang`: 2 occurrences
    - `Yu Wang`: 2 occurrences
    - `Yong He`: 2 occurrences
    - `Heng Li`: 2 occurrences
    - `J. Helen Cross`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 1.8065 seconds
- Input File Hashing: 0.0023 seconds
- Get Authors Parquet Stats: 1.1928 seconds
- Get Author Details Parquet Stats: 2.3686 seconds
- Excel Reading: 0.1469 seconds
- Author Graph Lookup Index Build: 16.6254 seconds
- OpenAlex API Interaction and Graph Lookup: 406.5664 seconds
- Authors Parquet Reading: 2.0244 seconds
- Author Details Parquet Reading: 3.1698 seconds
- Data Collation: 0.0056 seconds
- Collated Parquet Saving: 0.0156 seconds
- Collated CSV Saving: 0.0565 seconds
- RDF Generation and Serialization: 6.5095 seconds
- **Overall Script**: 440.5346 seconds
