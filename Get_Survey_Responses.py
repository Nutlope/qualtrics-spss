import requests
import zipfile
import json
import io
import os
import sys
import re
import csv
import constants

# Create a dictionary with data from surveys.csv (user_generated_name, survey_name, survey_qualtrics_id)
with open('surveys.csv', 'r') as f:
    reader = csv.reader(f)
    surveys_dict = {}
    next(f) # skip header line

    for row in reader:
        surveys_dict[row[0]] = {'state_survey_name': row[1],'survey_qualtrics_id': row[2]}

def exportSurvey(apiToken, surveyId, dataCenter, fileFormat):

    # Setting static parameters
    requestCheckProgress = 0.0
    progressStatus = "inProgress"
    baseUrl = "https://{}.qualtrics.com/API/v3/surveys/{}/export-responses/".format(dataCenter, surveyId)
    headers = {"content-type": "application/json","x-api-token": apiToken}

    # Step 1: Creating Data Export - POST request to qualtrics to send data
    downloadRequestPayload = '{"format":"' + fileFormat + '"}'
    downloadRequestResponse = requests.request("POST", baseUrl, data=downloadRequestPayload, headers=headers)
    progressId = downloadRequestResponse.json()["result"]["progressId"]

    # Step 2: Checking on Data Export Progress and waiting until export is ready - GET request to qualtrics to get data
    while progressStatus != "complete" and progressStatus != "failed":
        # The result object will contain a status value. Keep looping until status has the value complete.
        requestCheckUrl = baseUrl + progressId
        requestCheckResponse = requests.request("GET", requestCheckUrl, headers=headers)
        requestCheckProgress = requestCheckResponse.json()["result"]["percentComplete"]
        progressStatus = requestCheckResponse.json()["result"]["status"]

    # step 2.1: Check for errors
    if progressStatus == "failed":
        raise Exception("Sorry! the export failed")

    # step 2.2: Get the file id
    # Once the export is complete, use the fileId field in the result object from Get Response Export Progress
    fileId = requestCheckResponse.json()["result"]["fileId"]

    # Step 3: Downloading file
    requestDownloadUrl = baseUrl + fileId + '/file'
    requestDownload = requests.request("GET", requestDownloadUrl, headers=headers, stream=True)

    # Step 4: Unzipping the file
    zipfile.ZipFile(io.BytesIO(requestDownload.content)).extractall("./SPSS_Surveys")
    print('Complete\n')

def main():
    for key, value in surveys_dict.items():
        surveyId = value['survey_qualtrics_id']
        fileFormat = constants.fileFormat
        dataCenter = constants.dataCenter
        apiToken = constants.apiToken

        # Error handling
        if fileFormat not in ["csv", "tsv", "spss"]:
            print('fileFormat must be either csv, tsv, or spss')
            sys.exit(2)
        r = re.compile('^SV_.*')
        m = r.match(surveyId)
        if not m:
            print("survey Id must match ^SV_.*")
            sys.exit(2)

        exportSurvey(apiToken, surveyId, dataCenter, fileFormat)

if __name__ == "__main__":
    main()