from pydantic import BaseModel


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



