# Simplest Toolbox API run without using SDK for https://toolbox.nextgis.com/t/hello

import requests
import time
import sys

##############SET THESE#######################
token = "YOUR API TOKEN"
tool_name = "hello"
name = "John"
##############################################

headers = {"Authorization": "Token %s" % token}
json_request = {"operation": tool_name, "inputs": {}}
json_request["inputs"]["name"] = name
json_request["inputs"]["sleep"] = ""  # empty string if no sleeping
url = "https://toolbox.nextgis.com/api/json/execute/"

# Run tool
response = requests.post(url, json=json_request, headers=headers)
print(response.text)  # returns task_id if all is good

# Wait for the result
task_id = response.json()["task_id"]
task_state = "UNKNOWN"
url = "https://toolbox.nextgis.com/api/json/status/{task_id}/".format(task_id=task_id)
while task_state in ["UNKNOWN", "ACCEPTED", "STARTED"]:
    time.sleep(1)
    sys.stdout.write(".")
    sys.stdout.flush()

    # Check state
    response = requests.get(url, headers=headers)
    task_state = response.json().get("state")

# Download results
if task_state == "SUCCESS":
    output = response.json()["output"][0]["value"]
    print("\n" + output)
