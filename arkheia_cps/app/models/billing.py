from pydantic import BaseModel

class BillInput(BaseModel):
    text: str
