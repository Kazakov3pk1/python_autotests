import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '710b4460994dafbff1875f39050b98d5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create_pokemon = {
    "name": "generate",
    "photo_id": 362
}

body_change_pokemon = {
    "pokemon_id": "244756",
    "name": "qwerty",
    "photo_id": 362
}

body_pokeball_pokemon = {
    "pokemon_id": "244756"  
}

response = requests.post(url= f'{URL}/pokemons', headers=HEADER, json = body_create_pokemon)
print(response.text)

response = requests.put(url= f'{URL}/pokemons', headers=HEADER, json = body_change_pokemon)
print(response.text)

response = requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_pokeball_pokemon)
print(response.text)
