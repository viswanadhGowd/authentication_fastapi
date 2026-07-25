from fastapi import APIRouter
from authentication_fastapi.sample_fastapi.routers.schema import UserV1

v1_router = APIRouter()

@v1_router.post("/users")
def create_user(user: UserV1):
    print(f"User data {UserV1}")
    return {
        "version": "v1",
        "message": "User created",
        "data": user
    }

@v1_router.get("/users")
def get_users():
    return {
        "version": "v1",
        "data": [{"name": "Alice", "age": 25}]
    }