# import asyncio
# import httpx
# from fastapi import FastAPI
# app= FastAPI()
# semapure= asyncio.Semaphore(10)

# async def fetch(client, url):
#     print("======================")
#     async with semapure:
#         response=await  client.get(url)
#         data=response.raise_for_status()
#         print(f"fetched data:{data}")
#         return (response.json, data)

# @app.get("/limit")
# async def get_requests():
#     # return {"stats":"ok"}
#     url = "https://api.practicesoftwaretesting.com/products"
#     async with httpx.AsyncClient(timeout=1) as client:
#         results= await asyncio.gather(* [fetch(client, url) for x in range(100)])
#         print(results)
#         return {"results": results}

import asyncio
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

semaphore = asyncio.Semaphore(10)


async def fetch(client, url):
    async with semaphore:
        response = await client.get(url)
        code=response.raise_for_status()

        data = response.json()
        print(f"Fetched data: {len(data.get('data', []))} items")

        return code


@app.get("/limit")
async def get_requests():
    url = "https://api.practicesoftwaretesting.com/products"

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            results = await asyncio.gather(
                *[fetch(client, url) for _ in range(100)]
            )

        return {
            "total_requests": len(results),
            "results": results
        }

    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"External API request failed: {str(exc)}"
        )
