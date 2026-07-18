print("MAIN IMPORTED")

from fastapi import FastAPI
from app.routers import billing, contracts

app = FastAPI(
    title="ARKHEIA-CPS",
    version="1.0.0"
)

app.include_router(billing.router)
app.include_router(contracts.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
