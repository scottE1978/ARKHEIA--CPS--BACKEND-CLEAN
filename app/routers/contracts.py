from fastapi import APIRouter

router = APIRouter(
    prefix="/contracts",
    tags=["contracts"]
)

@router.post("/analyze")
def analyze_contracts(data: dict):
    return {"message": "Contract analysis complete", "input": data}
