from backend.contracts.schema import GenericSchema
from datetime import datetime
from io import BytesIO
import pandas as pd
import traceback
import requests

class APICollector():

    def __init__(self, api_url, schema: GenericSchema, aws):
        self.api_url = api_url
        self._aws = aws
        self._buffer = None
        self._schema = schema

    def start(self, param: int):
        response = self.getData(param)
        response = self.extractData(response)
        response = self.transformDf(response)
        response = self.convertToParquet(response)

        if self._buffer is not None:
            filename = self.filename()
            print(f"Upload do arquivo {filename} para o S3")
            self._aws.upload_file(response, filename)
            return True
        
        return False

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

    def transformDf(self, response):
        result = pd.DataFrame(response)
        return result

    def convertToParquet(self, response):
        self._buffer = BytesIO()
        try:
            response.to_parquet(self._buffer)
            return self._buffer
        except:
            print("Erro ao transformar o DF em parquet")
            self._buffer = None 

    def filename(self):
        date = datetime.now().isoformat()
        return f"airbnb_{date.split('.')[0]}.parquet"