
from fastapi import FastAPI

app = FastAPI(title="Payment Service")

@app.get("/payments")
def get_payments():
    return [
        {"id": 901, "status": "Success"},
        {"id": 902, "status": "Pending"}
    ]

@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    return {"id": payment_id, "service": "Payment Service"}
