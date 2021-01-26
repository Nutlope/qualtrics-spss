import pyreadstat
import numpy as np
import pandas as pd

# Read SPSS file and store in df (meta contains some more info)
df, meta = pyreadstat.read_sav("./SPSS_Surveys/CA.sav")

# Specify date you want to start at
dateFilter = '2021-01-01'

# Problem was the dataframe needs to get reset after manipulation. 
# for i in range(len(df)):
#     if df['EndDate'][i] < np.datetime64(dateFilter):
#         df.drop(index=i, inplace=True)

# Checking which survey responses (SPSS rows) don't satisfy date condition and delete the rows. 
df = df[df.EndDate > np.datetime64(dateFilter)] # Syntactic sugar instead of the for loop
df.reset_index(level=0, drop=True, inplace=True) # Reset indices

print("Old DF:")
print(df)
pyreadstat.write_sav(df, "./SPSS_Surveys/CA.sav")

new_df, new_meta = pyreadstat.read_sav("./SPSS_Surveys/CA.sav")
print("New DF:")
print(new_df)

# RESOURCES
# Pyreadstat docs - https://github.com/Roche/pyreadstat
# Pandas Dataframe tutorials - https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question2
# https://note.nkmk.me/en/python-pandas-drop/
# https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/