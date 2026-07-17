print("LOADING BILLING MODEL")

from pydantic import BaseModel

class BillInput(BaseModel):
    text: str
