FROM python:3.11

# Instalar o pipenv
RUN pip install pipenv

# Copiar os arquivos Pipfile e Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Instalar as dependências do projeto

# Copiar o restante dos arquivos do projeto
COPY . /app

# Definir o diretório de trabalho como /app
WORKDIR /app
RUN pipenv install
RUN pip install fastapi uvicorn  

# Expor a porta 8001
EXPOSE 8001

# Definir o comando de entrada para executar o uvicorn
CMD ["pipenv", "run", "uvicorn", "backend.fakeapi.start:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]
