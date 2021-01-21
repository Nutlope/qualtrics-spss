import csv

# Load the csv file to a dictionary
# open the file 'surveys.csv  for reading its content and assign it to f
with open('surveys.csv', 'r') as f:
    reader = csv.reader(f)
    surveys_dict = {}
    next(f)
    # state_id, state_survey_name, state_survey_id

    for row in reader:
        surveys_dict[row[0]] = {'state_survey_name': row[1],
                                'state_survey_id': row[2]}

emptyStates = ['AK', 'AL', 'CT', 'GA', 'ID', 'IN', 'MI',
               'MO', 'NE', 'NY', 'OK', 'SC', 'SD', 'VT', 'WV']
i = 1
for key, value in surveys_dict.items():
    if key not in emptyStates:
        print("GET")
        print('  /FILE="C:\\MyNewQualtricsDownload\\STATE LEADER SURVEY_ Supporting Immigrant Families (2020-2021) - {}.sav".'.format(key))
        print("DATASET NAME DataSet{}.".format(i))
        print('\n')
        i += 1

print("DATASET ACTIVATE DataSet1.")
print("ADD FILES /FILE=*")
j = 2
while j < 51 - len(emptyStates):
    print("  /FILE=DataSet{}".format(j))
    j += 1

print("EXECUTE.")
