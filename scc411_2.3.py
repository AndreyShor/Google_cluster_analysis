import numpy as np
import pandas as pd

#Loac dataset
file_path = "/Users/xuzhengyi/Desktop/scc 411/cleaned_data.csv"
df = pd.read_csv(file_path)

#Automatically detect all numeric columns
sci_columns = df.select_dtypes(include=[np.number]).columns
print(f"Columns of detected values: {sci_columns.tolist()}")

#Convert scientific notation to standard decimal format (actually only 6 decimal places are kept)
df[sci_columns] = df[sci_columns].applymap(lambda x: '{:.6f}'.format(x) if isinstance(x, float) else x)

#Save the converted data
converted_file_path = "/Users/xuzhengyi/Desktop/scc 411/final_cleaned_data.csv"
df.to_csv(converted_file_path, index=False)

print(df[sci_columns].head())