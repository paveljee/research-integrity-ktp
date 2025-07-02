#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
authors = os.getenv('AUTHORS_PARQUET_PATH')
author_details = os.getenv('AUTHOR_DETAILS_PARQUET_PATH')
dummy_authors = 'dummy_data/dummy_authors.parquet'
dummy_author_details = 'dummy_data/dummy_author_details.parquet'


# In[ ]:


import pyarrow.parquet as pq

def print_authors_schemas(pq_real, pq_dummy):
    columns = pq.ParquetFile(pq_real).schema_arrow
    print(columns)
    dummy_columns = pq.ParquetFile(pq_dummy).schema_arrow
    print("\ndummy:", dummy_columns, sep="\n")
print_authors_schemas(authors, dummy_authors)


# In[ ]:


# inference sources have a different name.
# check what's going on in dummy table
dummy_pf = pq.ParquetFile(dummy_authors)
dummy_batch = dummy_pf.read_row_groups([0])
print(dummy_batch)


# In[ ]:


# check actual table
pf = pq.ParquetFile(authors)
batch = pf.read_row_groups([0])
print(batch)


# In[21]:


# replace list column with random numbers
import pyarrow.compute as pc
import pyarrow as pa
import numpy as np
n = dummy_batch.num_rows
random_ints = pa.array(np.random.randint(0, 2**63, size=n, dtype=np.int64))
dummy_batch = dummy_batch.remove_column(dummy_batch.schema.get_field_index('inference_sources'))
dummy_batch = dummy_batch.append_column('inference_sources', random_ints)
print(dummy_batch)


# In[ ]:


# save updated parquet
pq.write_table(dummy_batch, dummy_authors)
print_authors_schemas(authors, dummy_authors)


# In[32]:


print_authors_schemas(author_details, dummy_author_details)


# In[36]:


# replace list column with random string
dummy_ad_pf = pq.ParquetFile(dummy_author_details)
dummy_ad_batch = dummy_ad_pf.read_row_groups([0])
n = dummy_ad_batch.num_rows
str_array = pa.array(['dummy display name alternative'] * n, type=pa.string())
dummy_ad_batch = dummy_ad_batch.remove_column(dummy_ad_batch.schema.get_field_index('display_name_alternatives'))
dummy_ad_batch = dummy_ad_batch.append_column('display_name_alternatives', str_array)
print(dummy_ad_batch)


# In[37]:


# save updated parquet
pq.write_table(dummy_ad_batch, dummy_author_details)


# In[38]:


pf = pq.ParquetFile(authors)
batch = pf.read_row_groups([0], columns=['authorid', 'display_name'])
df = batch.to_pandas().head(10)
print(df)


# In[5]:


get_ipython().run_cell_magic('script', 'echo skip', "pf = pq.ParquetFile(author_details)\nbatch = pf.read_row_groups([0], columns=['authorid', 'display_name'])\ndf = batch.to_pandas().head(10)\nprint(df)\n")

