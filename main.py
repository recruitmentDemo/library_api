from fastapi import FastAPI, HTTPException
from typing import List
from models import Book, BookUpdate

app = FastAPI()

# Fake in-memory DB
books_db = {}
book_id_counter = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the Library API"}

@app.get("/books", response_model=List[Book])
def list_books():
    return list(books_db.values())

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

@app.post("/books", response_model=Book)
def add_book(book: Book):
    global book_id_counter
    books_db[book_id_counter] = book
    book_id_counter += 1
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    stored_book = books_db[book_id]
    updated_data = book_update.dict(exclude_unset=True)
    updated_book = stored_book.copy(update=updated_data)
    books_db[book_id] = updated_book
    return updated_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[book_id]
    return {"message": "Book deleted successfully"}
