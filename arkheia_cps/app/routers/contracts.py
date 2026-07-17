from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.<service_name> import <ServiceClass>

router = APIRouter(
    prefix="/<route>",
    tags=["<tag>"]
)

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    service = <ServiceClass>(db)
    return service.list_items()
