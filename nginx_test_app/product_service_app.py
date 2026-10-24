
from fastapi import FastAPI

app = FastAPI(title="Product Service")

@app.get("/products")
def get_products():
    return [
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Mobile"}
    ]

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"id": product_id, "service": "Product Service"}
