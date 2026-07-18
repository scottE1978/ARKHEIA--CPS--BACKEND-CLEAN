from fastapi import FastAPI
from app.routers import billing, contracts

app = FastAPI()

# Include routers
app.include_router(billing.router)
app.include_router(contracts.router)

# Optional homepage route
@app.get("/")
def root():
    return {"status": "ARKHEIA-CPS backend is running"}
