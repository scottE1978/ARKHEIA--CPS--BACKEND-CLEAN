from fastapi import APIRouter
from arkheia_cps.app.services.billing_analysis import analyze_bill
from arkheia_cps.app.models.billing import BillInput

router = APIRouter(
    prefix="/analysis/billing",
    tags=["Billing Analysis"]
)

@router.post("/")
def analyze_billing_endpoint(payload: BillInput):
    """
    Billing Error Analysis Endpoint
    -------------------------------
    Accepts raw billing statement text and returns:
    - mismatched totals
    - duplicate charges
    - unexplained fees
    - missing discounts
    - timeline inconsistencies
    - ambiguous line items

    Designed to help seniors and vulnerable consumers understand
    confusing monthly bills.
    """
    return analyze_bill(payload.text)
