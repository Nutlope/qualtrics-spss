# 1: import the pyreadstat package
import pyreadstat
import pandas as pd

# # 2 use read_sav to read SPSS file:
# # In the code chunk below we create two variables; df, and meta. As can be seen, when using type df is a Pandas dataframe:
# df, meta = pyreadstat.read_sav(
#     'C:/MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - NJ.sav')

# type(df)

# # Thus, we can use all methods available for Pandas dataframe objects. In the next line of code, we are going to print the 5 first rows of the dataframe using pandas head method.

# df.head()

# Pandas

df = pd.read_spss(
    'C: \MyNewQualtricsDownload\STATE LEADER SURVEY_ Supporting Immigrant Families(2020-2021) - NJ.sav')
df.tail()
