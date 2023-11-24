# Project Title
YouTube Data Analysis

# Short Description
This project involves analyzing YouTube channel data, extracting insights, and saving the top 1000 records to both a CSV file and a MySQL database

# Getting Started
Prerequisites: <br>
Install Python on your machine <br>
Required Python packages: pandas, sqlalchemy <br>
<br>
You can install the required packages using the following commands: <br>
pip install pandas <br>
pip install sqlalchemy <br>

# Running the Tests

1. Calculate Channel Type Distribution: <br>

Function: calculate_channel_type_distribution <br>
Purpose: To calculate the distribution of channel types in the dataset <br>
Output: Displays the distribution of channel types <br>

2. Save Top 1000 Records to CSV: <br>

Function: save_top_1000_to_csv <br>
Purpose: Saves the top 1000 records to a CSV file <br>
Output: Displays a message indicating the successful saving of records <br>

3. Save Top 1000 Records to Database: <br>

Function: save_top_1000_to_database <br>
Purpose: Saves the top 1000 records to a MySQL database table <br>
Output: Displays a message indicating the successful saving of records <br>

# Deployment
This project is primarily a data analysis script. <br>
To deploy it: <br>
Ensuring the necessary data file ('Youtube_Dataset.csv') in the specified location <br>
Install the required Python packages as mentioned in the "Installing" section <br>
Run the script, and it will perform the data analysis, save the top 1000 records to a CSV file ('top_1000_records.csv'), and also save them to a MySQL database table <br>

Note: Make sure to have a MySQL server running and adjust the database connection details in the script accordingly

