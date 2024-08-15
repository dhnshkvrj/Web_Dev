# To-do list using Python & FAST API

from typing import Union
from models import Todo

from fastapi import FastAPI

app = FastAPI()

todos=[]

@app.get("/")                       # Just the root so returns something
def read_root():
    return {"Hello": "World"}

# get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if(todo.id==todo_id):
            return {"todo":todo}
        return {"message":"No todo found"}

# Create a todo
@app.post("/todos")
async def create_todos(todo:Todo):
    todos.append(todo)
    return {"message":"Todo has been added"}

# Update a  todos
@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int, todo_obj:Todo):
    for todo in todos:
        if(todo.id==todo_id):
            todo.id=todo_id
            todo.item=todo_obj.item
            return {"todo":todo}
        return {"message":"No todo found"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    for todo in todos:
        if(todo.id==todo_id):
            todos.remove(todo)
            return {"message":"Todo deleted"}
        return {"message":"No todo found"}