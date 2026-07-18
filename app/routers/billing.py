from fastapi import APIRouter

router = APIRouter(
    prefix="/billing",
    tags=["billing"]
)

@router.post("/analyze")
def analyze_billing(data: dict):
    return {"message": "Billing analysis complete", "input": data}
