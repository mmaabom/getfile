# Read File
import pandas as pd
file = pd.read_csv("Class List-convert.txt")
col = []
# Get Column Data
for cols in file.columns:
    col.append(cols)
# sort Columns
# covert to csv
file.to_csv("NewFile/final_output.csv", index=False)
