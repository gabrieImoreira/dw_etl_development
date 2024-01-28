import variables.variables as variables
from backend.datasource.API import APICollector
from backend.contracts.schema import RoomsSchema
import json

api = APICollector(variables.URL_AIRBNB_API, RoomsSchema)

response = api.getData(20)
response = api.extractData(response)
response = json.dumps(response, indent=2)
print(response)