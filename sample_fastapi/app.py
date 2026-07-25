# from fastapi import APIRouter, FastAPI, Request
# from slowapi.errors import RateLimitExceeded
# from slowapi.util import get_remote_address
# from slowapi.middleware import SlowAPIMiddleware
# from slowapi import Limiter
# from fastapi.responses import JSONResponse
# app= FastAPI(title="My testing app")

# from routers.v1.router import v1_router
# from routers.v2.router import v2_router

# app.include_router(v1_router,prefix="/api/v1", tags=["v1"])
# app.include_router(v2_router, prefix="/api/v2", tags=["v2"])

# limiter= Limiter(key_func= get_remote_address)
# app.state.limiter=limiter
# app.add_middleware(SlowAPIMiddleware)

# @app.get("/home/")
# @limiter.limit("5/minute")
# async def get(request: Request):
#     print("hello world")
#     return {"home": "Ok" }

# @app.exception_handler(RateLimitExceeded)
# async def rate_limit_exced(request: Request,exc: RateLimitExceeded):
#     return JSONResponse(status_code=429, content={"details": "TO Many requests"})


#-----------------
# from fastapi import FastAPI, Request
# import asyncio
# app = FastAPI()

# @app.middleware("http")
# async def log_middleware(
#     request: Request,
#     call_next
# ):

#     print("Before request")
#     await asyncio.sleep(5)
#     response = await call_next(request)

#     print("After request")

#     return response


# @app.get("/")
# async def home():
#     print("Home is called")
#     return {"message": "Hello"}

# from fastapi import FastAPI
# from transformers import pipeline

# app = FastAPI()

# # Load local model
# generator = pipeline(
#     "text-generation",
#     model="distilgpt2"
# )

# @app.get("/generate")
# def generate(prompt: str):

#     result = generator(
#         prompt,
#         max_length=100
#     )

#     return {
#         "response": result[0]["generated_text"]
#     }



import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe("events")

print("Listening for events...")

for message in pubsub.listen():
    if message["type"] == "message":
        data = json.loads(message["data"])
        print(f"Processing event: {data}")