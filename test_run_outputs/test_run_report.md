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
- Sampled 6886 names (random_state=42).
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
- Query results: 5797 unique `hcr:firstName`, `hcr:lastName` pairs found
- Processed 6886 names:
  - Found in local graph (API call skipped): 6069
  - API calls attempted: 817
  - API calls succeeded (found OpenAlex ID): 811
  - API calls failed (no OpenAlex ID found): 6
- Full API search results saved to: `test_run_outputs/data/api_full_results/1751561470.json`
- Found 6880 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 6461 matching records from authors parquet.
- Successfully read 6461 matching records from author details parquet.
- Collated DataFrame has 6880 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 141221 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.

### RDF Triple Statistics
- Master RDF Graph now contains 159514 triples.
- Analyzing 24 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 6804
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 21
  - Top 5 most frequent values:
    - `Cross-Field`: 3253 occurrences
    - `Clinical Medicine`: 443 occurrences
    - `Biology and Biochemistry`: 247 occurrences
    - `Neuroscience and Behavior`: 231 occurrences
    - `Materials Science`: 228 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 6555
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 4681
  - Top 5 most frequent values:
    - `David`: 40 occurrences
    - `Michael`: 38 occurrences
    - `Peter`: 27 occurrences
    - `Wei`: 22 occurrences
    - `Thomas`: 21 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 6492
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 4124
  - Top 5 most frequent values:
    - `Wang`: 141 occurrences
    - `Zhang`: 128 occurrences
    - `Li`: 101 occurrences
    - `Chen`: 85 occurrences
    - `Liu`: 82 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 6630
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1274
  - Top 5 most frequent values:
    - `Chinese Academy of Sciences, China Mainland`: 225 occurrences
    - `Harvard University, United States`: 220 occurrences
    - `Stanford University, United States`: 120 occurrences
    - `Tsinghua University, China Mainland`: 83 occurrences
    - `Massachusetts Institute of Technology (MIT), United States`: 72 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 1445
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 792
  - Top 5 most frequent values:
    - `Harvard Medical School, United States`: 24 occurrences
    - `Howard Hughes Medical Institute, United States`: 23 occurrences
    - `Flanders Institute for Biotechnology (VIB), Belgium`: 18 occurrences
    - `Centre National de la Recherche Scientifique (CNRS), France`: 17 occurrences
    - `Harvard University, United States`: 16 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 6462
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6462
  - Top 5 most frequent values:
    - `2024-12-27 08:00:36.703471`: 1 occurrences
    - `2024-12-26 21:51:54.414936`: 1 occurrences
    - `2024-12-26 17:16:34.629455`: 1 occurrences
    - `2024-12-31 00:08:35.957249`: 1 occurrences
    - `2024-12-29 20:57:53.166691`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 6462
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6462
  - Top 5 most frequent values:
    - `["Helen J. Cross", "J.H CROSS", "Judith Cross", "J. H. Cross", "Jh Cross", "J. Cross", "J. H Cross", "Helen Cross", "Helen HJ Cross", "Harold Cross", "H. Cross", "J. Helen Cross", "Judith Helen Cross", "Cross Jh"]`: 1 occurrences
    - `["J J van Loon", "Joop J. A. Loon", "Joop J. A. van van Loon", "Joop J. van Loon", "J.J.A Van Loon", "Joop Van Loon", "J. Van Loon", "J. J. A. Van Loon", "Joop Loon", "Joop J.A van Loon", "Joop J. Avan Loon", "Joop Ja van Loon", "Joop J. A. Van Loon"]`: 1 occurrences
    - `["Wen‐Bin Hu", "Wenbin Hu", "W. B. Hu"]`: 1 occurrences
    - `["L. Yu", "Le Yu", "L.C. Yu"]`: 1 occurrences
    - `["S. H. Yin", "S. Yin", "Yin S", "Shen Yin", "Yin. Shen"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 8410
- **Numeric Values Statistics:**
  - Count: 8410
  - Mean: 46793.06
  - Median: 32266.00
  - Q1 (25th percentile): 18361.00
  - Q3 (75th percentile): 58076.00

#### Predicate 9: `schema1:name`
- Total occurrences: 6548
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6547
  - Top 5 most frequent values:
    - `Yang Zhang`: 2 occurrences
    - `J. Cross`: 1 occurrences
    - `Linas Mazutis`: 1 occurrences
    - `Maximilian Haeussler`: 1 occurrences
    - `Tobias Kippenberg`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 6462
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6462
  - Top 5 most frequent values:
    - `ns1:A5000013257`: 1 occurrences
    - `ns1:A5069611685`: 1 occurrences
    - `ns1:A5069789783`: 1 occurrences
    - `ns1:A5069757291`: 1 occurrences
    - `ns1:A5069744156`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 8410
- **Numeric Values Statistics:**
  - Count: 8410
  - Mean: 609.67
  - Median: 455.00
  - Q1 (25th percentile): 245.00
  - Q3 (75th percentile): 779.75

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 6462
- **Numeric Values Statistics:**
  - Count: 6462
  - Mean: 94.42
  - Median: 67.42
  - Q1 (25th percentile): 46.92
  - Q3 (75th percentile): 100.78

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 6462
- **Numeric Values Statistics:**
  - Count: 6462
  - Mean: 2.60
  - Median: 2.58
  - Q1 (25th percentile): 2.22
  - Q3 (75th percentile): 2.95

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 8410
- **Numeric Values Statistics:**
  - Count: 8410
  - Mean: 104.90
  - Median: 96.00
  - Q1 (25th percentile): 69.00
  - Q3 (75th percentile): 132.00

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 6196
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6196
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-7345-4829`: 1 occurrences
    - `https://orcid.org/0000-0002-0000-9342`: 1 occurrences
    - `https://orcid.org/0000-0001-5530-3613`: 1 occurrences
    - `https://orcid.org/0000-0002-3250-6714`: 1 occurrences
    - `https://orcid.org/0000-0001-8695-0274`: 1 occurrences

#### Predicate 16: `sciscinet:p_gf`
- Total occurrences: 6080
- **Numeric Values Statistics:**
  - Count: 6080
  - Mean: 0.23
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.35

#### Predicate 17: `sciscinet:p_gf_inference_counts`
- Total occurrences: 6462
- **Numeric Values Statistics:**
  - Count: 6462
  - Mean: 628547.24
  - Median: 17917.00
  - Q1 (25th percentile): 36.00
  - Q3 (75th percentile): 580964.00

#### Predicate 18: `sciscinet:p_gf_inference_sources`
- Total occurrences: 6462
- **Numeric Values Statistics:**
  - Count: 6462
  - Mean: 19.61
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
- Total occurrences: 6462
- **Numeric Values Statistics:**
  - Count: 6462
  - Mean: 573.65
  - Median: 431.00
  - Q1 (25th percentile): 233.00
  - Q3 (75th percentile): 738.00

#### Predicate 21: `rdf:type`
- Total occurrences: 12939
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 6465 occurrences
    - `openalex:Author`: 6465 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 22: `rdfs:label`
- Total occurrences: 6557
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6557
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: Fergus Shanahan (A5069986091)`: 1 occurrences
    - `Author: Chris Huntingford (A5070191910)`: 1 occurrences
    - `Author: Maximilian Haeussler (A5070184232)`: 1 occurrences
    - `Author: Tobias Kippenberg (A5070164056)`: 1 occurrences

#### Predicate 23: `owl:sameAs`
- Total occurrences: 6196
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6196
  - Top 5 most frequent values:
    - `ns2:0000-0001-7345-4829`: 1 occurrences
    - `ns2:0000-0002-0000-9342`: 1 occurrences
    - `ns2:0000-0001-5530-3613`: 1 occurrences
    - `ns2:0000-0002-3250-6714`: 1 occurrences
    - `ns2:0000-0001-8695-0274`: 1 occurrences

#### Predicate 24: `foaf:name`
- Total occurrences: 6462
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 6458
  - Top 5 most frequent values:
    - `Yu Wang`: 2 occurrences
    - `Jian Zhang`: 2 occurrences
    - `Heng Li`: 2 occurrences
    - `Yong He`: 2 occurrences
    - `J. Helen Cross`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 2.0787 seconds
- Input File Hashing: 0.0026 seconds
- Get Authors Parquet Stats: 1.1266 seconds
- Get Author Details Parquet Stats: 2.2332 seconds
- Excel Reading: 0.2035 seconds
- Author Graph Lookup Index Build: 23.4432 seconds
- OpenAlex API Interaction and Graph Lookup: 350.7763 seconds
- Authors Parquet Reading: 2.1292 seconds
- Author Details Parquet Reading: 3.3335 seconds
- Data Collation: 0.0067 seconds
- Collated Parquet Saving: 0.0165 seconds
- Collated CSV Saving: 0.0482 seconds
- RDF Generation and Serialization: 7.1869 seconds
- **Overall Script**: 392.6241 seconds
