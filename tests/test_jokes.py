import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from main import app
from services.api_jokes import api_jokes, select_joke

client = TestClient(app)


def test_has_not_select_joke():
    with pytest.raises(KeyError):
        select_joke('Joke')


def test_not_suppoted_joke():
    response = client.get('/jokes/Data')
    detail_error = {"detail": "This type of joke is not supported"}
    assert response.status_code == 400
    assert response.json() == detail_error

def test_random_joke():
    response = client.get('/jokes/')
    joke = response.json()
    assert response.status_code == 200
    assert joke['value'] != ''

def test_save_joke():
    joke = "Hijo, me veo gorda, fea y vieja. ¿Qué tengo hijo, qué tengo? Mamá, tienes toda la razón."
    response = client.post('/jokes/', json={"value": joke})
    assert response.status_code == 200

def test_not_save_empty_joke():
    joke = '   '
    response = client.post('/jokes/', json={"value": joke})
    assert response.status_code == 422
    

def test_update_joke():
    joke = "Hijo, me veo gorda, fea y vieja. ¿Qué tengo hijo, qué tengo? Mamá, tienes toda la razón."
    response = client.post('/jokes/', json={"value": joke})
    joke_id = response.json()["id"]
    new_joke = "¿Cómo se dice pelo sucio en chino? Chin cham pu"
    update_response = client.put(f"/jokes/{joke_id}",json={"value": new_joke})
    assert update_response.status_code == 202

def test_not_update_joke():
    new_joke = "¿Cómo se dice pelo sucio en chino? Chin cham pu"
    joke_id=0
    update_response = client.put(f"/jokes/{joke_id}",json={"value": new_joke})
    assert update_response.status_code == 400
    

def test_delete_joke():
    joke = "Hijo, me veo gorda, fea y vieja. ¿Qué tengo hijo, qué tengo? Mamá, tienes toda la razón."
    response = client.post('/jokes/', json={"value": joke})
    joke_id = response.json()["id"]
    delete_response = client.delete(f"/jokes/{joke_id}")
    assert delete_response.status_code == 204

def test_not_delete_joke():
    joke_id = -1
    delete_response = client.delete(f"/jokes/{joke_id}")
    assert delete_response.status_code == 400