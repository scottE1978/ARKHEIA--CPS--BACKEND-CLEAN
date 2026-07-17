from sqlalchemy.orm import Session
from app.models.billing import Billing
from app.config import settings

class BillingService:
    def __init__(self, db: Session):
        self.db = db

    def get_records(self):
        return self.db.query(Billing).all()

    def get_record_by_id(self, record_id: int):
        return self.db.query(Billing).filter(Billing.id == record_id).first()

    def create_record(self, data):
        record = Billing(**data)
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def update_record(self, record_id: int, data):
        record = self.get_record_by_id(record_id)
        if not record:
            return None
        for key, value in data.items():
            setattr(record, key, value)
        self.db.commit()
        self.db.refresh(record)
        return record

    def delete_record(self, record_id: int):
        record = self.get_record_by_id(record_id)
        if not record:
            return None
        self.db.delete(record)
        self.db.commit()
        return True
