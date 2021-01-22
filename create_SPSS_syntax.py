import csv

# Load the csv file to a dictionary
# open the file 'surveys.csv  for reading its content and assign it to f
with open('surveys.csv', 'r') as f:
    reader = csv.reader(f)
    surveys_dict = {}
    next(f)
    # Structure of cvs: state_id, state_survey_name, state_survey_id

    for row in reader:
        surveys_dict[row[0]] = {'state_survey_name': row[1],
                                'state_survey_id': row[2]}

# Put states here that are empty
emptyStates = ['AK', 'AL', 'CT', 'GA', 'ID', 'IN', 'MI',
               'MO', 'NE', 'NY', 'OK', 'SC', 'SD', 'VT', 'WV']
i = 1

# Filepath to the folder with all SPSS files
filePath = "C:\\Users\\Home\\Desktop\\Coding\\Qualtrics_SPSS_Surveys\\SPSS_Surveys"
outputFile = open('FinalSyntax.sps','w')

for key, value in surveys_dict.items():
    if key not in emptyStates:
        outputFile.write('GET\n')
        outputFile.write('  /FILE="{}\\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - {}.sav".\n'.format(filePath, key))
        outputFile.write("DATASET NAME DataSet{}.\n".format(i))
        outputFile.write('\n')
        i += 1

outputFile.write("DATASET ACTIVATE DataSet1.\n")
outputFile.write("ADD FILES /FILE=*\n")

j = 2

while j < 51 - len(emptyStates):
    if j == 50 - len(emptyStates):
        outputFile.write("  /FILE=DataSet{}.\n".format(j))
        break
    outputFile.write("  /FILE=DataSet{}\n".format(j))
    j += 1

outputFile.write("EXECUTE.\n")

f.close()
