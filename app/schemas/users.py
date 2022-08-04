from typing import Union
from pydantic import BaseModel
from . import travels


class User(BaseModel):
    id: int
    email: str
    # travels: list[Travel] = []

    class Config:
        orm_mode = True