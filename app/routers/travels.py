from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.post("/travels/{travel}", tags=["travels"]) 
async def create_travel(travel: str):
    return {"travel": travel} 

@router.get("/travels/{travel}", tags=["travels"])
async def read_travel(travel: str):
    return {"travel": travel}

@router.put("/travels/{travel_id}", tags=["travels"])
async def update_travel():
    return "Actualizando un travel"

@router.delete("/travels/{travel_id}", tags=["travels"])
async def delete_user():
    return "Eliminando un travel"

@router.get("/travels/", tags=["travels"])
async def read_travels():
    return "Return all travels that exist"

@router.get("/travels/user/{user_id}", tags=["travels"])
async def get_travel_for_user(user_id: int):
    return "Return all travels for a specific user"