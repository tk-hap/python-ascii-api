from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from main import ascii_api

client = TestClient(ascii_api)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "healthy"}


@patch("main.r", autospec=True)
def test_add_art(mock_redis):
    mock_redis.hset.return_value = 1

    response = client.post(
        "/art",
        json={
            "name": "monster",
            "ascii_b64": "2akozL7il4/MrsyuzIPMvuKAosyDzL4p27Y=",
            "artist": "John",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"message": "ASCII art monster added"}


@patch("main.r", autospec=True)
def test_read_art(mock_redis):
    mock_redis.hget.return_value = "2akozL7il4/MrsyuzIPMvuKAosyDzL4p27Y="

    response = client.get("/art/monster")

    assert response.status_code == 200
    assert response.text == r"٩(̾●̮̮̃̾•̃̾)۶"
