
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Book model
class Book(BaseModel):
    title: str
    author: str


# Temporary book storage
books = []


# 1. POST - Add a book
@app.post("/addbook")
def add_book(book: Book):
    books.append(book)

    return {
        "message": "Book added successfully",
        "book": book
    }


# 2. GET - Get all books
@app.get("/getbooks")
def get_books():
    return {
        "books": books
    }


# 3. PUT - Update a book
@app.put("/updatebook/{index}")
def update_book(index: int, book: Book):
    if index < 0 or index >= len(books):
        return {"message": "Book not found"}

    books[index] = book

    return {
        "message": "Book updated successfully",
        "book": book
    }


# 4. DELETE - Delete a book
@app.delete("/deletebook/{index}")
def delete_book(index: int):
    if index < 0 or index >= len(books):
        return {"message": "Book not found"}

    deleted_book = books.pop(index)

    return {
        "message": "Book deleted successfully",
        "book": deleted_book
    }

