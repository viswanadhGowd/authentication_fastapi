
from fastapi import FastAPI

app = FastAPI(title="Order Service")

@app.get("/orders")
def get_orders():
    return [
        {"id": 501, "status": "Created"},
        {"id": 502, "status": "Shipped"}
    ]

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return {"id": order_id, "service": "Order Service"}
