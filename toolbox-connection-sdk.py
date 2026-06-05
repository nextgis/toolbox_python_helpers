# Simplest tool run using Toolbox SDK
# Tool: https://toolbox.nextgis.com/t/webmap2qgis
# More SDK examples: https://pypi.org/project/toolbox-sdk/

from toolbox_sdk import ToolboxClient

##############SET THESE#######################
token = "YOUR API TOKEN"
tool_name = "webmap2qgis"
# Guest mode
webgis_connection = {"url": "https://demo.nextgis.com"}
# Example with authorization
# webgis_connection = {"url":"https://sandbox.nextgis.com","login":"administrator","password":"demodemo"}
webmap_id = 4226  # try 5 for authorization example
output_format = "Geopackage"
crs_id = 4326
##############################################

toolbox = ToolboxClient(token)
tool = toolbox.tool(tool_name)

# Run and wait for the result
result = tool(
    {
        "webgis_connection": webgis_connection,
        "webmap_id": webmap_id,
        "output_format": output_format,
        "crs_id": crs_id,
    }
)

# Download all results into the current directory
toolbox.download_results(result, ".")
