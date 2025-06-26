import requests

BASE_URL = "http://127.0.0.1:8000"

def test_add_book():
    payload = {
        "title": "Harry Potter",
        "author": "J.K.Rowling",
        "description": "Fiction",
        "year_published": 2005
    }

    response = requests.post(f"{BASE_URL}/books", json=payload)
    assert response.status_code == 200
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert data["description"] == payload["description"]
    assert data["year_published"] == payload["year_published"]

def test_get_books():
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert any(book["title"] == "Harry Potter" for book in data)
