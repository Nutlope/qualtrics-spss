# https://www.youtube.com/watch?v=5GzVNi0oTxQ&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=37&ab_channel=sentdex

import urllib.request
# The urllib module in Python 3 allows you access websites via your program. This opens up as many doors for your programs as the internet opens up for you. urllib in Python 3 is slightly different than urllib2 in Python 2, but they are mostly the same. Through urllib, you can access websites, download data, parse data, modify your headers, and do any GET and POST requests you might need to do.

# GET

# x = urllib.request.urlopen('https://www.google.com')  (This is a GET)
# print(x.read())

# # POST

# import urllib.parse

# url = 'http://pythonprogramming.net'
# values = {'s': 'basic',
#           'submit': 'search'}
# # encode 'values' as the data we want to POST in
# data = urllib.parse.urlencode(values)
# # put data in bytes, a type of encoding
# data = data.encode('utf-8')
# # we are requesting the url & data we want to pass through
# req = urllib.request.Request(url, data)
# # we are visiting the url right now here
# resp = urllib.request.urlopen(req)
# # read the results
# respData = resp.read()
# # Python is looking at the source of the web page and displys it
# print(respData)

# try & accept

# try:
#     # we will attempt to vist this url. This is a search request in google with the word 'test'
#     x = urllib.request.urlopen('https://www.google.com/search?q=test')
#     # read the source code of the search results
#     print(x.read())
#     # otherwise we will through the exception as e and print it
# except Exception as e:
#     print(str(e))


try:
    url = urllib.request.urlopen('https://www.google.com/search?q=test')
    # headers are the data you are sending (who you are? including the users agents)
    headers = {}
    # This tells google that we are no longer announcing ourselves as Python- we are replacing our user-agent and fooling google
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'

    # we are defining the request --- the function Request has default parameters (default value for headers)
    req = urllib.request.Request(url, headers=headers)
    #
    resp = urllib.request.urlopen(req)
    respData = resp.read()  # this response data is huge as it is a google search

    # open the file with the intention to write -- CREATE A FILE WITHhEADERS.TXT
    saveFile = open('withHeaders.txt', 'w')
    # sincerespData is not in a string format, we need to convert it
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))  # just in case
