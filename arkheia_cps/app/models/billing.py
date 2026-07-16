from fastapi import APIRouter
from arkheia_cps.app.models.billing import BillInput

router = APIRouter(
    prefix="/billing",
    tags=["billing"]
)

@router.post("/process")
def process_bill(data: BillInput):
    return {"received": data.text}
