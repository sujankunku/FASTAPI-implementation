from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return "GDSC VIT IS AMAGING!"


Todos = {
    1 : {
        "title": "Complete Computer Networks Assignment",
        "completed": False,
    },
    2 : {
        "title": "Complete 10 Questions from Binary Search concept",
        "completed": False,
    },
    3 : {
        "title": "Complete the 2km Jogging",
        "completed": False,
    }
}

#Request body schema
class TodoItem(BaseModel):
    title: str
    completed: bool


#Endpoints

# 1. view all the exiting todo items
@app.get("/todos")
def get_all_todo_items(title: str=""):
    results={}
    if title!="" or title != None:
        for id in Todos:
            if title in Todos[id]["title"]:
                results[id] = Todos[id]
    else:
        results = Todos
    return results

#displaying single todo task
@app.get("/todos/{id}",status_code=status.HTTP_200_OK)
def get_todo_item(id: int):
    if id in Todos:
       return Todos[id]
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not found")

#2. create todo items
@app.post("/todos",status_code=status.HTTP_201_CREATED)
def create_todo_item(todo_item: TodoItem):
    id = max(Todos)+1
    Todos[id]=todo_item.dict()
    return Todos[id]

#3. update todo item
@app.put("/todos/{id}",status_code=status.HTTP_200_OK)
def update_todo_item(id: int,todo_item: TodoItem):
    if id in Todos:
      Todos[id] = todo_item.dict()
      return Todos[id]
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not found")

#4. Delete todo item
@app.delete("/todos/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_item(id: int):
    if id in Todos:
       Todos.pop(id)
       return 
    
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not found")