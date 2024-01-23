# ETL Project - DW #

### Descrição do Projeto ###

Essa automação visará fazer a extração de dados do Airbnb de Nova York a partir de 3 origens de dados diferentes: SQL, API e Excel.
Dados originais: new_york_listings_2024_complete.csv - Cerca de 20k linhas
Dados da API: new_york_listings_2024_api.csv - Apenas as 1k primeiras linhas.
Dados do Excel: À definir 
Dados do SQL: À definir 

### How to use ###

 - Iniciar a API fake:
 ```
    uvicorn backend.fakeapi.start:app --reload
 ```