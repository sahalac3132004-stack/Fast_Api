
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

# Temporary storage
tasks = []


# Task model
class Task(BaseModel):
    title: str
    status: Literal["pending", "completed"]


# 1. Add a task
@app.post("/addtask")
def add_task(task: Task):
    tasks.append(task)

    return {
        "message": "Task added successfully",
        "task": task
    }


# 2. Get all tasks
@app.get("/gettask")
def get_tasks():
    return {
        "tasks": tasks
    }


# 3. Update a task
@app.put("/updatetask/{index}")
def update_task(index: int, task: Task):
    if index < 0 or index >= len(tasks):
        return {"message": "Task not found"}

    tasks[index] = task

    return {
        "message": "Task updated successfully",
        "task": task
    }


# 4. Delete a task
@app.delete("/deletetask/{index}")
def delete_task(index: int):
    if index < 0 or index >= len(tasks):
        return {"message": "Task not found"}

    deleted_task = tasks.pop(index)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }


