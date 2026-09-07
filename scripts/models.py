from pydantic import BaseModel

# Due to pydantic Basemodel now we don't need separate constructor
# pydantic class
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

# Create a separate Product class for SQLAlchemy so the database schema
# is generated based on this specific class.

