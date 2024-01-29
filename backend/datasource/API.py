from backend.contracts.schema import GenericSchema
import requests

class APICollector():

    def __init__(self, api_url, schema):
        self.api_url = api_url
        self._aws = None
        self._buffer = None
        self._schema = schema

    def start(self, param: int):
        response = self.getData(param)
        response = self.extractData(response)
        return response
    def getData(self, param: int):
        if param is None:
            response = requests.get(self.api_url)
        elif param < 1:
            return "Number de parâmetros tem que ser maior que 0"
        
        response = requests.get(self.api_url + '/' + str(param))
        return response.json()

    def extractData(self, response):
        result: List[GenericSchema] = []
        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item.get(key)) == value:
                    index[key] = item[key]
                else:
                    index[key] = None
            result.append(index)
        return result



    def transformDf(self):
        pass
