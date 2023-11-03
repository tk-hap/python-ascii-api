from fastapi.testclient import TestClient
from main import ascii_api

client = TestClient(ascii_api)

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "healthy"}