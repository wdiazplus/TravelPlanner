from typing import Union
from pydantic import BaseModel


class Travel(BaseModel):
    id: int
    departure_date: str
    return_date: str
    origin: str
    destiny: str
    name_destiny: str
    owner_id: int

    class Config:
        orm_mode = True