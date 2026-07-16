from fastapi import FastAPI
from routers.billing import router as billing_router
from routers.contracts import router as contracts_router

app = FastAPI()

app.include_router(billing_router)
app.include_router(contracts_router)
