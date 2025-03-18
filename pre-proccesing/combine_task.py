import pandas as pd
import glob

# Use glob to get a list of all CSV files in the directory
csv_files = glob.glob("./../Data/task_event/*.csv")

# Read and store each CSV file in a list
dataframes = [pd.read_csv(file) for file in csv_files]

# Concatenate all DataFrames along rows
combined_df = pd.concat(dataframes, ignore_index=True)

combined_df.to_csv("./../Data/task_event/task_event_combined.csv", index=False)

print("Combined file saved as combined_file.csv")