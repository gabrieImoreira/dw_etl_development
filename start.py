import variables.variables as variables
from backend.datasource.API import APICollector
from backend.contracts.schema import RoomsSchema
from backend.libraries.AWS.S3Client import S3Client
import json

s3 = S3Client()
api = APICollector(variables.URL_AIRBNB_API, RoomsSchema, s3)
response = api.start(100)
response = json.dumps(response, indent=2)
print(response)