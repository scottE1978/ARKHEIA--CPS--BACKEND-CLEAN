from fastapi import FastAPI
from arkheia_cps.routers.billing import router as billing_router
from arkheia_cps.routers.contracts import router as contracts_router

app = FastAPI()

app.include_router(billing_router)
app.include_router(contracts_router)
