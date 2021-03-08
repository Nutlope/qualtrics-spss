import pyreadstat
import numpy as np
import os
import json
import csv

directory = os.fsencode("./My_SPSS_Surveys")
populated = 0
emptyStates = []

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    fullFileName = "./My_SPSS_Surveys/" + fileName

    # Read SPSS file and store in df (meta has extra info)
    df, meta = pyreadstat.read_sav(fullFileName)

    # Read CSV file and create 3 arrays for each column
    with open('./new_columns.csv', 'r') as csv_file:
        f = csv.reader(csv_file)
        next(f)  # ignore header line

        firstRow = next(f)
        fieldName = [firstRow[0]]
        fieldKeep = [firstRow[1]]
        newFieldName = [firstRow[2]]

        for row in f:
            fieldName.append(row[0])
            fieldKeep.append(row[1])
            newFieldName.append(row[2])

    # If field says no, rename it to new name
    # for i in range(len(fieldKeep)):
    #     if fieldKeep[i] == "Yes":
    #         df = df.rename(columns={fieldName[i]: newFieldName[i]})
    #     else:
    #         df = df.drop(columns=fieldName[i])

    # Prints df Columns
    print(df.columns)

    meta.variable_value_labels['Statusomar'][1.0] = "Omar"
    print(meta.variable_value_labels['Statusomar'][1.0])

    # print(meta.column_names) # OR this one

    # Deletes column IP Address from the data frame
    # df = df.drop(columns="IPAddress")

    # Prints new df
    # print("This is new df", df)

    # Prints out IPAddress Column
    # print(df.loc[0]["IPAddress"])

    # Loops through columns and creates CSV with them
    # with open('columns.csv', 'w') as csv_file:
    #     for col in df.columns:
    #         csv_file.write(col + '\n')

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

# Prints empty states
# print("The states that did not respond yet are: ", emptyStates)

# Write master df to a json file
# json_file = dfMaster.to_json()
# print(json_file)
# with open("./finalFilteredSPSSjson.txt", 'w') as outfile:
#     json.dump(json_file, outfile)
