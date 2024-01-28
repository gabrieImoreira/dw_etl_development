import variables.variables as variables
from backend.datasource.API import APICollector
import json
api = APICollector(variables.URL_AIRBNB_API)

response = api.getData(20)
# response = json.dumps(response, indent=2)
print(response)