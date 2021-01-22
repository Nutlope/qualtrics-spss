# Qualtrics and SPSS script

This Python script can query Qualtrics for all surveys, extract them as SPSS files, and combine them with a Scheme script

## How to Run

1. Run the Get_Survey_Responses.py with an excel file containing all the survey IDs in the 3rd column
2. An SPSS file will be generated for each survey as well as a Scheme script to combine these SPSS files
3. Run the Scheme script in SPSS to generate one final file.

## Dependencies
- requests
- zipfile
- json
- io
- os
- sys
- re
- csv