import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from services.api_jokes import api_jokes, select_joke
from main import app

client = TestClient(app)

def test_has_not_select_joke():
  with pytest.raises(KeyError):
    select_joke('Joke')
    
def test_not_suppoted_joke():
  response = client.get('/jokes/Data')
  detail_error = {"detail":"This type of joke is not supported"}
  assert response.status_code == 400
  assert response.json() == detail_error
    