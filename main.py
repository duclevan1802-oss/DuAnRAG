from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from database import users_collection

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello Duck"}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/hello")
def hello(name: str):
    if name != "duc":
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": f"Hello {name}"}


# Dữ liệu nhận
class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None


# Dữ liệu trả ra
class UserResponse(BaseModel):
    name: str
    age: int


@app.post("/user")
def create_user(user: User):
    user_data = user.model_dump()
    result = users_collection.insert_one(user_data)
    return {
        "message": "User created successfully",
        "id": str(result.inserted_id)
    }


# Dependency
def check_user(name: str):
    if name != "Hung":
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "name": name,
    }

def get_user_age():
    return 18

@app.get("/profile/{name}")
def get_profile(
    name: str = Depends(check_user),
    age: int = Depends(get_user_age)
):
    return {"name": name, "age": age}