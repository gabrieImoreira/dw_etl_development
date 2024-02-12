import variables.variables as variables
from backend.datasource.API import APICollector
from backend.contracts.schema import RoomsSchema
from backend.libraries.AWS.S3Client import S3Client
import json, schedule, time

s3 = S3Client()

def apiCollector(url_api, schema, aws, repeat):
    api = APICollector(url_api, schema, aws).start(repeat)
    # response = json.dumps(response, indent=2)
    print(f'API Collector started, response: {api}')
    return

schedule.every(30).seconds.do(apiCollector, variables.URL_AIRBNB_API, RoomsSchema, s3, 50)


while True:
    schedule.run_pending()
    time.sleep(1)