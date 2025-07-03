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
- Processed 1000 names:
  - Found in local graph (API call skipped): 103
  - API calls attempted: 897
  - API calls succeeded (found OpenAlex ID): 896
  - API calls failed (no OpenAlex ID found): 1
- Full API search results saved to: `test_run_outputs/data/api_full_results/1751501543.json`
- Found 999 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 987 matching records from authors parquet.
- Successfully read 987 matching records from author details parquet.
- Collated DataFrame has 999 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 2107 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.
- Master RDF Graph now contains 20924 triples.

### RDF Triple Statistics
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 998
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 21
  - Top 5 most frequent values:
    - `Cross-Field`: 484 occurrences
    - `Clinical Medicine`: 51 occurrences
    - `Molecular Biology and Genetics`: 38 occurrences
    - `Neuroscience and Behavior`: 37 occurrences
    - `Biology and Biochemistry`: 37 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 990
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 865
  - Top 5 most frequent values:
    - `David`: 7 occurrences
    - `Yang`: 7 occurrences
    - `Michael A.`: 6 occurrences
    - `Wei`: 6 occurrences
    - `Peter`: 6 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 988
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 748
  - Top 5 most frequent values:
    - `Wang`: 27 occurrences
    - `Liu`: 21 occurrences
    - `Zhang`: 20 occurrences
    - `Chen`: 18 occurrences
    - `Li`: 15 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 991
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 452
  - Top 5 most frequent values:
    - `Harvard University, United States`: 37 occurrences
    - `Chinese Academy of Sciences, China Mainland`: 32 occurrences
    - `Stanford University, United States`: 18 occurrences
    - `University of California San Francisco, United States`: 12 occurrences
    - `Max Planck Society, Germany`: 12 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 220
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 176
  - Top 5 most frequent values:
    - `Imperial College London, United Kingdom`: 4 occurrences
    - `Institut National de la Sante et de la Recherche Medicale (Inserm), France`: 4 occurrences
    - `Harvard Medical School, United States`: 4 occurrences
    - `Flanders Institute for Biotechnology (VIB), Belgium`: 4 occurrences
    - `University of Toronto, Canada`: 4 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 987
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 987
  - Top 5 most frequent values:
    - `2024-12-28 19:03:33.802513`: 1 occurrences
    - `2024-12-28 04:10:26.089803`: 1 occurrences
    - `2024-12-30 07:44:46.273636`: 1 occurrences
    - `2024-12-26 07:28:33.674472`: 1 occurrences
    - `2024-12-28 21:23:28.447979`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 987
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 987
  - Top 5 most frequent values:
    - `["H. K Eltzschig", "Holger Eltzschig", "Holger Klaus Eltzschig", "Holger K. Eltzschig", "H. K. Eltzschig", "H. Eltzschig"]`: 1 occurrences
    - `["en Zhang Zhi", "Zhi‐En Zhang", "Zhi'en Zhang", "Zhien Zhang", "L Zhang", "Z. Zhang"]`: 1 occurrences
    - `["Wendy K. Smith", "W. Novis Smith", "Wendy Smith"]`: 1 occurrences
    - `["Frank Glorius", "F. Glorius"]`: 1 occurrences
    - `["G. Masters", "G.A Masters", "Gregory A. Masters", "G. A. Masters", "Gregory Masters"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 987
- **Numeric Values Statistics:**
  - Count: 987
  - Mean: 49496.42
  - Median: 33598.00
  - Q1 (25th percentile): 19303.00
  - Q3 (75th percentile): 59735.00

#### Predicate 9: `schema1:name`
- Total occurrences: 989
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 989
  - Top 5 most frequent values:
    - `Holger Eltzschig`: 1 occurrences
    - `Takanori Kanai`: 1 occurrences
    - `Frank Glorius`: 1 occurrences
    - `Gregory Masters`: 1 occurrences
    - `Longtao Ma`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 987
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 987
  - Top 5 most frequent values:
    - `ns1:A5001509341`: 1 occurrences
    - `ns1:A5030069786`: 1 occurrences
    - `ns1:A5110746760`: 1 occurrences
    - `ns1:A5017167322`: 1 occurrences
    - `ns1:A5071796883`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 987
- **Numeric Values Statistics:**
  - Count: 987
  - Mean: 645.21
  - Median: 460.00
  - Q1 (25th percentile): 249.50
  - Q3 (75th percentile): 797.50

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 987
- **Numeric Values Statistics:**
  - Count: 987
  - Mean: 91.43
  - Median: 68.51
  - Q1 (25th percentile): 47.08
  - Q3 (75th percentile): 106.84

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 987
- **Numeric Values Statistics:**
  - Count: 987
  - Mean: 2.65
  - Median: 2.63
  - Q1 (25th percentile): 2.25
  - Q3 (75th percentile): 3.02

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 987
- **Numeric Values Statistics:**
  - Count: 987
  - Mean: 108.86
  - Median: 98.00
  - Q1 (25th percentile): 72.00
  - Q3 (75th percentile): 135.00

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 941
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 941
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0002-5676-6473`: 1 occurrences
    - `https://orcid.org/0000-0002-8440-5536`: 1 occurrences
    - `https://orcid.org/0000-0002-0648-956X`: 1 occurrences
    - `https://orcid.org/0000-0002-8538-3826`: 1 occurrences
    - `https://orcid.org/0000-0002-2942-3221`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 916
- **Numeric Values Statistics:**
  - Count: 916
  - Mean: 0.22
  - Median: 0.01
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.33

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 1086
- **Numeric Values Statistics:**
  - Count: 1086
  - Mean: 619.11
  - Median: 449.00
  - Q1 (25th percentile): 246.50
  - Q3 (75th percentile): 759.00

#### Predicate 18: `rdf:type`
- Total occurrences: 1983
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `sciscinet:Author`: 987 occurrences
    - `openalex:Author`: 987 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 998
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 998
  - Top 5 most frequent values:
    - `Category from HCR`: 1 occurrences
    - `Author: Eric Brown (A5083894198)`: 1 occurrences
    - `Author: John Lambris (A5074301183)`: 1 occurrences
    - `Author: Zhien Zhang (A5030069786)`: 1 occurrences
    - `Author: Takanori Kanai (A5035900623)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 941
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 941
  - Top 5 most frequent values:
    - `ns2:0000-0002-5676-6473`: 1 occurrences
    - `ns2:0000-0002-8440-5536`: 1 occurrences
    - `ns2:0000-0002-0648-956X`: 1 occurrences
    - `ns2:0000-0002-8538-3826`: 1 occurrences
    - `ns2:0000-0002-2942-3221`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 987
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 986
  - Top 5 most frequent values:
    - `Yu Wang`: 2 occurrences
    - `John D. Lambris`: 1 occurrences
    - `Takanori Kanai∥`: 1 occurrences
    - `Wendy K. Smith`: 1 occurrences
    - `Frank Glorius`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 0.0269 seconds
- Input File Hashing: 0.0014 seconds
- Get Authors Parquet Stats: 1.0846 seconds
- Get Author Details Parquet Stats: 1.8569 seconds
- Excel Reading: 0.1430 seconds
- OpenAlex API Interaction and Graph Lookup: 417.4010 seconds
- Authors Parquet Reading: 1.4754 seconds
- Author Details Parquet Reading: 2.3567 seconds
- Data Collation: 0.0020 seconds
- Collated Parquet Saving: 0.0048 seconds
- Collated CSV Saving: 0.0078 seconds
- RDF Generation and Serialization: 0.6218 seconds
- **Overall Script**: 425.0492 seconds
