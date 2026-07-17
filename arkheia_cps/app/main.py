
from fastapi import FastAPI
from app.routers import billing, contracts  # adjust to your actual router names

app = FastAPI()

app.include_router(billing.router)
app.include_router(contracts.router)
