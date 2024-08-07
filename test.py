from fastapi.testclient import TestClient
from http import HTTPStatus
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"Hello": "World"}


def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"item_id": 1, "q": None}


def test_read_item_with_q():
    response = client.get("/items/1?q=test")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"item_id": 1, "q": "test"}


def test_create_item():
    json_payload = {
        "name": "Test Item",
        "description": "This is a test item",
        "price": 1,
        "tax": 2.5
    }

    response = client.post("/items/", json=json_payload)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == json_payload


def test_read_cookie():
    client.post("/cookie")  # Set cookie
    response = client.get("/cookie")  # Read cookie
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"user": "joel_geiser"}
