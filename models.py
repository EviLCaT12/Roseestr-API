from pydantic import BaseModel
from typing import List

class Points(BaseModel):
    x: float
    y: float

class Place(BaseModel):
    address: str | None = None
    cad_cost: str | None = None
    util_by_doc: str | None = None
    cc_date_entering: str | None = None
    date_cost: str | None = None
    application_date: str | None = None
    area_value: str | None = None
    y_max: str | None = None
    x_max: str | None = None
    x_min: str | None = None
    y_min: str | None = None
    y_center: str | None = None
    x_center: str | None = None



