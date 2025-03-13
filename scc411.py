import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "data_with_labels_small.csv"  
df = pd.read_csv(file_path)

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

#Output the number of rows of cleaned data
print(f"Number of rows of raw data: {df.shape[0]}, Number of data rows after clearing: {df_cleaned.shape[0]}")

'''
#Box plotting（Before and after comparison）
plt.figure(figsize=(12, 6))
df[selected_columns].boxplot(rot=45)
plt.title("Boxplot of Selected Metrics (Before Outlier Removal)")
plt.ylabel("Value Range")
plt.show()

plt.figure(figsize=(12, 6))
df_cleaned[selected_columns].boxplot(rot=45)
plt.title("Boxplot of Selected Metrics (After Outlier Removal)")
plt.ylabel("Value Range")
plt.show()
'''

cleaned_file_path = "/Users/xuzhengyi/Desktop/scc 411/cleaned_data.csv"
df_cleaned.to_csv(cleaned_file_path, index=False)

