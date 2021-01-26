import pyreadstat
import numpy as np

# Read SPSS file and store in df (meta contains some extra info)
df, meta = pyreadstat.read_sav("./SPSS_Surveys/CA.sav")

# Meta information
print(meta.column_names)
print(meta.column_labels)
print(meta.column_names_to_labels)
print(meta.number_rows)
print(meta.number_columns)
print(meta.file_label)

# How to access a row
print(df.iloc[0])
print(df.loc[0])

# Specify date you want to start at
dateFilter = '2021-01-01'

# Checking which survey responses (SPSS rows) satisfy date condition
for i in range(len(df)):
    if df['EndDate'][i] > np.datetime64(dateFilter):
        print(df.loc[i])
