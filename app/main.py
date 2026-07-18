from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
@app.head("/")
def root():
    return JSONResponse({"status": "ARKHEIA-CPS backend is running"})
