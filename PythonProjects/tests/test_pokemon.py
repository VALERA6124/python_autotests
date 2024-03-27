import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'TOKEN'
HEADERS = {
           'Content-Type' : 'application/json',
           'trainer_token' : TOKEN
           }

def test_status_200():
    response = requests.get(url=f'{URL}/trainers', params= {"trainer_id" : id тренера})
    assert response.status_code == 200

def test_name_trainers():
    response = requests.get(url=f'{URL}/trainers', params= {"trainer_id" : id тренера})
    assert response.json()['data'][0]['trainer_name'] == 'имя тренера'
