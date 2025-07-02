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
- Sampled 10 names (random_state=42).
- Finding OpenAlex IDs (top_k=1, highest relevance only).
- Found 10 unique OpenAlex IDs for the sample.
- Loading data from Parquet files for matched OpenAlex IDs.
- Successfully read 10 matching records from authors parquet.
- Successfully read 10 matching records from author details parquet.
- Collated DataFrame has 10 rows and 23 columns.
- Successfully saved collated data to `test_run_outputs/collated_sample_data.parquet`.

## RDF Graph Generation
- Successfully saved RDF graph to `test_run_outputs/collated_sample_data.ttl`.
- RDF Graph contains 228 triples.

### RDF Triple Statistics
- Analyzing 21 unique predicates:

#### Predicate 1: `hcr:category`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 3
  - Top 5 most frequent values:
    - `Cross-Field`: 7 occurrences
    - `Materials Science`: 2 occurrences
    - `Economics and Business`: 1 occurrences

#### Predicate 2: `hcr:firstName`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Michael A.`: 1 occurrences
    - `Ajayan`: 1 occurrences
    - `James E.`: 1 occurrences
    - `Yi`: 1 occurrences
    - `Vinit`: 1 occurrences

#### Predicate 3: `hcr:lastName`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Angelo`: 1 occurrences
    - `Vinu`: 1 occurrences
    - `Crowe Jr.`: 1 occurrences
    - `Luo`: 1 occurrences
    - `Parida`: 1 occurrences

#### Predicate 4: `hcr:primaryAffiliation`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 8
  - Top 5 most frequent values:
    - `Stanford University, United States`: 3 occurrences
    - `University of Newcastle, Australia`: 1 occurrences
    - `Universite Paris Cite, France`: 1 occurrences
    - `University of Science & Technology of China CAS, China Mainland`: 1 occurrences
    - `Lulea University of Technology, Sweden`: 1 occurrences

#### Predicate 5: `hcr:secondaryAffiliation`
- Total occurrences: 1
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 1
  - Top 5 most frequent values:
    - `University of Oxford, United Kingdom`: 1 occurrences

#### Predicate 6: `dcterms:modified`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `2024-12-28 12:19:41.550892`: 1 occurrences
    - `2024-12-28 11:49:58.992909`: 1 occurrences
    - `2024-12-28 02:03:56.614912`: 1 occurrences
    - `2024-12-29 19:40:05.347147`: 1 occurrences
    - `2024-12-29 18:07:02.152738`: 1 occurrences

#### Predicate 7: `schema1:alternateName`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `["M. A. Palladino", "Michael Angelo Palladino", "Palladino Ma", "Michael A. Palladino", "Michael Palladino", "M. Palladino", "M.A Palladino"]`: 1 occurrences
    - `["A. Vinu", "A. K. Vinu", "Ajayan Vinu"]`: 1 occurrences
    - `["JamesE. Crowe", "J. Crowe", "James. E. Crowe", "James E. Crowe", "J CROWEJR", "James Crowe", "J. E. Crowe", "J.E Crowe", "Crowe Je", "Jim Crowe", "James E. Crowe, Jr."]`: 1 occurrences
    - `["Luo Y", "Yi Luo", "Y. Luo", "罗毅", "Luo Yi", "Y.M. Luo"]`: 1 occurrences
    - `["V. Parida", "Vinit Parida", "Vinit Parida"]`: 1 occurrences

#### Predicate 8: `schema1:citation`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 36433.80
  - Median: 33312.00
  - Q1 (25th percentile): 22962.25
  - Q3 (75th percentile): 37709.75

#### Predicate 9: `schema1:name`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Michael A. Angelo`: 1 occurrences
    - `Ajayan Vinu`: 1 occurrences
    - `James E. Crowe Jr.`: 1 occurrences
    - `Yi Luo`: 1 occurrences
    - `Vinit Parida`: 1 occurrences

#### Predicate 10: `schema1:url`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `ns1:A5000260833`: 1 occurrences
    - `ns1:A5015562487`: 1 occurrences
    - `ns1:A5046971682`: 1 occurrences
    - `ns1:A5057282533`: 1 occurrences
    - `ns1:A5090362709`: 1 occurrences

#### Predicate 11: `schema1:workExample`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 720.40
  - Median: 624.00
  - Q1 (25th percentile): 321.25
  - Q3 (75th percentile): 1196.75

#### Predicate 12: `sciscinet:avg_c10`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 61.55
  - Median: 54.19
  - Q1 (25th percentile): 41.72
  - Q3 (75th percentile): 65.53

#### Predicate 13: `sciscinet:avg_logc10`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 2.54
  - Median: 2.42
  - Q1 (25th percentile): 2.23
  - Q3 (75th percentile): 2.92

#### Predicate 14: `sciscinet:h_index`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 105.70
  - Median: 101.50
  - Q1 (25th percentile): 76.25
  - Q3 (75th percentile): 135.25

#### Predicate 15: `sciscinet:orcid`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `https://orcid.org/0000-0002-4687-7612`: 1 occurrences
    - `https://orcid.org/0000-0002-7508-251X`: 1 occurrences
    - `https://orcid.org/0000-0002-0049-1079`: 1 occurrences
    - `https://orcid.org/0000-0003-0007-0394`: 1 occurrences
    - `https://orcid.org/0000-0003-3255-414X`: 1 occurrences

#### Predicate 16: `sciscinet:pgf_author`
- Total occurrences: 9
- **Numeric Values Statistics:**
  - Count: 9
  - Mean: 0.04
  - Median: 0.00
  - Q1 (25th percentile): 0.00
  - Q3 (75th percentile): 0.00

#### Predicate 17: `sciscinet:productivity`
- Total occurrences: 10
- **Numeric Values Statistics:**
  - Count: 10
  - Mean: 699.60
  - Median: 606.50
  - Q1 (25th percentile): 322.25
  - Q3 (75th percentile): 1139.75

#### Predicate 18: `rdf:type`
- Total occurrences: 29
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 5
  - Top 5 most frequent values:
    - `openalex:Author`: 10 occurrences
    - `sciscinet:Author`: 10 occurrences
    - `owl:DatatypeProperty`: 6 occurrences
    - `owl:Class`: 2 occurrences
    - `owl:ObjectProperty`: 1 occurrences

#### Predicate 19: `rdfs:label`
- Total occurrences: 19
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 19
  - Top 5 most frequent values:
    - `SciSciNet Author`: 1 occurrences
    - `Author: Ajayan Vinu (A5015562487)`: 1 occurrences
    - `Author: Ayyoob Sharifi (A5002835698)`: 1 occurrences
    - `Author: Iain McCulloch (A5034296749)`: 1 occurrences
    - `Author: Sanjiv Sam Gambhir (A5019955301)`: 1 occurrences

#### Predicate 20: `owl:sameAs`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `ns2:0000-0002-4687-7612`: 1 occurrences
    - `ns2:0000-0002-7508-251X`: 1 occurrences
    - `ns2:0000-0002-0049-1079`: 1 occurrences
    - `ns2:0000-0003-0007-0394`: 1 occurrences
    - `ns2:0000-0003-3255-414X`: 1 occurrences

#### Predicate 21: `foaf:name`
- Total occurrences: 10
- **Non-Numeric Values Statistics:**
  - Count of distinct values: 10
  - Top 5 most frequent values:
    - `Michael A. Palladino`: 1 occurrences
    - `Ajayan Vinu`: 1 occurrences
    - `James E. Crowe`: 1 occurrences
    - `Yi Luo`: 1 occurrences
    - `Vinit Parida`: 1 occurrences

## Pipeline Execution Timing
- Excel Reading: 0.5359 seconds
- OpenAlex API Interaction: 3.1146 seconds
- Authors Parquet Reading: 18.3201 seconds
- Author Details Parquet Reading: 8.1506 seconds
- Data Collation: 0.0101 seconds
- Collated Parquet Saving: 0.0131 seconds
- RDF Generation and Serialization: 0.0400 seconds
- **Overall Script**: 47.1334 seconds
