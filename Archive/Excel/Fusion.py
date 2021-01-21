import glob
import spss

import savReaderWriter
import pandas as pd
import pyreadstat
import os
import numpy as np

dataframes = []
i = 0
cmd = ["MATCH FILES"]

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
        cmd.append("""/FILE="%s" """ % name)
# spss.Submit(cmd)

        i += 1
        print(i)


# begin program.

# cmd = ["MATCH FILES"]
# # C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload

# # for f in glob.glob(r"C:\Users\Home\Documents\Omar\Python\Excel\MyNewQualtricsDownload\*.sav"):
# #     cmd.append("""/FILE="%s" """ % f)
# # # spss.Submit(cmd)
# # end program.
