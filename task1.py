from fastapi import FastAPI

app = FastAPI()


# 1. Root Endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Math API!"}


# 2. Multiplication Endpoint
@app.get("/multiply/{number}")
def multiply(number: int):
    return {
        "number": number,
        "result": number * 5
    }


# 3. Square Endpoint
@app.get("/square/{number}")
def square(number: int):
    return {
        "number": number,
        "result": number ** 2
    }