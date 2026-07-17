from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.contract_service import ContractService

router = APIRouter(
    prefix="/contracts",
    tags=["contracts"]
)

@router.get("/")
def list_contracts(db: Session = Depends(get_db)):
    service = ContractService(db)
    return service.get_contracts()

@router.get("/{contract_id}")
def get_contract(contract_id: int, db: Session = Depends(get_db)):
    service = ContractService(db)
    return service.get_contract_by_id(contract_id)

@router.post("/")
def create_contract(data: dict, db: Session = Depends(get_db)):
    service = ContractService(db)
    return service.create_contract(data)

@router.put("/{contract_id}")
def update_contract(contract_id: int, data: dict, db: Session = Depends(get_db)):
    service = ContractService(db)
    return service.update_contract(contract_id, data)

@router.delete("/{contract_id}")
def delete_contract(contract_id: int, db: Session = Depends(get_db)):
    service = ContractService(db)
    return service.delete_contract(contract_id)
