print("LOADING BILLING ROUTER")

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.billing_service import BillingService

router = APIRouter(
    prefix="/billing",
    tags=["billing"]
)

@router.get("/")
def list_billing_records(db: Session = Depends(get_db)):
    service = BillingService(db)
    return service.get_records()

@router.get("/{record_id}")
def get_billing_record(record_id: int, db: Session = Depends(get_db)):
    service = BillingService(db)
    return service.get_record_by_id(record_id)

@router.post("/")
def create_billing_record(data: dict, db: Session = Depends(get_db)):
    service = BillingService(db)
    return service.create_record(data)

@router.put("/{record_id}")
def update_billing_record(record_id: int, data: dict, db: Session = Depends(get_db)):
    service = BillingService(db)
    return service.update_record(record_id, data)

@router.delete("/{record_id}")
def delete_billing_record(record_id: int, db: Session = Depends(get_db)):
    service = BillingService(db)
    return service.delete_record(record_id)
