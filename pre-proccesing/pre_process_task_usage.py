import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "./../Data/task_usage_combined.csv"  # part-01_task_usage.csv
df = pd.read_csv(file_path)

colnames = [
    "start_time_measurement",               # 1. start time of the measurement period
    "end_time_measurement",                 # 2. end time of the measurement period
    "job_ID",                               # 3. job ID
    "task_index",                           # 4. task index
    "machine_ID",                           # 5. machine ID
    "mean_CPU_usage_rate",                  # 6. mean CPU usage rate
    "canonical_memory_usage",               # 7. canonical memory usage
    "assigned_memory_usage",                # 8. assigned memory usage
    "unmapped_page_cache_memory_usage",     # 9. unmapped page cache memory usage
    "total_page_cache_memory_usage",        # 10. total page cache memory usage
    "maximum_memory_usage",                 # 11. maximum memory usage
    "mean_disk_IO_time",                    # 12. mean disk I/O time
    "mean_local_disk_space_used",           # 13. mean local disk space used
    "maximum_CPU_usage",                    # 14. maximum CPU usage
    "maximum_disk_IO_time",                 # 15. maximum disk IO time
    "cycles_per_instruction_CPI",           # 16. cycles per instruction (CPI)
    "memory_accesses_per_instruction_MAI",  # 17. memory accesses per instruction (MAI)
    "sample_portion",                       # 18. sample portion
    "aggregation_type",                     # 19. aggregation type (1 if maximums from subcontainers were summed)
    "sampled_CPU_usage_mean"                # 20. sampled CPU usage: mean CPU usage during a sample period
]

# Assign the new column names to the DataFrame
df.columns = colnames

#Manually select the columns that you want to process
selected_columns = [
    'task_index', 'mean_CPU_usage_rate', 'canonical_memory_usage', 'assigned_memory_usage', 
    'unmapped_page_cache_memory_usage', 'total_page_cache_memory_usage', 'maximum_memory_usage', 
    'mean_disk_IO_time', 'mean_local_disk_space_used', 'maximum_CPU_usage', 
    'maximum_disk_IO_time', 'cycles_per_instruction_CPI', 'memory_accesses_per_instruction_MAI', 
    'sampled_CPU_usage_mean'
]

#Delete the entire line containing NaN
df.dropna(subset=selected_columns, inplace=True)

#Calculate IQR
Q1 = df[selected_columns].quantile(0.25)
Q3 = df[selected_columns].quantile(0.75)
IQR = Q3 - Q1

#Define an outlier range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

#Identify outliers
outliers = ((df[selected_columns] < lower_bound) | (df[selected_columns] > upper_bound))

#Calculate the number of outliers in each column
outlier_counts = outliers.sum()
#print("Number of outliers (per column)：\n", outlier_counts)

#Filter outliers (remove outlier rows)
df_cleaned = df[~outliers.any(axis=1)]

#Automatically detect all numeric columns
sci_columns = df.select_dtypes(include=[np.number]).columns
print(f"Columns of detected values: {sci_columns.tolist()}")

#Convert scientific notation to standard decimal format (actually only 6 decimal places are kept)
df[sci_columns] = df[sci_columns].applymap(lambda x: '{:.6f}'.format(x) if isinstance(x, float) else x)


if 'job_ID' in df.columns and 'task_index' in df.columns:
    #String splicing
    df['process_ID'] = df['job_ID'].astype(str) + "_" + df['task_index'].astype(str)
    
    #Save data
    output_path = "./task_usage_combined_cleaned.csv"
    df.to_csv(output_path, index=False)
    
    print(df[['job_ID', 'task_index', 'process_ID']].head())
else:
    print("The job_ID or task_index column is missing from the dataset")
