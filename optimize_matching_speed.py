import pyarrow.parquet as pq
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import os # Added for index path joining

# Strategy 1A: Enhanced PyArrow reading with optimizations
def read_parquet_optimized(parquet_path, columns, matched_ids_set):
    """Optimized parquet reading with PyArrow filters and threading."""
    try:
        table = pq.read_table(
            parquet_path,
            columns=columns,
            filters=[('authorid', 'in', list(matched_ids_set))] if matched_ids_set else None,
            use_threads=True,
            pre_buffer=True,
            use_pandas_metadata=True
        )
        return table.to_pandas()
    except Exception as e:
        # print(f"Error in read_parquet_optimized for {parquet_path}: {e}")
        return pd.DataFrame()

# Strategy 1B: Batch reading approach
def read_parquet_batched(parquet_path, columns, matched_ids_set, batch_size=10000): # Increased batch_size
    """Read parquet in batches to reduce memory pressure, filter in pandas."""
    parquet_file = pq.ParquetFile(parquet_path)
    matching_dfs = []
    try:
        for batch in parquet_file.iter_batches(batch_size=batch_size, columns=columns):
            batch_df = batch.to_pandas()
            if not matched_ids_set: # If no IDs, means load all (though typically we'd have IDs)
                 matching_dfs.append(batch_df)
            elif not batch_df.empty and 'authorid' in batch_df.columns:
                matching_rows = batch_df[batch_df['authorid'].isin(matched_ids_set)]
                if not matching_rows.empty:
                    matching_dfs.append(matching_rows)
        return pd.concat(matching_dfs, ignore_index=True) if matching_dfs else pd.DataFrame()
    except Exception as e:
        # print(f"Error in read_parquet_batched for {parquet_path}: {e}")
        return pd.DataFrame()

# Strategy 2: Parallel processing of row groups
def read_parquet_parallel_rowgroups(parquet_path, columns, matched_ids_set, max_workers=4):
    """Read row groups in parallel and filter."""
    try:
        parquet_file = pq.ParquetFile(parquet_path)
        if parquet_file.num_row_groups == 0:
            return pd.DataFrame()

        def process_row_group(rg_idx):
            try:
                table = parquet_file.read_row_group(rg_idx, columns=columns)
                df = table.to_pandas()
                if not matched_ids_set: # Load all if no specific IDs
                    return df
                if not df.empty and 'authorid' in df.columns:
                    return df[df['authorid'].isin(matched_ids_set)]
                return pd.DataFrame()
            except Exception: # pylint: disable=broad-except
                # print(f"Error processing row group {rg_idx} in {parquet_path}: {e_rg}")
                return pd.DataFrame()

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(process_row_group, i) for i in range(parquet_file.num_row_groups)]
            row_group_dfs = [future.result() for future in futures]

        valid_dfs = [df for df in row_group_dfs if not df.empty]
        return pd.concat(valid_dfs, ignore_index=True) if valid_dfs else pd.DataFrame()
    except Exception as e:
        # print(f"Error in read_parquet_parallel_rowgroups for {parquet_path}: {e}")
        return pd.DataFrame()

# Strategy 3: Smart filtering using row group statistics (if 'authorid' is string, stats may not be min/max comparable for range)
def read_parquet_with_stats_filtering(parquet_path, columns, matched_ids_set):
    """Use row group statistics to skip irrelevant row groups.
    Note: This is most effective if 'authorid' is numeric or sortable with meaningful min/max stats.
    If 'authorid' is a hash or UUID string, range filtering (min_id, max_id) might not be effective.
    However, it can still check for `null_count == row_count` to skip empty groups for 'authorid'.
    """
    try:
        parquet_file = pq.ParquetFile(parquet_path)
        if parquet_file.num_row_groups == 0:
            return pd.DataFrame()
        matching_dfs = []

        # Attempt to get string representations for comparison if IDs are strings
        # This strategy is less effective for arbitrary string IDs unless there's a known prefix or pattern.
        # For now, we rely on PyArrow's internal filter pushdown where possible or full scan of relevant groups.

        for i in range(parquet_file.num_row_groups):
            rg_metadata = parquet_file.metadata.row_group(i)
            skip_group = False
            authorid_col_stats = None

            for col_idx in range(rg_metadata.num_columns):
                col_chunk_metadata = rg_metadata.column(col_idx)
                if col_chunk_metadata.path_in_schema == 'authorid': # Make sure this matches the actual column name in Parquet
                    if col_chunk_metadata.statistics:
                        authorid_col_stats = col_chunk_metadata.statistics
                        # If all values in this row group for 'authorid' are null, and we are looking for specific IDs, skip.
                        if authorid_col_stats.null_count == rg_metadata.num_rows and matched_ids_set:
                            skip_group = True
                            break
                        # If min/max are available and matched_ids_set is not empty, you could try more complex filtering
                        # For general string IDs, direct min/max range check is tricky.
                        # Example: if col_stats.min and col_stats.max and matched_ids_set:
                        #   if not any(col_stats.min <= mid <= col_stats.max for mid in matched_ids_set): # simplified check
                        #       could_contain_ids = False # This logic needs to be robust for string types
            if skip_group:
                continue

            try:
                table = parquet_file.read_row_group(i, columns=columns)
                df = table.to_pandas()
                if not matched_ids_set:
                    matching_dfs.append(df)
                elif not df.empty and 'authorid' in df.columns:
                    matching_rows = df[df['authorid'].isin(matched_ids_set)]
                    if not matching_rows.empty:
                        matching_dfs.append(matching_rows)
            except Exception: # pylint: disable=broad-except
                # print(f"Error reading row group {i} with stats filtering in {parquet_path}: {e_rg_stats}")
                continue
        return pd.concat(matching_dfs, ignore_index=True) if matching_dfs else pd.DataFrame()
    except Exception as e:
        # print(f"Error in read_parquet_with_stats_filtering for {parquet_path}: {e}")
        return pd.DataFrame()

# --- Indexing Strategy Helper Functions ---
def create_parquet_index(parquet_path, index_file_path, id_column='authorid'):
    """Create an index file mapping id_column to row group.
    Index file stores a DataFrame with two columns: `id_column` and `row_group_idx`.
    """
    if not os.path.exists(parquet_path):
        # print(f"Parquet file not found for indexing: {parquet_path}")
        return pd.DataFrame()
    try:
        parquet_file = pq.ParquetFile(parquet_path)
        if parquet_file.num_row_groups == 0:
            return pd.DataFrame()

        index_data = []
        for rg_idx in range(parquet_file.num_row_groups):
            try:
                table = parquet_file.read_row_group(rg_idx, columns=[id_column])
                df = table.to_pandas()
                for unique_id in df[id_column].unique():
                    if pd.notna(unique_id):
                        index_data.append({id_column: unique_id, 'row_group_idx': rg_idx})
            except Exception: # pylint: disable=broad-except
                # print(f"Error reading row group {rg_idx} for index creation in {parquet_path}: {e_idx_rg}")
                continue # Skip this row group

        if not index_data:
            # print(f"No indexable data found in {parquet_path} for column {id_column}")
            return pd.DataFrame()

        index_df = pd.DataFrame(index_data)
        index_df.drop_duplicates(inplace=True)
        os.makedirs(os.path.dirname(index_file_path), exist_ok=True)
        index_df.to_parquet(index_file_path, index=False)
        # print(f"Index created for {parquet_path} at {index_file_path}")
        return index_df
    except Exception as e:
        # print(f"Error creating parquet index for {parquet_path}: {e}")
        return pd.DataFrame()

def get_index_file_path(parquet_path, id_column='authorid'):
    """Generates a standard name for an index file based on the parquet file path and ID column."""
    directory, filename = os.path.split(parquet_path)
    name, _ = os.path.splitext(filename)
    index_filename = f"{name}_{id_column}_index.parquet"
    return os.path.join(directory, index_filename)


# Strategy 4: Use pre-built index files
def read_parquet_with_index(parquet_path, columns, matched_ids_set, id_column='authorid'):
    """Use pre-built index to read only relevant row groups."""
    index_file_path = get_index_file_path(parquet_path, id_column)

    if not os.path.exists(index_file_path):
        # print(f"Index file not found: {index_file_path}. Consider creating it first.")
        # Fallback: Try creating the index on-the-fly or use another strategy
        # For this exercise, we'll try to create it. In a production system, this might be a separate step.
        # print(f"Attempting to create index for {parquet_path} on-the-fly...")
        create_parquet_index(parquet_path, index_file_path, id_column)
        if not os.path.exists(index_file_path):
            # print(f"Failed to create index on-the-fly. Falling back to full scan (optimized).")
            return read_parquet_optimized(parquet_path, columns, matched_ids_set) # Fallback

    try:
        index_df = pd.read_parquet(index_file_path)
        if index_df.empty or id_column not in index_df.columns or 'row_group_idx' not in index_df.columns:
            # print(f"Index file {index_file_path} is empty or malformed. Falling back.")
            return read_parquet_optimized(parquet_path, columns, matched_ids_set)

        relevant_rgs = index_df[index_df[id_column].isin(matched_ids_set)]['row_group_idx'].unique()

        if len(relevant_rgs) == 0 and matched_ids_set: # If IDs specified but no relevant row groups
            return pd.DataFrame()

        parquet_file = pq.ParquetFile(parquet_path)
        if parquet_file.num_row_groups == 0:
            return pd.DataFrame()

        matching_dfs = []
        for rg_idx in relevant_rgs:
            if rg_idx >= parquet_file.num_row_groups: # Safety check
                # print(f"Warning: Row group index {rg_idx} out of bounds for {parquet_path}")
                continue
            try:
                table = parquet_file.read_row_group(rg_idx, columns=columns)
                df = table.to_pandas()
                if not matched_ids_set: # Should not happen if relevant_rgs were derived from matched_ids_set
                    matching_dfs.append(df)
                elif not df.empty and 'authorid' in df.columns: # Ensure 'authorid' is the filter column
                    matching_rows = df[df['authorid'].isin(matched_ids_set)]
                    if not matching_rows.empty:
                        matching_dfs.append(matching_rows)
            except Exception: # pylint: disable=broad-except
                # print(f"Error reading indexed row group {rg_idx} in {parquet_path}: {e_idx_read}")
                continue # Skip this row group
        return pd.concat(matching_dfs, ignore_index=True) if matching_dfs else pd.DataFrame()

    except Exception as e:
        # print(f"Error in read_parquet_with_index for {parquet_path}: {e}. Falling back.")
        return read_parquet_optimized(parquet_path, columns, matched_ids_set) # Fallback

# Main function to load data using specified strategies
def load_parquet_with_strategies(
    parquet_path: str,
    matched_ids: list[str],
    columns_to_load: list[str],
    selected_strategy: str = "all",
    id_column_name: str = 'authorid'
) -> tuple[pd.DataFrame | None, str]:
    """
    Loads data from a Parquet file using one or all defined strategies and reports timing.

    Args:
        parquet_path: Path to the Parquet file.
        matched_ids: List of IDs to filter by.
        columns_to_load: List of columns to load from the Parquet file.
        selected_strategy: Name of the strategy to use, or "all" to run all.
        id_column_name: The name of the ID column in the parquet file (e.g. 'authorid').

    Returns:
        A tuple containing:
        - DataFrame: The data loaded by the selected strategy (or the first successful one if "all").
                   Returns None if all strategies fail or no data is found.
        - str: A report string detailing the timing for each executed strategy.
    """
    if not columns_to_load: # Ensure there's something to load
        return pd.DataFrame(), "No columns specified for loading.\n" # Return empty DataFrame

    if not os.path.exists(parquet_path):
        return pd.DataFrame(), f"Error: Parquet file not found at {parquet_path}\n" # Return empty DataFrame

    matched_ids_set = set(str(mid) for mid in matched_ids) if matched_ids else set()


    strategies = {
        "optimized_pyarrow": lambda: read_parquet_optimized(parquet_path, columns_to_load, matched_ids_set),
        "batched_read": lambda: read_parquet_batched(parquet_path, columns_to_load, matched_ids_set),
        "parallel_rowgroups": lambda: read_parquet_parallel_rowgroups(parquet_path, columns_to_load, matched_ids_set),
        "stats_filtering": lambda: read_parquet_with_stats_filtering(parquet_path, columns_to_load, matched_ids_set),
        "indexed_read": lambda: read_parquet_with_index(parquet_path, columns_to_load, matched_ids_set, id_column_name),
    }

    timing_report_parts = [f"--- Timing Report for {os.path.basename(parquet_path)} ---"]
    result_df = pd.DataFrame() # Initialize with an empty DataFrame
    
    strategies_to_run_names = []
    if selected_strategy == "all":
        strategies_to_run_names = list(strategies.keys())
    elif selected_strategy in strategies:
        strategies_to_run_names = [selected_strategy]
    else:
        timing_report_parts.append(f"Error: Strategy '{selected_strategy}' not found. Available: {', '.join(strategies.keys())}.")
        return pd.DataFrame(), "\n".join(timing_report_parts) + "\n"

    first_successful_df_taken = False
    for strategy_name in strategies_to_run_names:
        strategy_func = strategies[strategy_name]
        start_time = time.time()
        current_df = pd.DataFrame() # Default to empty DF for this iteration
        status = "failed"
        error_msg = ""
        try:
            current_df_candidate = strategy_func()
            duration = time.time() - start_time

            if current_df_candidate is None:
                # This case should ideally not happen if strategy functions always return DataFrames
                status = "returned None, treated as empty"
                current_df_candidate = pd.DataFrame() # Ensure it's a DataFrame
            elif not isinstance(current_df_candidate, pd.DataFrame):
                status = f"returned {type(current_df_candidate)}, forced to empty DataFrame"
                current_df_candidate = pd.DataFrame() # Ensure it's a DataFrame
            else:
                status = "succeeded"

            current_df = current_df_candidate # Assign valid DataFrame (even if empty)
            timing_report_parts.append(f"- Strategy '{strategy_name}': {duration:.4f} seconds ({status}, {len(current_df)} rows)")

            if selected_strategy != "all":
                result_df = current_df # If specific strategy, this is the one
                break # Exit loop after running the specific strategy
            elif not first_successful_df_taken: # For "all", take the first one that ran (even if empty)
                result_df = current_df
                first_successful_df_taken = True # And prefer non-empty ones later if this was empty

            # If running "all" and current_df is non-empty, and previous result_df was empty, prefer current_df
            if selected_strategy == "all" and not current_df.empty and (result_df.empty or not first_successful_df_taken) :
                 result_df = current_df
                 first_successful_df_taken = True


        except Exception as e: # pylint: disable=broad-except
            duration = time.time() - start_time
            error_msg = str(e)
            timing_report_parts.append(f"- Strategy '{strategy_name}': FAILED in {duration:.4f} seconds. Error: {error_msg}")
            # current_df remains an empty DataFrame as initialized for this iteration
            if selected_strategy != "all": # If specific strategy failed
                result_df = current_df # Which is an empty df
                break
            elif not first_successful_df_taken: # If this is the first strategy in "all" and it failed
                result_df = current_df # Keep the empty df
                first_successful_df_taken = True


    if not strategies_to_run_names:
         timing_report_parts.append("No valid strategies were specified to run.")
    elif selected_strategy == "all" and result_df.empty and first_successful_df_taken :
        timing_report_parts.append("All strategies resulted in empty DataFrames or failed.")
    elif selected_strategy != "all" and result_df.empty:
         timing_report_parts.append(f"Strategy '{selected_strategy}' resulted in an empty DataFrame or failed.")


    return result_df, "\n".join(timing_report_parts) + "\n"

# --- Utility for one-time index building for all relevant files ---
def build_indices_for_directory(directory_path, id_column_map=None):
    """
    Builds index files for all .parquet files in a given directory.
    id_column_map: Optional dict mapping filename (or prefix) to id_column name.
                   e.g., {'authors': 'authorid', 'author_details': 'authorid'}
    """
    if id_column_map is None:
        id_column_map = {}

    # print(f"Scanning {directory_path} for parquet files to index...")
    for filename in os.listdir(directory_path):
        if filename.endswith(".parquet") and not filename.endswith("_index.parquet"): # Avoid indexing index files
            parquet_file_path = os.path.join(directory_path, filename)

            id_column = 'authorid'
            matched_prefix = False
            for prefix, col_name in id_column_map.items():
                if filename.startswith(prefix):
                    id_column = col_name
                    matched_prefix = True
                    break
            if not matched_prefix and 'default' in id_column_map: # Fallback to a 'default' if provided
                 id_column = id_column_map['default']

            index_file_path = get_index_file_path(parquet_file_path, id_column)
            # print(f"Found {parquet_file_path}. Index will be {index_file_path} (id_col: {id_column}).")
            if os.path.exists(index_file_path):
                # print(f"Index {index_file_path} already exists. Skipping creation.")
                continue

            # print(f"Building index for {filename} with id_column '{id_column}'...")
            start_time = time.time()
            created_index_df = create_parquet_index(parquet_file_path, index_file_path, id_column)
            duration = time.time() - start_time
            if created_index_df is not None and not created_index_df.empty:
                # print(f"Successfully created index {index_file_path} in {duration:.2f}s.")
                pass
            else:
                # print(f"Index creation may have failed or yielded empty index for {parquet_file_path} (took {duration:.2f}s).")
                pass

# Example usage (can be run as a script to pre-build indices):
if __name__ == '__main__':
    print("Optimize Matching Speed - Utility Mode")
    
    dummy_data_dir = os.path.join(os.path.dirname(__file__), 'dummy_data')
    if not os.path.isdir(dummy_data_dir): # Check if directory exists
        print(f"Directory {dummy_data_dir} not found. Please ensure it exists and contains Parquet files.")
    else:
        print(f"\nBuilding indices for Parquet files in: {dummy_data_dir}")
        id_map = {
            'dummy_authors': 'authorid', # Filename starts with 'dummy_authors'
            'dummy_author_details': 'authorid', # Filename starts with 'dummy_author_details'
            'default': 'authorid' # Default for any other parquet file
        }
        build_indices_for_directory(dummy_data_dir, id_map)
        print("\nIndex building process finished for specified files.")

        print("\n--- Example: Running load_parquet_with_strategies ---")
        sample_authors_path = os.path.join(dummy_data_dir, "dummy_authors.parquet")
        if not os.path.exists(sample_authors_path):
            print(f"Skipping example run: {sample_authors_path} not found.")
        else:
            print(f"Testing with {sample_authors_path}")
            # Assuming authorid in dummy_authors.parquet are strings like 'A1', 'A2'
            # If they are integers, matched_ids should be list of ints.
            # The load_parquet_with_strategies converts matched_ids to strings internally.
            example_matched_ids = ['A1', 'A2', 'A100', 'NonExistentID']
            example_cols = ['authorid', 'display_name', 'h_index']

            df_all, report_all = load_parquet_with_strategies(
                sample_authors_path, example_matched_ids, example_cols, selected_strategy="all"
            )
            print("\nReport for 'all' strategies:")
            print(report_all)
            if df_all is not None:
                print(f"DataFrame returned from 'all' ({len(df_all)} rows):")
                # print(df_all.head())
            else: # Should not happen as it defaults to empty DataFrame
                print("No DataFrame returned from 'all' strategies (should be an empty DataFrame).")

            print("\n----------------------------------")
            print("Test with 'indexed_read' strategy:")
            # Ensure index exists: dummy_data/dummy_authors_authorid_index.parquet
            df_indexed, report_indexed = load_parquet_with_strategies(
                sample_authors_path, example_matched_ids, example_cols, selected_strategy="indexed_read"
            )
            print("\nReport for 'indexed_read' strategy:")
            print(report_indexed)
            if df_indexed is not None:
                print(f"DataFrame returned by 'indexed_read' ({len(df_indexed)} rows):")
                # print(df_indexed.head())
            else: # Should not happen
                print("No DataFrame returned from 'indexed_read'.")

        print("\n--- Example Run Finished ---")
    print("\nTo use in your main script: from optimize_matching_speed import load_parquet_with_strategies")
