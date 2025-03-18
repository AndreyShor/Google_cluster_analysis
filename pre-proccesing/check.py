import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = "./../Data/task_usage_combined.csv" 
df = pd.read_csv(file_path)

print("Number of columns:", len(df.columns))