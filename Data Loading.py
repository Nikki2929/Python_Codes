#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import sqlite3


# In[6]:


df = pd.read_csv('Documents/Youtube_Dataset.csv')
df.head(10)


# In[59]:


def calculate_channel_type_distribution(df):
    channel_type_distribution = df['channeltype'].value_counts()
    return channel_type_distribution


# In[60]:


def save_top_1000_to_csv(df, output_csv_path):
    top_1000_records = df.head(1000)
    top_1000_records.to_csv(output_csv_path, index=False)
    print(f"Top 1000 records saved to {output_csv_path}")


# In[61]:


from sqlalchemy import create_engine

def save_top_1000_to_database(df, top_1000_channels, 'mysql+pymysql://root:Vani%402929@localhost:3306/data_1202'):
    engine = create_engine('mysql+pymysql://root:Vani%402929@localhost:3306/data_1202')
    top_1000_records = df.head(1000)
    top_1000_records.to_sql(top_1000_channels, conn, if_exists='replace', , index=False)
    print(f"Top 1000 records saved to the '{top_1000_channels}' table in the database.")


# In[79]:


channel_type_distribution = calculate_channel_type_distribution(df)
print("Channel Type Distribution for Top 1000 Records:")
print(channel_type_distribution)
save_top_1000_to_csv(df, 'top_1000_records.csv')
save_top_1000_to_database(df, 'top_1000_channels','mysql+pymysql://root:Vani%402929@localhost:3306/data_1202')


# In[ ]:




