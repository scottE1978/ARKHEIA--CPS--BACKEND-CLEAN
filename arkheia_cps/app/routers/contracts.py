from fastapi import APIRouter
from arkheia_cps.app.services.contract_analysis import analyze_contract
from arkheia_cps.app.models.contract import ContractInput

router = APIRouter(
    prefix="/analysis/contract",
    tags=["Contract Analysis"]
)

@router.post("/")
def analyze_contract_endpoint(payload: ContractInput):
    """
    Contract Analysis Endpoint
    --------------------------
    Accepts raw contract text and returns:
    - structural inconsistencies
    - factual contradictions
    - undefined terms
    - mismatched numbers
    - missing references
    - timeline errors

    This endpoint is part of the ARKHEIA‑CPS multi‑discipline engine.
    """
    return analyze_contract(payload.text)
