from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.post("/users/{username}", tags=["users"]) 
async def create_item(username: str):
    return {"username": username} 

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}

@router.put("/users/{username}", tags=["users"])
async def update_user():
    return "Actualizando un user"

@router.delete("/users/{username}", tags=["users"])
async def delete_user():
    return "Eliminando un user"

@router.get("/users/", tags=["users"])
async def read_users():
    return "Return all users that exist"