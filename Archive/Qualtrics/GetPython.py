import json
import urllib.request  # default module for Python 3.X

url = 'https://i1d1.qualtrics.com/API/v3/whoami'
specific_url = 'https://iad1.qualtrics.com/API/v3/surveys/SV_6DLkFs2V8RJnTpj/responses/R_bsEazZ65x3fKIsp'

# specific_url = 'https://iad1.qualtrics.com/API/v3/surveys/SV_6DLkFs2V8RJnTpj/export-responses/'

header = {'X-API-TOKEN': '1IoQvw8DhEzm3HdKNQoqSC90iSoIEIDqohoFWFA0'}

# generating the request object
req = urllib.request.Request(specific_url, None, header)

handler = urllib.request.urlopen(req)  # running the request object

print(handler.status)  # print status code
print(handler.reason)  # prints error message
data = handler.read()  # reads in all the data

# print(data)

encoding = handler.info().get_content_charset(
    'utf-8')  # turns binary data into string
# turns string into a dictionary
dictionary = json.loads(data.decode(encoding))
# print(dictionary)
print(dictionary['result']['responseId'])


# prints dictionary in JSON FILE
with open("q3ual_result.json", "w") as outfile:
    json.dump(dictionary, outfile)

# print(dictionary)  -- how can we print an object in mutiple lines ?
requestId = dictionary["meta"]["requestId"]
# print(requestId)
