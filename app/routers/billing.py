from fastapi import APIRouter

router = APIRouter()

@router.get("/billing/test")
def billing_test():
    return {"message": "Billing router is working"}
