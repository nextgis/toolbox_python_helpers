# Simple tool run that sends a file over to Toolbox to run a tool
# https://toolbox.nextgis.com/t/kmldae2footprints

import requests

##############SET THESE#######################
token = 'YOUR API TOKEN'
operation = 'kmldae2footprints'
##############################################

headers = {"Authorization": "Token %s" % token}

url = 'https://toolbox.nextgis.com/api/upload/'
files = {}
file = open('sampledata.zip', 'rb')
response = requests.post(url, data=file, headers=headers, verify=False)
files['zip_with_kmls'] = response.text

json_request = {'operation': operation, 'inputs': {}}
json_request['inputs']['zip_with_kmls'] = files['zip_with_kmls']

url = 'https://toolbox.nextgis.com/api/json/execute/'
response = requests.post(url, json=json_request, headers=headers, verify=False)
print(response.text)
