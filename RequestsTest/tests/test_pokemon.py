import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '710b4460994dafbff1875f39050b98d5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '22242'

def test_trainers_status_code():
    responce = requests.get(url = f'{URL}/trainers')
    assert responce.status_code == 200

def test_part_of_response():
    responce_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert responce_get.json()["data"][0]['trainer_name'] == 'Молния в тапках'