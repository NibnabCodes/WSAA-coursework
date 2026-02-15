# Author: Niamh Hogan

# This program retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json"

import requests

urlStart = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    url = urlStart + dataset + urlEnd
    response = requests.get(url)
    with open("cso.json", "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    getAllAsFile("FIQ02")