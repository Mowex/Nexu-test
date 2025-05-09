from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ModelBase(BaseModel):
    name: str | None = None
    average_price: int

class ModelCreate(ModelBase):
    pass

class Model(ModelBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class BrandBase(BaseModel):
    name: str

class BrandCreate(BrandBase):
    pass

class Brand(BrandBase):
    id: int
    created_at: datetime
    models: list[Model] = []
    model_config = ConfigDict(from_attributes=True)