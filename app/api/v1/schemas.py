from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str
    description: str
    price: int

    model_config = ConfigDict(from_attributes=True)
class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
