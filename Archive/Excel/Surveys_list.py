# Get Survey API

import os
import requests

# Setting user Parameters
apiToken = os.environ["Q_API_TOKEN"]     # 1
dataCenter = os.environ["Q_DATA_CENTER"]  # 2

surveyId = "YOUR SURVEY ID"    # 3


baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}".format(
    dataCenter, surveyId)
headers = {
    "x-api-token": apiToken,
}

response = requests.get(baseUrl, headers=headers)
print(response.text)
