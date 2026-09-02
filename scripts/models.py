from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

# Due to pydantic Basemodel now we don't need separate constructor