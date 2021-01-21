import requests
import zipfile
import json
import io
import os
import sys
import re
import csv

# Load the csv file (which contains the list of all survey IDs, along with State name & stae survey name) to a dictionary
# open the file 'surveys.csv  for reading its content and assign it to f
with open('surveys.csv', 'r') as f:
    reader = csv.reader(f)
    surveys_dict = {}
    next(f)
    # state_id, state_survey_name, state_survey_id

    for row in reader:
        surveys_dict[row[0]] = {'state_survey_name': row[1],
                                'state_survey_id': row[2]}
# the dictionary is now ready


def exportSurvey(apiToken, surveyId, dataCenter, fileFormat):

    # Setting static parameters
    requestCheckProgress = 0.0
    progressStatus = "inProgress"
    baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}/export-responses/".format(
        dataCenter, surveyId)

    headers = {
        "content-type": "application/json",
        "x-api-token": apiToken,
    }

    # Step 1: Creating Data Export
    downloadRequestUrl = baseUrl
    downloadRequestPayload = '{"format":"' + fileFormat + '"}'
    downloadRequestResponse = requests.request(
        "POST", downloadRequestUrl, data=downloadRequestPayload, headers=headers)
    progressId = downloadRequestResponse.json()["result"]["progressId"]
    print(downloadRequestResponse.text)

    # Step 2: Checking on Data Export Progress and waiting until export is ready
    while progressStatus != "complete" and progressStatus != "failed":
        # The result object will contain a status value. Keep looping until status has the value complete.

        print("progressStatus=", progressStatus)
        requestCheckUrl = baseUrl + progressId
        requestCheckResponse = requests.request(
            "GET", requestCheckUrl, headers=headers)
        requestCheckProgress = requestCheckResponse.json()[
            "result"]["percentComplete"]
        print("Download is " + str(requestCheckProgress) + " complete")
        progressStatus = requestCheckResponse.json()["result"]["status"]

    # step 2.1: Check for errors
    if progressStatus == "failed":
        raise Exception("Sorry! the export failed")

    # step 2.2: Get the file id
    # Once the export is complete, use the fileId field in the result object from Get Response Export Progress

    fileId = requestCheckResponse.json()["result"]["fileId"]
    print(fileId)

    # Step 3: Downloading file
    requestDownloadUrl = baseUrl + fileId + '/file'
    requestDownload = requests.request(
        "GET", requestDownloadUrl, headers=headers, stream=True)

    # Step 4: Unzipping the file
    zipfile.ZipFile(io.BytesIO(requestDownload.content)
                    ).extractall("./SPSS_Surveys")
    print('Complete\n')


def main():

    for key, value in surveys_dict.items():
        surveyId = value['state_survey_id']
        fileFormat = "spss"
        dataCenter = "iad1"
        apiToken = "1IoQvw8DhEzm3HdKNQoqSC90iSoIEIDqohoFWFA0"

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
