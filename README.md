# Qualtrics and SPSS script

This Python script can query Qualtrics for all surveys and extract them as SPSS or CSV files. A Scheme script was also generated to combine all SPSS files into one.

## Motivation

My mom had 50 surveys on Qualtrics that she used to manually go through each week and update a spreadsheet with responses. This took a few hours every week and was repetitive so I decided write a script that queried qualtrics for all the surveys she needed and generate a master excel file with all the data. She also wanted the data in a statistics software called SPSS to analyze it, so I ended up generating a Scheme script to create this document as well.

## How to Run
1. Make a surveys.csv file with the format of: id (user generated), survey_name, survey_qualtrics_id
2. Update constants.py with your Qualtrics API key and other things.
3. Run the Get_Survey_Responses.py with an excel file containing all the survey IDs in the 3rd column
4. An SPSS file will be generated for each survey as well as a Scheme script to combine these SPSS files
5. Run the Scheme script in SPSS to generate one final file.

## Dependencies
- requests
- zipfile
- json
- io
- os
- sys
- re
- csv

## Future work
- [x] Generate a Scheme script to combine all SPSS files into one
- [x] Refactor to 1 script with everything
- [ ] Generalize this generate a master excel file instead of just SPSS 
- [ ] Split into two scripts, one for excel and one for SPSS for ease of use

## Contact
If you have any questions or would like someone to modify this script for your specific scenario, feel free to reach out to me at hassan@hey.com