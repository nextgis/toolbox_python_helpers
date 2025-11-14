# Simple tool run that sends a file over to Toolbox to run a tool
# https://toolbox.nextgis.com/t/kmldae2footprints

import requests

##############SET THESE#######################
token = "YOUR API TOKEN"
tool = "kmldae2footprints"
##############################################

headers = {"Authorization": "Token %s" % token}

filename = "sampledata.zip"
url = "https://toolbox.nextgis.com/api/upload/?format=json&filename=" + filename
files = {}
file = open(filename, "rb")
response = requests.post(url, data=file, headers=headers, verify=False)
files["zip_with_kmls"] = "storage/" + response.json()["local"]["uuid"]

json_request = {"tool": tool, "inputs": {}}
json_request["inputs"]["zip_with_kmls"] = files["zip_with_kmls"]

url = "https://toolbox.nextgis.com/api/tasks/"
response = requests.post(url, json=json_request, headers=headers)
print(response.text)
