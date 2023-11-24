import pandas as pd
import sqlite3
df = pd.read_csv('Documents/Youtube_Dataset.csv')
df.head(10)

def calculate_channel_type_distribution(df):
    channel_type_distribution = df['channeltype'].value_counts()
    return channel_type_distribution
    
def save_top_1000_to_csv(df, output_csv_path):
    top_1000_records = df.head(1000)
    top_1000_records.to_csv(output_csv_path, index=False)
    print(f"Top 1000 records saved to {output_csv_path}")
from sqlalchemy import create_engine

def save_top_1000_to_database(df, top_1000_channels, 'mysql+pymysql://root:Password@localhost:3306/data_1202'):
    engine = create_engine('mysql+pymysql://root:Password@localhost:3306/data_1202')
    top_1000_records = df.head(1000)
    top_1000_records.to_sql(top_1000_channels, conn, if_exists='replace', , index=False)
    print(f"Top 1000 records saved to the '{top_1000_channels}' table in the database.")


channel_type_distribution = calculate_channel_type_distribution(df)
print("Channel Type Distribution for Top 1000 Records:")
print(channel_type_distribution)
save_top_1000_to_csv(df, 'top_1000_records.csv')
save_top_1000_to_database(df, 'top_1000_channels','mysql+pymysql://root:Password@localhost:3306/data_1202')




