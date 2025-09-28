# Simplest tool run using Toolbox SDK
# Tool: https://toolbox.nextgis.com/t/hello
# More SDK examples: https://pypi.org/project/toolbox-sdk/

from toolbox_sdk import ToolboxClient

##############SET THESE#######################
token = "YOUR API TOKEN"
tool_name = "hello"
name = "John"
##############################################

toolbox = ToolboxClient(token)
tool = toolbox.tool(tool_name)

# Run and wait for the result
result = tool({
    "name": name
})

print(result.value)