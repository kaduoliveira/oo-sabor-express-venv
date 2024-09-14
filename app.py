import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    #print(dados_json)
    for item in dados_json:
        nome_do_restaurante = item['Company']
        nome_do_prato = item['Item']
        preco = item['price']
        descricao = item['description']
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

print(dados_restaurante['Burger King'])