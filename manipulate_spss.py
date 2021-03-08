import pyreadstat
import numpy as np
import os
import json

directory = os.fsencode("./SPSS_Surveys")
populated = 0
emptyStates = []

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    fullFileName = "./SPSS_Surveys/" + fileName

    # Read SPSS file and store in df (meta has extra info)
    df, meta = pyreadstat.read_sav(fullFileName)

    # Deletes column IP Address from the data frame
    # df = df.drop(columns="IPAddress")

    # Prints new df without IPAddress column
    # print("This is new df", df)

    # Prints df Columns
    print(df.columns)

    with open('columns.csv', 'w') as csv_file:
        for col in df.columns:
            csv_file.write(col + '\n')

    # Prints out IPAddress Column
    # print(df.loc[0]["IPAddress"])

    # If the SPSS file is empty, delete it
    if df.empty:
        print("it's empty before")
        emptyStates.append(fullFileName[-6:-4])
        os.remove(fullFileName)  # DELETE FILE
        continue

    # Specify date you want to start at
    dateFilter = '2019-01-20'

    # How to access a row
    # print(df.iloc[0])
    # print(df.loc[0])

    # FOR LOOP OLD VERSION: Checking which survey responses (SPSS rows) satisfy date condition
    # for i in range(len(df)):
    #     if df['EndDate'][i] > np.datetime64(dateFilter):
    #         print(df.loc[i])

    # Check which survey responses (SPSS rows) don't satisfy date condition and delete them
    df = df[df.EndDate > np.datetime64(dateFilter)]

    # Check if the dataframe is empty after we filter, if it is delete file
    if df.empty:
        print("it's empty after")
        emptyStates.append(fullFileName[-6:-4])
        os.remove(fullFileName)  # DELETE FILE
        continue

    # Reset indices - Important
    df.reset_index(level=0, drop=True, inplace=True)
    print("it worked")

    # Append each to a master dataframe
    if populated == 1:
        dfMaster = dfMaster.append(df, ignore_index=True)
    if populated == 0:
        dfMaster = df
        populated = 1

    # Write the new SPSS changes back to the same file
    pyreadstat.write_sav(df, fullFileName)

# Write master df to a final SPSS file
pyreadstat.write_sav(dfMaster, "./finalFilteredSPSS.sav")

# Write master df to a json file
json_file = dfMaster.to_json()
print(json_file)
with open("./finalFilteredSPSSjson.txt", 'w') as outfile:
    json.dump(json_file, outfile)


# print("The states that did not respond yet are: ", emptyStates)
