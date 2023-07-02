from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    """
    Создает новый товар.
    """
    return {"item": item}

@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Обновляет информацию о товаре.
    """
    return {"item_id": item_id, "item": item}

# Изменяем примеры в эндпоинтах
@app.post("/items/", response_model=Item, response_model_exclude_unset=True)
async def create_item_with_examples(item: Item):
    """
    Создает новый товар с примерами.
    """
    return {"item": item}

@app.post("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def update_item_with_examples(item_id: int, item: Item):
    """
    Обновляет информацию о товаре с примерами.
    """
    return {"item_id": item_id, "item": item}