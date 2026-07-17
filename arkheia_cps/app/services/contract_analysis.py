from sqlalchemy.orm import Session
from app.models.<model_name> import <Model>   # only models
from app.config import settings               # safe
# NO router imports
# NO main imports

class <ServiceClass>:
    def __init__(self, db: Session):
        self.db = db

    def list_items(self):
        return self.db.query(<Model>).all()
