import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TOKEN'
HEADERS = {
           'Content-Type' : 'application/json',
           'trainer_token' : TOKEN
           }

body = {
    "name": "имя",
    "photo": "https://dolnikov.ru/pokemons/albums/100.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)
data = response.json()

id = data['id']

body_new_name = {
    "pokemon_id": id,
    "name": "Новое имя",
    "photo": "https://dolnikov.ru/pokemons/albums/100.png"
}

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_new_name)
print(response_put.text)
data = response.json()

body_pokeball={
    "pokemon_id": id
}
response_pokeball= requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADERS, json=body_pokeball)
print(response_pokeball.text)
