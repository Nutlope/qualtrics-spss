import Qualtrics

apiToken = os.environ["1IoQvw8DhEzm3HdKNQoqSC90iSoIEIDqohoFWFA0"]
dataCenter = os.environ["iad1"]

qualtrics = Qualtrics(apiToken, dataCenter)

qualtrics.download_all_responses()
