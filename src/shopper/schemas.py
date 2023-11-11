from datetime import datetime

from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int
    title: str
    price: int
    created_at: datetime
    updated_at: datetime
    is_active: bool


class ProductUpdate(BaseModel):
    title: str
    price: int
    updated_at: datetime
