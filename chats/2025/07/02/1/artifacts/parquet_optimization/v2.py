# Strategy 1: Optimized reading with threading and batching
import pyarrow.parquet as pq
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor
import numpy as np

# Convert matched_ids to set for faster lookups
matched_ids_set = set(matched_ids)

# Strategy 1A: Enhanced PyArrow reading with optimizations
def read_parquet_optimized(parquet_path, columns, matched_ids_set):
    """Optimized parquet reading with threading and batch processing"""
    try:
        # Read with optimizations
        table = pq.read_table(
            parquet_path, 
            columns=columns,
            filters=[('authorid', 'in', list(matched_ids_set))],
            use_threads=True,  # Enable multi-threading
            pre_buffer=True,   # Pre-buffer data
            use_pandas_metadata=True
        )
        return table.to_pandas()
    except Exception as e:
        print(f"Error reading {parquet_path}: {e}")
        return pd.DataFrame()

# Strategy 1B: Batch reading approach
def read_parquet_batched(parquet_path, columns, matched_ids_set, batch_size=1000):
    """Read parquet in batches to reduce memory pressure"""
    parquet_file = pq.ParquetFile(parquet_path)
    matching_dfs = []
    
    for batch in parquet_file.iter_batches(batch_size=batch_size, columns=columns):
        batch_df = batch.to_pandas()
        # Filter in pandas after reading batch
        matching_rows = batch_df[batch_df['authorid'].isin(matched_ids_set)]
        if not matching_rows.empty:
            matching_dfs.append(matching_rows)
    
    return pd.concat(matching_dfs, ignore_index=True) if matching_dfs else pd.DataFrame()

# Strategy 2: Parallel processing of row groups
def read_parquet_parallel_rowgroups(parquet_path, columns, matched_ids_set, max_workers=4):
    """Read row groups in parallel"""
    parquet_file = pq.ParquetFile(parquet_path)
    
    def process_row_group(rg_idx):
        try:
            # Read specific row group
            table = parquet_file.read_row_group(rg_idx, columns=columns)
            df = table.to_pandas()
            # Filter for matching IDs
            return df[df['authorid'].isin(matched_ids_set)]
        except:
            return pd.DataFrame()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        row_group_dfs = list(executor.map(process_row_group, range(parquet_file.num_row_groups)))
    
    # Combine results
    valid_dfs = [df for df in row_group_dfs if not df.empty]
    return pd.concat(valid_dfs, ignore_index=True) if valid_dfs else pd.DataFrame()

# Strategy 3: Smart filtering using row group statistics
def read_parquet_with_stats_filtering(parquet_path, columns, matched_ids_set):
    """Use row group statistics to skip irrelevant row groups"""
    parquet_file = pq.ParquetFile(parquet_path)
    matching_dfs = []
    
    # Get ID range for filtering
    min_id, max_id = min(matched_ids_set), max(matched_ids_set)
    
    for i in range(parquet_file.num_row_groups):
        # Get row group metadata
        rg_metadata = parquet_file.metadata.row_group(i)
        
        # Check if authorid column has statistics
        authorid_col_idx = None
        for col_idx in range(rg_metadata.num_columns):
            col_metadata = rg_metadata.column(col_idx)
            if col_metadata.path_in_schema == 'authorid':
                authorid_col_idx = col_idx
                break
        
        if authorid_col_idx is not None:
            col_stats = rg_metadata.column(authorid_col_idx).statistics
            if col_stats and col_stats.min and col_stats.max:
                # Skip row group if no overlap with our ID range
                if col_stats.max < min_id or col_stats.min > max_id:
                    continue
        
        # Read this row group
        try:
            table = parquet_file.read_row_group(i, columns=columns)
            df = table.to_pandas()
            matching_rows = df[df['authorid'].isin(matched_ids_set)]
            if not matching_rows.empty:
                matching_dfs.append(matching_rows)
        except:
            continue
    
    return pd.concat(matching_dfs, ignore_index=True) if matching_dfs else pd.DataFrame()

# Strategy 4: Create and use index files (run once to create indices)
def create_parquet_index(parquet_path, index_path):
    """Create an index file mapping authorid to row group"""
    parquet_file = pq.ParquetFile(parquet_path)
    index_data = []
    
    for rg_idx in range(parquet_file.num_row_groups):
        table = parquet_file.read_row_group(rg_idx, columns=['authorid'])
        df = table.to_pandas()
        for authorid in df['authorid'].unique():
            index_data.append({'authorid': authorid, 'row_group': rg_idx})
    
    index_df = pd.DataFrame(index_data)
    index_df.to_parquet(index_path, index=False)
    return index_df

def read_parquet_with_index(parquet_path, index_path, columns, matched_ids_set):
    """Use pre-built index to read only relevant row groups"""
    # Load index
    index_df = pd.read_parquet(index_path)
    
    # Find relevant row groups
    relevant_rgs = index_df[index_df['authorid'].isin(matched_ids_set)]['row_group'].unique()
    
    # Read only relevant row groups
    parquet_file = pq.ParquetFile(parquet_path)
    matching_dfs = []
    
    for rg_idx in relevant_rgs:
        table = parquet_file.read_row_group(rg_idx, columns=columns)
        df = table.to_pandas()
        matching_rows = df[df['authorid'].isin(matched_ids_set)]
        if not matching_rows.empty:
            matching_dfs.append(matching_rows)
    
    return pd.concat(matching_dfs, ignore_index=True) if matching_dfs else pd.DataFrame()

# Main optimized reading function
def load_parquet_data_optimized(authors_parquet_path, author_details_parquet_path, matched_ids, report_content, timings):
    """Main function using the best strategy based on your data"""
    
    # Convert to set for faster lookups
    matched_ids_set = set(matched_ids)
    
    # Column definitions
    authors_cols_to_load = ['authorid', 'avg_c10', 'avg_logc10', 'productivity', 'h_index', 'display_name', 'inference_sources', 'inference_counts', 'P(gf)']
    author_details_cols_to_load = ['authorid', 'orcid', 'display_name_alternatives', 'works_count', 'cited_by_count', 'last_known_institution', 'works_api_url', 'updated_date']
    
    # Strategy selection based on file size and pattern
    # Try stats-based filtering first (fastest if statistics are available)
    t_start = time.time()
    try:
        authors_data_df = read_parquet_with_stats_filtering(authors_parquet_path, authors_cols_to_load, matched_ids_set)
        if authors_data_df.empty:
            # Fallback to parallel row group reading
            authors_data_df = read_parquet_parallel_rowgroups(authors_parquet_path, authors_cols_to_load, matched_ids_set)
        report_content += f"- Successfully read {len(authors_data_df)} matching records from authors parquet.\n"
    except Exception as e:
        report_content += f"- Error reading authors Parquet: {e}\n"
        authors_data_df = pd.DataFrame()
    timings["Authors Parquet Reading"] = time.time() - t_start
    
    t_start = time.time()
    try:
        author_details_data_df = read_parquet_with_stats_filtering(author_details_parquet_path, author_details_cols_to_load, matched_ids_set)
        if author_details_data_df.empty:
            # Fallback to parallel row group reading
            author_details_data_df = read_parquet_parallel_rowgroups(author_details_parquet_path, author_details_cols_to_load, matched_ids_set)
        report_content += f"- Successfully read {len(author_details_data_df)} matching records from author details parquet.\n"
    except Exception as e:
        report_content += f"- Error reading author details Parquet: {e}\n"
        author_details_data_df = pd.DataFrame()
    timings["Author Details Parquet Reading"] = time.time() - t_start
    
    return authors_data_df, author_details_data_df

# STEP 1: One-time index creation script
def build_all_indices(data_dir):
    """Build indices for all parquet files - run this once"""
    import os
    
    parquet_files = {
        'authors.parquet': 'authors_index.parquet',
        'author_details.parquet': 'author_details_index.parquet'
    }
    
    for parquet_file, index_file in parquet_files.items():
        parquet_path = os.path.join(data_dir, parquet_file)
        index_path = os.path.join(data_dir, index_file)
        
        if os.path.exists(parquet_path):
            print(f"Building index for {parquet_file}...")
            start_time = time.time()
            create_parquet_index(parquet_path, index_path)
            print(f"Index built in {time.time() - start_time:.2f} seconds: {index_file}")
        else:
            print(f"Warning: {parquet_file} not found")

# STEP 2: Check if indices exist, build if needed
def ensure_indices_exist(data_dir):
    """Check if indices exist, build them if they don't"""
    import os
    
    index_files = ['authors_index.parquet', 'author_details_index.parquet']
    missing_indices = []
    
    for index_file in index_files:
        index_path = os.path.join(data_dir, index_file)
        if not os.path.exists(index_path):
            missing_indices.append(index_file)
    
    if missing_indices:
        print(f"Missing indices: {missing_indices}")
        print("Building indices...")
        build_all_indices(data_dir)
        return True
    return False

# STEP 3: Updated main function using indices
def load_parquet_data_with_indices(authors_parquet_path, author_details_parquet_path, matched_ids, report_content, timings, data_dir):
    """Main function that uses prebuilt indices for ultra-fast reading"""
    
    # Ensure indices exist
    ensure_indices_exist(data_dir)
    
    # Convert to set for faster lookups
    matched_ids_set = set(matched_ids)
    
    # Column definitions
    authors_cols_to_load = ['authorid', 'avg_c10', 'avg_logc10', 'productivity', 'h_index', 'display_name', 'inference_sources', 'inference_counts', 'P(gf)']
    author_details_cols_to_load = ['authorid', 'orcid', 'display_name_alternatives', 'works_count', 'cited_by_count', 'last_known_institution', 'works_api_url', 'updated_date']
    
    # Use indexed reading
    t_start = time.time()
    try:
        authors_index_path = os.path.join(data_dir, 'authors_index.parquet')
        authors_data_df = read_parquet_with_index(authors_parquet_path, authors_index_path, authors_cols_to_load, matched_ids_set)
        report_content += f"- Successfully read {len(authors_data_df)} matching records from authors parquet using index.\n"
    except Exception as e:
        report_content += f"- Error reading authors Parquet with index: {e}\n"
        # Fallback to optimized reading without index
        authors_data_df = read_parquet_with_stats_filtering(authors_parquet_path, authors_cols_to_load, matched_ids_set)
    timings["Authors Parquet Reading"] = time.time() - t_start
    
    t_start = time.time()
    try:
        author_details_index_path = os.path.join(data_dir, 'author_details_index.parquet')
        author_details_data_df = read_parquet_with_index(author_details_parquet_path, author_details_index_path, author_details_cols_to_load, matched_ids_set)
        report_content += f"- Successfully read {len(author_details_data_df)} matching records from author details parquet using index.\n"
    except Exception as e:
        report_content += f"- Error reading author details Parquet with index: {e}\n"
        # Fallback to optimized reading without index
        author_details_data_df = read_parquet_with_stats_filtering(author_details_parquet_path, author_details_cols_to_load, matched_ids_set)
    timings["Author Details Parquet Reading"] = time.time() - t_start
    
    return authors_data_df, author_details_data_df

# USAGE EXAMPLE:
# # One-time setup (run once)
# build_all_indices('/path/to/your/data')
# 
# # Then in your main code, replace your current reading with:
# authors_data_df, author_details_data_df = load_parquet_data_with_indices(
#     authors_parquet_path, 
#     author_details_parquet_path, 
#     matched_ids, 
#     report_content, 
#     timings,
#     data_dir='/path/to/your/data'  # Directory containing parquet files
# )