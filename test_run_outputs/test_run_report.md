# Test Run Report

## Input Files Statistics
- Excel File (`dummy_names.xlsx`): SHA256 = `571e242810d73080bfa575636586d1a4c0306a60e7c43688cbc24a9d7aea0c32`
- Authors Parquet Rows: `5`
- Authors Parquet Columns: `9`
- Authors Parquet Schema:
  - `authorid`: `string`
  - `avg_c10`: `double`
  - `avg_logc10`: `double`
  - `productivity`: `double`
  - `h_index`: `int64`
  - `display_name`: `string`
  - `inference_sources`: `list<element: string>`
  - `inference_counts`: `list<element: int64>`
  - `P(gf)`: `double`
- Authors Parquet SHA256: `76018b20e7931a1221cee8858daaeff988140dd16e951e8eeaa349cc5a15cf24`
- Author Details Parquet Rows: `5`
- Author Details Parquet Columns: `8`
- Author Details Parquet Schema:
  - `authorid`: `string`
  - `orcid`: `string`
  - `display_name_alternatives`: `list<element: string>`
  - `works_count`: `int64`
  - `cited_by_count`: `int64`
  - `last_known_institution`: `string`
  - `works_api_url`: `string`
  - `updated_date`: `timestamp[ns]`
- Author Details Parquet SHA256: `cb94af1162e2aeb9f9fc27444085518d54af42a14ff2005dbdd5032b6e2d3edc`

## Data Sampling and Matching
- Total names in Excel: 6
- Sampled 5 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Processed 5 names:
  - Found in local graph (API call skipped): 0
  - API calls attempted: 5
  - API calls succeeded (found OpenAlex ID): 5
  - API calls failed (no OpenAlex ID found): 0
- Found 5 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 1 matching records from authors parquet.
- Successfully read 1 matching records from author details parquet.
- Collated DataFrame has 5 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.parquet`.
- Successfully saved collated data to `test_run_outputs/data/collated_sample_data.csv`.

## RDF Graph Generation
- Master graph currently has 0 triples before adding new data from this run.
- Successfully saved master RDF graph to `test_run_outputs/data/master_knowledge_graph.ttl`.
- Master RDF Graph now contains 76 triples.

### RDF Triple Statistics
- Analyzing 22 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3
  - Top 5 most frequent values:
    - `Art`: 2 occurrences
    - `Science`: 2 occurrences
    - `Misc`: 1 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Michael`: 1 occurrences
    - `Leonardo`: 1 occurrences
    - `Unknown`: 1 occurrences
    - `Raphael`: 1 occurrences
    - `Marie`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Angelo`: 1 occurrences
    - `Vinci`: 1 occurrences
    - `Author`: 1 occurrences
    - `Sanzio`: 1 occurrences
    - `Curie`: 1 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Vatican`: 1 occurrences
    - `Milan`: 1 occurrences
    - `Nowhere`: 1 occurrences
    - `Florence`: 1 occurrences
    - `Paris Sorbonne`: 1 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 4
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 4
  - Top 5 most frequent values:
    - `Florence`: 1 occurrences
    - `Amboise`: 1 occurrences
    - `Rome`: 1 occurrences
    - `Warsaw`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `2023-01-01 00:00:00`: 1 occurrences

#### Predicate 7: `schema1:affiliation`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `Florence Academy`: 1 occurrences

#### Predicate 8: `schema1:alternateName`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `Michelangelo Buonarroti`: 1 occurrences

#### Predicate 9: `schema1:citation`
- Total occurrences: 1
- **Numeric Values Statistics:**
  - Count: 1
  - Mean: 1000.00
  - Median: 1000.00
  - Q1 (25th percentile): 1000.00
  - Q3 (75th percentile): 1000.00

#### Predicate 10: `schema1:name`
- Total occurrences: 5
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `Michael Angelo`: 1 occurrences
    - `Leonardo Vinci`: 1 occurrences
    - `Unknown Author`: 1 occurrences
    - `Raphael Sanzio`: 1 occurrences
    - `Marie Curie`: 1 occurrences

#### Predicate 11: `schema1:url`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `url1`: 1 occurrences

#### Predicate 12: `schema1:workExample`
- Total occurrences: 1
- **Numeric Values Statistics:**
  - Count: 1
  - Mean: 138.00
  - Median: 138.00
  - Q1 (25th percentile): 138.00
  - Q3 (75th percentile): 138.00

#### Predicate 13: `sciscinet:avg_c10`
- Total occurrences: 1
- **Numeric Values Statistics:**
  - Count: 1
  - Mean: 1.00
  - Median: 1.00
  - Q1 (25th percentile): 1.00
  - Q3 (75th percentile): 1.00

#### Predicate 14: `sciscinet:avg_logc10`
- Total occurrences: 1
- **Numeric Values Statistics:**
  - Count: 1
  - Mean: 0.10
  - Median: 0.10
  - Q1 (25th percentile): 0.10
  - Q3 (75th percentile): 0.10

#### Predicate 15: `sciscinet:h_index`
- Total occurrences: 1
- **Numeric Values Statistics:**
  - Count: 1
  - Mean: 5.00
  - Median: 5.00
  - Q1 (25th percentile): 5.00
  - Q3 (75th percentile): 5.00

#### Predicate 16: `sciscinet:orcid`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0001-2345-6789`: 1 occurrences

#### Predicate 17: `sciscinet:pgf_author`
- Total occurrences: 1
- **Numeric Values Statistics:**
  - Count: 1
  - Mean: 0.90
  - Median: 0.90
  - Q1 (25th percentile): 0.90
  - Q3 (75th percentile): 0.90

#### Predicate 18: `sciscinet:productivity`
- Total occurrences: 1
- **Numeric Values Statistics:**
  - Count: 1
  - Mean: 10.00
  - Median: 10.00
  - Q1 (25th percentile): 10.00
  - Q3 (75th percentile): 10.00

#### Predicate 19: `rdf:type`
- Total occurrences: 19
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `owl:DatatypeProperty`: 6 occurrences
    - `sciscinet:Author`: 5 occurrences
    - `openalex:Author`: 5 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 20: `rdfs:label`
- Total occurrences: 14
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 14
  - Top 5 most frequent values:
    - `SciSciNet Author`: 1 occurrences
    - `OpenAlex Author Entity`: 1 occurrences
    - `ORCID`: 1 occurrences
    - `has OpenAlex ID`: 1 occurrences
    - `First Name from HCR`: 1 occurrences

#### Predicate 21: `owl:sameAs`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `ns1:0000-0001-2345-6789`: 1 occurrences

#### Predicate 22: `foaf:name`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `Michael Angelo`: 1 occurrences

## Pipeline Execution Timing
- Master Graph Parsing: 0.0008 seconds
- Input File Hashing: 0.0001 seconds
- Get Authors Parquet Stats: 0.0003 seconds
- Get Author Details Parquet Stats: 0.0002 seconds
- Excel Reading: 0.1289 seconds
- OpenAlex API Interaction and Graph Lookup: 2.4662 seconds
- Authors Parquet Reading: 0.0225 seconds
- Author Details Parquet Reading: 0.0033 seconds
- Data Collation: 0.0059 seconds
- Collated Parquet Saving: 0.0059 seconds
- Collated CSV Saving: 0.0104 seconds
- RDF Generation and Serialization: 0.0286 seconds
- **Overall Script**: 2.6782 seconds
