import pyreadstat
import numpy as np
import pandas as pd
import os

directory = os.fsencode("./SPSS_Surveys")

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    fullFileName = "./SPSS_Surveys/" + fileName

    df, meta = pyreadstat.read_sav(fullFileName) # Read SPSS file and store in df (meta has extra info)
    if not df.empty:
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
        print("it worked fam")
        pyreadstat.write_sav(df, fullFileName) # Write the new SPSS changes back to the same file