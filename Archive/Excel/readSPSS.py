import savReaderWriter
import pandas as pd
import pyreadstat
import os
import numpy as np

# dataframes = []
# i = 0
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         # print(os.path.join(root, name))
#         df = pd.read_spss(name)
#         dataframes.append(df)
#         i += 1
#         print(i)
# print(dataframes)

######
dataframes = []
i = 0
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        while i != 1:
            i += 1
            print(i)
            # print(name)
            # print(os.path.join(root, name))
            df = pd.read_spss(name)
            print(type(df))
            pyreadstat.write_sav(df, './all_spss.sav')
            # dataframes.append(df)


#####


######

# # You could access the data using something like:
# reader = savReaderWriter.SavReader("spss_demo.sav")
# all_data = reader.all()
# print all_data
# variable_names = reader.varNames
# print variable_names
# reader.close()

# ######


# mc_all = pd.DataFrame({'col_1': [0, 1, 1, 2],
#                        'col_2': ['france', 'france', 'uk', 'uk']})
# savFileName = 'mc_all.sav'
# args = (['col_1', 'col_2'], dict(col_1=0, col_2=0))
# array = mc_all.values
# with savReaderWriter(savFileName, *args) as writer:
#     writer.writerows(array)


# # This is our pseudocode
# # 1. open new spss file


# # dataframes = []
# # for file in os.walk('C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload'):
# #     # for f in files:
# #     df = pd.read_spss(file)
# #     dataframes.append(df)
# # print[dataframes]


# # for file in os.walk("c:/Users/Home/Documents/Omar/Python/Excel/"):
# #     # for f in files:
# #     df = pd.read_spss(file)
# #     # df, meta = pyreadstat.read_sav(file)
# #     # type(df)
# #     dataframes.append(df)
# # # print[dataframes]
