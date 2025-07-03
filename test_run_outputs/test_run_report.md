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
- Sampled 1000 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Executed a parametrized alternative to the following SPARQL query against the master graph:
    ```
    SELECT ?author_uri ?fn ?ln WHERE {
            ?author_uri hcr:firstName ?fn ;
                        hcr:lastName ?ln .
        }
    ```
- Query results: 3908 unique author name pairs found
- Processed 1000 names:
  - Found in local graph (API call skipped): 999
  - API calls attempted: 1
  - API calls succeeded (found OpenAlex ID): 0
  - API calls failed (no OpenAlex ID found): 1
- Full API search results saved to: `test_run_outputs/data/api_full_results/1751550196.json`
- Found 0 unique OpenAlex IDs for the sample.
- No OpenAlex IDs found for the sample. Cannot proceed.

## Pipeline Execution Timing
- Master Graph Parsing: 1.2141 seconds
- Input File Hashing: 0.0002 seconds
- Get Authors Parquet Stats: 1.1128 seconds
- Get Author Details Parquet Stats: 1.8663 seconds
- Excel Reading: 0.1792 seconds
- Author Graph Lookup Index Build: 11.0790 seconds
- OpenAlex API Interaction and Graph Lookup: 0.2714 seconds

Total execution time: 15.73 seconds.

### RDF Triple Statistics
- Master RDF Graph now contains 87007 triples.
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 3969
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 21
  - Top 5 most frequent values:
    - `Cross-Field`: 1908 occurrences
    - `Clinical Medicine`: 243 occurrences
    - `Biology and Biochemistry`: 154 occurrences
    - `Neuroscience and Behavior`: 136 occurrences
    - `Chemistry`: 128 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 3874
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2986
  - Top 5 most frequent values:
    - `Michael`: 25 occurrences
    - `David`: 25 occurrences
    - `Peter`: 16 occurrences
    - `Wei`: 14 occurrences
    - `Thomas`: 13 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 3848
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 2554
  - Top 5 most frequent values:
    - `Zhang`: 85 occurrences
    - `Wang`: 84 occurrences
    - `Li`: 59 occurrences
    - `Chen`: 57 occurrences
    - `Liu`: 56 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 3906
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 997
  - Top 5 most frequent values:
    - `Harvard University, United States`: 135 occurrences
    - `Chinese Academy of Sciences, China Mainland`: 130 occurrences
    - `Stanford University, United States`: 66 occurrences
    - `Tsinghua University, China Mainland`: 51 occurrences
    - `Massachusetts Institute of Technology (MIT), United States`: 46 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 876
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 546
  - Top 5 most frequent values:
    - `Harvard Medical School, United States`: 15 occurrences
    - `Howard Hughes Medical Institute, United States`: 13 occurrences
    - `Flanders Institute for Biotechnology (VIB), Belgium`: 12 occurrences
    - `University of Toronto, Canada`: 11 occurrences
    - `University of California System, United States`: 10 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 3832
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3832
  - Top 5 most frequent values:
    - `2024-12-25 10:21:39.790135`: 1 occurrences
    - `2024-12-28 15:27:53.244109`: 1 occurrences
    - `2024-12-27 11:03:40.385192`: 1 occurrences
    - `2024-12-28 00:53:11.807902`: 1 occurrences
    - `2024-12-26 14:20:00.923637`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 3832
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3832
  - Top 5 most frequent values:
    - `["A.J. vanderGoot", "A.‐J. van der Goot", "Atze Jan Van Der Goot", "A. J. Van Der Goot", "Atze J. van der Goot", "Atze‐Jan van der Goot", "A Van Der Goot"]`: 1 occurrences
    - `["Y. L. Xiong", "Youling Xiong", "Yucong Xiong", "Youling L. Xiong", "Y Xiong", "Y.L Xiong"]`: 1 occurrences
    - `["Benjamin Levine Ebert", "Benjamin Ebert", "B. L. Ebert", "B.A.R. Ebert", "B. Ebert", "Benjamin A. R. Ebert", "Benjamin L. Ebert", "B.L Ebert"]`: 1 occurrences
    - `["C. E. Lovelock", "C. Lovelock", "Catherine Ellen Lovelock", "CatherineE. Lovelock", "Catherine E. Lovelock", "Lovelock Ce", "Catherine Lovelock", "Ce Lovelock", "Caroline Lovelock"]`: 1 occurrences
    - `["Yves Van De Peer", "Yves De Peer", "Y. Van De Peer", "Y VANDEPEER", "Yves Van Peer", "Yves Van de Peer§", "Yves Van der Peer", "Yves Peer", "Y. van der Peer"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 5780
- **Numeric Values Statistics:**
  - Count: 5780
  - Mean: 47672.16
  - Median: 32624.50
  - Q1 (25th percentile): 18445.00
  - Q3 (75th percentile): 58635.25

#### Predicate 9: `schema1:name`
- Total occurrences: 3867
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3867
  - Top 5 most frequent values:
    - `Atze van der Goot`: 1 occurrences
    - `Tobias Kippenberg`: 1 occurrences
    - `Tony James`: 1 occurrences
    - `Brendan Manning`: 1 occurrences
    - `Tamsin Ford`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 3832
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3832
  - Top 5 most frequent values:
    - `ns1:A5000027835`: 1 occurrences
    - `ns1:A5070903399`: 1 occurrences
    - `ns1:A5070668676`: 1 occurrences
    - `ns1:A5070671904`: 1 occurrences
    - `ns1:A5070738091`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 5780
- **Numeric Values Statistics:**
  - Count: 5780
  - Mean: 622.54
  - Median: 458.00
  - Q1 (25th percentile): 247.75
  - Q3 (75th percentile): 788.00

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 3832
- **Numeric Values Statistics:**
  - Count: 3832
  - Mean: 92.48
  - Median: 68.21
  - Q1 (25th percentile): 46.83
  - Q3 (75th percentile): 101.48

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 3832
- **Numeric Values Statistics:**
  - Count: 3832
  - Mean: 2.61
  - Median: 2.59
  - Q1 (25th percentile): 2.22
  - Q3 (75th percentile): 2.97

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 5780
- **Numeric Values Statistics:**
  - Count: 5780
  - Mean: 105.81
  - Median: 97.00
  - Q1 (25th percentile): 69.00
  - Q3 (75th percentile): 133.00

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 3672
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3672
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-8005-7864`: 1 occurrences
    - `https://orcid.org/0000-0003-1024-5602`: 1 occurrences
    - `https://orcid.org/0000-0001-7294-480X`: 1 occurrences
    - `https://orcid.org/0000-0002-5803-0718`: 1 occurrences
    - `https://orcid.org/0000-0002-0048-8849`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 3604
- **Numeric Values Statistics:**
  - Count: 3604
  - Mean: 0.23
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.33

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 3832
- **Numeric Values Statistics:**
  - Count: 3832
  - Mean: 588.15
  - Median: 433.00
  - Q1 (25th percentile): 233.75
  - Q3 (75th percentile): 746.00

#### Predicate 18: `rdf:type`
- Total occurrences: 7679
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 3835 occurrences
    - `openalex:Author`: 3835 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 3876
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3876
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: Alan Aspuru-Guzik (A5071495561)`: 1 occurrences
    - `Author: Karen Nelson (A5070836198)`: 1 occurrences
    - `Author: Tony James (A5070852723)`: 1 occurrences
    - `Author: Brendan Manning (A5070888686)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 3672
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3672
  - Top 5 most frequent values:
    - `ns2:0000-0001-8005-7864`: 1 occurrences
    - `ns2:0000-0003-1024-5602`: 1 occurrences
    - `ns2:0000-0001-7294-480X`: 1 occurrences
    - `ns2:0000-0002-5803-0718`: 1 occurrences
    - `ns2:0000-0002-0048-8849`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 3832
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3830
  - Top 5 most frequent values:
    - `Yu Wang`: 2 occurrences
    - `Yong He`: 2 occurrences
    - `Atze Jan van der Goot`: 1 occurrences
    - `Tamsin Ford`: 1 occurrences
    - `Oliver A. Cornely`: 1 occurrences
