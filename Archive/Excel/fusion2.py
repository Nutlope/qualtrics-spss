# Step 1: Import packages and set the working directory

import os
import glob
import pandas as pd
os.chdir("C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload")

# Step 2: Use glob to match the pattern ‘sav'
extension = 'sav'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Step 3: Combine all files in the list and export as SAV

# combine all files in the list
combined_sav = pd.concat([pd.read_sav(f) for f in all_filenames])
# export to sav
combined_sav.to_sav("combined_sav.sav", index=False, encoding='utf-8-sig')
