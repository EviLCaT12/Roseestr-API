import rosreestr_api.api_client as rosreestr
from fastapi import FastAPI

from models import *
from typing import List


app = FastAPI()


# examples
@app.post("/place/", response_model=List[Place])
async def place(points: Points = Points(x=43.165029, y=131.242545)):
    places = rosreestr.get_places(points.x, points.y)
    return places



