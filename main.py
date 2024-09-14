from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello': 'World!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurantes: str=Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        dados_restaurante = {}
        #print(dados_json)
        for item in dados_json:
            nome_do_restaurante = item['Company']
            if nome_do_restaurante not in dados_restaurante:
                dados_restaurante[nome_do_restaurante] = []
            
            dados_restaurante[nome_do_restaurante].append({
                'item': item['Item'],
                'price': item['price'],
                'description': item['description']
            })
        #print(dados_restaurante['KFC'])
    else:
        print(f'O erro foi {response.status_code}')