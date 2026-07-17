from sqlalchemy.orm import Session
from app.models.contracts import Contract
from app.config import settings

class ContractService:
    def __init__(self, db: Session):
        self.db = db

    def get_contracts(self):
        return self.db.query(Contract).all()

    def get_contract_by_id(self, contract_id: int):
        return self.db.query(Contract).filter(Contract.id == contract_id).first()

    def create_contract(self, data):
        contract = Contract(**data)
        self.db.add(contract)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def update_contract(self, contract_id: int, data):
        contract = self.get_contract_by_id(contract_id)
        if not contract:
            return None
        for key, value in data.items():
            setattr(contract, key, value)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def delete_contract(self, contract_id: int):
        contract = self.get_contract_by_id(contract_id)
        if not contract:
            return None
        self.db.delete(contract)
        self.db.commit()
        return True
