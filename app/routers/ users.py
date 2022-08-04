from fastapi import APIRouter
from pydantic import BaseModel
# from ..models.users import User
# from ..schemas.users import User
# from ..utils import crud_users
# from ..main import get_db

router = APIRouter()

@router.post("/users/", response_model=User, tags=["users"]) 
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
     

@router.get("/users/{user_id}", response_model=User, tags=["users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@userroute.put("/users/{username}", tags=["users"])
def update_user():
    return "Actualizando un user"

@userroute.delete("/users/{username}", tags=["users"])
def delete_user():
    return "Eliminando un user"

@userroute.get("/users/", tags=["users"])
def read_users():
    return "Return all users that exist"