from fastapi import FastAPI
import redis
import json

app = FastAPI()

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

@app.post("/publish")
def publish_event(user_id: str, action: str):
    event = {
        "user_id": user_id,
        "action": action
    }

    r.publish("events", json.dumps(event))
    r.publish()
    return {"status": "event published"}
