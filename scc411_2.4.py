import pandas as pd

#Load dataset
file_path = "/Users/xuzhengyi/Desktop/scc 411/final_cleaned_data.csv"
df = pd.read_csv(file_path)

#Check whether jobID and taskID exist
if 'job_ID' in df.columns and 'task_index' in df.columns:
    #String splicing
    df['process_ID'] = df['job_ID'].astype(str) + "_" + df['task_index'].astype(str)
    
    #Save data
    output_path = "/Users/xuzhengyi/Desktop/scc 411/final_cleaned_data_with_processID.csv"
    df.to_csv(output_path, index=False)
    
    print(df[['job_ID', 'task_index', 'process_ID']].head())
else:
    print("The job_ID or task_index column is missing from the dataset")