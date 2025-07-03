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
- Sampled 4110 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Executed a parametrized alternative to the following SPARQL query against the master graph:
    ```
    SELECT ?author_uri ?fn ?ln WHERE {
            ?author_uri hcr:firstName ?fn ;
                        hcr:lastName ?ln .
        }
    ```
- Query results: 4015 unique `hcr:firstName`, `hcr:lastName` pairs found
- Processed 4110 names:
  - Found in local graph (API call skipped): 4107
  - API calls attempted: 3
  - API calls succeeded (found OpenAlex ID): 0
  - API calls failed (no OpenAlex ID found): 3
- Full API search results saved to: `test_run_outputs/data/api_full_results/1751559157.json`
- Found 4107 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 3936 matching records from authors parquet.
- Successfully read 3936 matching records from author details parquet.
- Collated DataFrame has 4107 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 100766 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.

### RDF Triple Statistics
- Master RDF Graph now contains 100766 triples.
- Analyzing 24 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 4078
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 21
  - Top 5 most frequent values:
    - `Cross-Field`: 1956 occurrences
    - `Clinical Medicine`: 252 occurrences
    - `Biology and Biochemistry`: 158 occurrences
    - `Neuroscience and Behavior`: 141 occurrences
    - `Materials Science`: 129 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 3980
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3056
  - Top 5 most frequent values:
    - `Michael`: 26 occurrences
    - `David`: 25 occurrences
    - `Peter`: 16 occurrences
    - `Thomas`: 14 occurrences
    - `Wei`: 14 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 3952
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2621
  - Top 5 most frequent values:
    - `Wang`: 87 occurrences
    - `Zhang`: 87 occurrences
    - `Li`: 60 occurrences
    - `Chen`: 59 occurrences
    - `Liu`: 56 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 4012
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1009
  - Top 5 most frequent values:
    - `Harvard University, United States`: 141 occurrences
    - `Chinese Academy of Sciences, China Mainland`: 133 occurrences
    - `Stanford University, United States`: 66 occurrences
    - `Tsinghua University, China Mainland`: 51 occurrences
    - `Massachusetts Institute of Technology (MIT), United States`: 46 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 901
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 561
  - Top 5 most frequent values:
    - `Harvard Medical School, United States`: 16 occurrences
    - `Howard Hughes Medical Institute, United States`: 13 occurrences
    - `Flanders Institute for Biotechnology (VIB), Belgium`: 12 occurrences
    - `University of Toronto, Canada`: 11 occurrences
    - `University of California System, United States`: 10 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 3936
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3936
  - Top 5 most frequent values:
    - `2024-12-25 10:21:39.790135`: 1 occurrences
    - `2024-12-28 11:36:12.027084`: 1 occurrences
    - `2024-12-27 19:25:10.716035`: 1 occurrences
    - `2024-12-29 03:33:43.979907`: 1 occurrences
    - `2024-12-26 00:00:31.413715`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 3936
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3936
  - Top 5 most frequent values:
    - `["A.J. vanderGoot", "A.‐J. van der Goot", "Atze Jan Van Der Goot", "A. J. Van Der Goot", "Atze J. van der Goot", "Atze‐Jan van der Goot", "A Van Der Goot"]`: 1 occurrences
    - `["G. Long", "Georgia V. Long", "Georgina Venetia Long", "Gv Long", "Georgina Long", "G. V. Long", "Georgina V. Long", "Long GV", "GVLong", "GV Long", "G Long", "Georgina Long", "Georgina V Long", "G V Long", "GLong"]`: 1 occurrences
    - `["K. H. Crawford", "K. Crawford", "Katharine Crawford", "Katharine H. D. Crawford", "Kate H.D. Crawford", "Katharine Dusenbury"]`: 1 occurrences
    - `["Jérôme Galon", "J. Galon", "Jérome Galon", "Jerome Galon", "Jérǒme Galon"]`: 1 occurrences
    - `["Sharon I. Kirkpatrick", "Sharon Kirkpatrick", "S. I. Kirkpatrick", "S. Kirkpatrick"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 5884
- **Numeric Values Statistics:**
  - Count: 5884
  - Mean: 47681.29
  - Median: 32645.50
  - Q1 (25th percentile): 18482.00
  - Q3 (75th percentile): 58676.00

#### Predicate 9: `schema1:name`
- Total occurrences: 3973
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3973
  - Top 5 most frequent values:
    - `Atze van der Goot`: 1 occurrences
    - `Padmanee Sharma`: 1 occurrences
    - `Michael Lawrence`: 1 occurrences
    - `Patrick Meyfroidt`: 1 occurrences
    - `Karen Nelson`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 3936
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3936
  - Top 5 most frequent values:
    - `ns1:A5000027835`: 1 occurrences
    - `ns1:A5070576000`: 1 occurrences
    - `ns1:A5070608099`: 1 occurrences
    - `ns1:A5070615133`: 1 occurrences
    - `ns1:A5070627095`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 5884
- **Numeric Values Statistics:**
  - Count: 5884
  - Mean: 622.15
  - Median: 458.00
  - Q1 (25th percentile): 247.00
  - Q3 (75th percentile): 788.00

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 3936
- **Numeric Values Statistics:**
  - Count: 3936
  - Mean: 92.27
  - Median: 68.15
  - Q1 (25th percentile): 46.96
  - Q3 (75th percentile): 101.50

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 3936
- **Numeric Values Statistics:**
  - Count: 3936
  - Mean: 2.61
  - Median: 2.59
  - Q1 (25th percentile): 2.23
  - Q3 (75th percentile): 2.97

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 5884
- **Numeric Values Statistics:**
  - Count: 5884
  - Mean: 105.95
  - Median: 97.00
  - Q1 (25th percentile): 69.00
  - Q3 (75th percentile): 133.00

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 3774
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3774
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-8005-7864`: 1 occurrences
    - `https://orcid.org/0000-0001-8047-9020`: 1 occurrences
    - `https://orcid.org/0000-0003-0203-9681`: 1 occurrences
    - `https://orcid.org/0000-0002-5517-9103`: 1 occurrences
    - `https://orcid.org/0000-0001-6242-6005`: 1 occurrences

#### Predicate 16: `sciscinet:p_gf`
- Total occurrences: 3693
- **Numeric Values Statistics:**
  - Count: 3693
  - Mean: 0.23
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.33

#### Predicate 17: `sciscinet:p_gf_inference_counts`
- Total occurrences: 3936
- **Numeric Values Statistics:**
  - Count: 3936
  - Mean: 639195.64
  - Median: 16355.00
  - Q1 (25th percentile): 33.00
  - Q3 (75th percentile): 592546.00

#### Predicate 18: `sciscinet:p_gf_inference_sources`
- Total occurrences: 3936
- **Numeric Values Statistics:**
  - Count: 3936
  - Mean: 19.49
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
- Total occurrences: 3936
- **Numeric Values Statistics:**
  - Count: 3936
  - Mean: 587.68
  - Median: 434.00
  - Q1 (25th percentile): 234.00
  - Q3 (75th percentile): 746.00

#### Predicate 21: `rdf:type`
- Total occurrences: 7887
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 3939 occurrences
    - `openalex:Author`: 3939 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 22: `rdfs:label`
- Total occurrences: 3982
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3982
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: Sven Francque (A5070970519)`: 1 occurrences
    - `Author: Jiaguo Huang (A5070757305)`: 1 occurrences
    - `Author: Li-Chang Yin (A5070778973)`: 1 occurrences
    - `Author: Michael Lawrence (A5070808897)`: 1 occurrences

#### Predicate 23: `owl:sameAs`
- Total occurrences: 3774
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3774
  - Top 5 most frequent values:
    - `ns2:0000-0001-8005-7864`: 1 occurrences
    - `ns2:0000-0001-8047-9020`: 1 occurrences
    - `ns2:0000-0003-0203-9681`: 1 occurrences
    - `ns2:0000-0002-5517-9103`: 1 occurrences
    - `ns2:0000-0001-6242-6005`: 1 occurrences

#### Predicate 24: `foaf:name`
- Total occurrences: 3936
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3934
  - Top 5 most frequent values:
    - `Yong He`: 2 occurrences
    - `Yu Wang`: 2 occurrences
    - `Atze Jan van der Goot`: 1 occurrences
    - `Jintai Lin`: 1 occurrences
    - `Katharine H. D. Crawford`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 1.5300 seconds
- Input File Hashing: 0.0017 seconds
- Get Authors Parquet Stats: 1.1048 seconds
- Get Author Details Parquet Stats: 1.9287 seconds
- Excel Reading: 0.1300 seconds
- Author Graph Lookup Index Build: 11.3775 seconds
- OpenAlex API Interaction and Graph Lookup: 0.9334 seconds
- Authors Parquet Reading: 1.5286 seconds
- Author Details Parquet Reading: 2.7865 seconds
- Data Collation: 0.0055 seconds
- Collated Parquet Saving: 0.0126 seconds
- Collated CSV Saving: 0.0293 seconds
- RDF Generation and Serialization: 4.6715 seconds
- **Overall Script**: 26.0435 seconds
