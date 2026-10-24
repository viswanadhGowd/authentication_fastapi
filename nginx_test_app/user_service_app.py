
from fastapi import FastAPI

app = FastAPI(title="User Service")

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Viswa"},
        {"id": 2, "name": "Rahul"}
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "service": "User Service"}
