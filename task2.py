
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Contact model
class Contact(BaseModel):
    name: str
    phone: str
    email: str


# Temporary storage
contacts = []


# 1. POST - Add a contact
@app.post("/addcontact")
def add_contact(contact: Contact):
    contacts.append(contact)

    return {
        "message": "Contact added successfully",
        "name": contact.name
    }


# 2. GET - Get all contacts
@app.get("/getcontacts")
def get_contacts():
    return {
        "contacts": contacts
    }

