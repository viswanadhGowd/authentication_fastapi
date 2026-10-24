
from fastapi import FastAPI
import os

app = FastAPI(title="User Service")

INSTANCE_NAME = os.getenv("INSTANCE_NAME", "user-instance-1")

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Viswa",
        "served_by": INSTANCE_NAME
    }
