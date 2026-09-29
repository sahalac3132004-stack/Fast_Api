from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary storage
tasks = []


# Task structure
class Task(BaseModel):
    title: str
    completed: bool


# POST /addtask
@app.post("/addtask")
def add_task(task: Task):
    tasks.append(task)

    return {
        "message": "Task added successfully",
        "title": task.title
    }


# GET /gettasks
@app.get("/gettasks")
def get_tasks():
    return {
        "tasks": tasks
    }