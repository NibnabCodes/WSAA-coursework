# This program converts a web page to a pdf 
# to demonstrate API Keys
# Author: Niamh Hogan

import requests
import urllib.parse
from config import apikeys as cfg

targetUrl = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html" 
 
apikey = cfg["htmltopdfkey"]
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targetUrl,'apiKey': apikey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("lab4document.pdf", "wb") as handler:
    handler.write(result) 