import rosreestr_api.api_client as rosreestr
from fastapi import FastAPI

from models import *
from typing import List


app = FastAPI()


@app.post("/place/", response_model=List[Place])
async def place(points: Points = Points(x=43.165029, y=131.242545)):
    """
    Параметры: \\
    address - Адрес \\
    cad_cost - Кадастровая стоимость(в рублях) \\
    util_by_doc - Разрешённое использования \\
    cc_date_entering - Дата внесения сведений \\
    date_cost - Дата определения \\
    application_date - Дата применения \\
    area_value - Площадь(кв. м) \
    """
    places = rosreestr.get_places(points.x, points.y)
    return places



