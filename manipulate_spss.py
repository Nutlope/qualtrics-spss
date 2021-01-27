import pyreadstat
import numpy as np
import os

directory = os.fsencode("./SPSS_Surveys")
populated = 0

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    fullFileName = "./SPSS_Surveys/" + fileName

    df, meta = pyreadstat.read_sav(fullFileName) # Read SPSS file and store in df (meta has extra info)

    # If the SPSS file is empty, delete it
    if df.empty:
        print("it's empty before")
        os.remove(fullFileName) # DELETE FILE
        continue

    # Specify date you want to start at
    dateFilter = '2021-01-01' 

    # Check which survey responses (SPSS rows) don't satisfy date condition and delete them
    df = df[df.EndDate > np.datetime64(dateFilter)]

    # Check if the dataframe is empty after we filter, if it is delete file
    if df.empty:
        print("it's empty after")
        os.remove(fullFileName) # DELETE FILE
        continue

    df.reset_index(level=0, drop=True, inplace=True) # Reset indices - Important
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