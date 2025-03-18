import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#loac data 
file_path = "part-01_job_events.csv"
df = pd.read_csv(file_path)

#Delete useless column
df.drop(columns=['missing information'], inplace=True)  #All values in this column are NA and do not need to be reserved

#Automatically detects string columns
string_columns = df.select_dtypes(include=['object']).columns.tolist()
print("A detected column containing a hash value：", string_columns)

#Create LabelEncoder and convert
label_encoders = {}  
for col in string_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])  #Encoder
    label_encoders[col] = le  

#Save the converted data
converted_file_path = "/Users/xuzhengyi/Desktop/scc 411/converted_data.csv"
df.to_csv(converted_file_path, index=False)

print(df.head())