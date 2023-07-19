import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from requests import get

app = FastAPI()


class Item(BaseModel):
    name: str
    # optional for notes
    notes: Optional[str] = None
    time: int


class UpdateItem(BaseModel):
    name: Optional[str] = None
    notes: Optional[str] = None
    time: Optional[int] = None


todo_list = {
    1: Item(name="Task 1", notes="this if a note for task 1", time=60)
}


@app.get("/")
# item id must be int, path parameter
def home():
    return "All good"


@app.get("/get-item/{item_id}")
# item id must be int, path parameter
def get_item(item_id: int):
    return todo_list[item_id]


# query parameter ({{url}}/get-by-name?name=Clean Room)
@app.get("/get-by-name")
def get_item(name: str):
    for item_id in todo_list:
        if todo_list[item_id].name == name:
            return todo_list[item_id]
    return {"Data": "Not Found"}


# inserts things to todo list
@app.post("/create-item/{item_id}")
#     sending item information into request body
def create_item(item_id: int, item: Item):
    if item_id in todo_list:
        return {"Error": "Item already exists."}

    todo_list[item_id] = item
    return todo_list[item_id]


@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    del todo_list[item_id]
    return item_id


@app.get("/all")
def get_all():
    return todo_list


@app.get("/get-weather")
def get_weather(latitude: int, longitude: int):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    resp = get(url)
    return resp.content


# put method for full updating
@app.put("/update-item/{item_id}", description="Must change all details")
def update_item(item_id: int, item: Item):  # using Item pydantic basemodel (have to change all details)
    if item_id not in todo_list:
        return {"Error": "Item ID does not exist"}
    if item.name is not None:
        todo_list[item_id].name = item.name
    if item.notes is not None:
        todo_list[item_id].notes = item.notes
    if item.time is not None:
        todo_list[item_id].time = item.time
    return [item_id]

# patch method for partial update
@app.patch("/modify-item/{item_id}", description="Only for patial updates")
def modify_item(item_id: int, item: UpdateItem):  # using UpdateItem pydantic basemodel
    if item_id not in todo_list:
        return {"Error": "Item ID does not exist"}
    if item.name is not None:
        todo_list[item_id].name = item.name
    if item.notes is not None:
        todo_list[item_id].notes = item.notes
    if item.time is not None:
        todo_list[item_id].time = item.time
    return [item_id]

if __name__ == "__main__":
    uvicorn.run("request_prac:app", host="0.0.0.0", port=8000, reload=True)
