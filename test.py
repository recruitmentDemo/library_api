import requests

def add_books():
    payload = {
  "title": "Harry Potter",
  "author": "J.K.Rowling",
  "description": "Fiction",
  "year_published": 2005
}
    response = requests.post("http://127.0.0.1:8000/books", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert data["description"] == payload["description"]
    assert data["year_published"] == payload["year_published"]
    print(data)


def get_books():
    response = requests.get("http://127.0.0.1:8000/books")
    assert response.status_code == 200
    data = response.json()
    print(data)


if __name__ == "__main__":
    add_books()
    get_books()
    print("All tests passed!")
