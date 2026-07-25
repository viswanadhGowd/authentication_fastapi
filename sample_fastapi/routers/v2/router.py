from fastapi import APIRouter
from fastapi import HTTPException
from authentication_fastapi.sample_fastapi.routers.schema import UserV2
v2_router= APIRouter()

@v2_router.post("/users")
def create_user(userdata:UserV2):
    try:
        if userdata:
            return {
            "version": "v2",
            "message": "User created",
            "data": userdata
        }
    except Exception as err:
        raise HTTPException(status_code= 403,detail="Missing values")

@v2_router.get("/users")
def get_user():
    return {
        "version": "v2",
        "data": [
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "email": "alice@example.com",
                "age": 25
            }
        ]
    }