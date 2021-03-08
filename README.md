# Qualtrics script

This Python script can query Qualtrics for all surveys and extract them all into a single SPSS file. It can also filter based on any column values.

## Motivation

My mom had 50 surveys on Qualtrics that she needed to manually go through each week and update a spreadsheet with responses. This took ~5 hours every week for 10 months and was repetitive so I decided write a script that queried qualtrics for all the surveys she needed. Using the pyreadstat module, I was also able to filter responses to only those in a certain time period and store all the results in a single SPSS file for my mom to analyze.

## How to Run
1. Make a surveys.csv file with the format of: id (user generated), survey_name, survey_qualtrics_id
2. Update constants.py with your Qualtrics API key, dataCenter, and file format.
3. Run Get_Survey_Responses.py (make sure surveys.csv contains survey IDs in 3rd column).
4. A new folder will be created with an SPSS file for each survey. 
5. Run manipulate_spss.py to combine all SPSS files into one master SPSS file with any specific filters (example shown for date filtering)

## Dependencies
- pyreadstat
- numpy
- requests
- zipfile

## Contact
If you have any questions or would like someone to modify this script for your specific scenario, feel free to reach out to me at hassan@hey.com
