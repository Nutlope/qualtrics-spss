import pyreadstat
import numpy as np
import os
import json
import csv

# Read SPSS file and store in df (meta has extra info)
df, meta = pyreadstat.read_sav("./GoodSPSS.sav")

print(df.info())
