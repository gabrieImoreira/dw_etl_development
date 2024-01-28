import requests

class APICollector():

    def __init__(self, api_url):
        self.api_url = api_url
        self.aws = None
        self.buffer = None
        self.schema = None

    def start(self):
        pass

    def getData(self, num_registers: int):
        response = requests.get(self.api_url + '/' + str(num_registers))
        return response.json()

    def extractData(self):
        pass

    def transformDf(self):
        pass
