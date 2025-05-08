from sqlmodel import SQLModel, Field, Relationship, func
from datetime import datetime


class Brand(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True, index=True)
    name: str = Field(unique=True)
    created_at: datetime = Field(default_factory=datetime.now)
    models: list['Model'] = Relationship(back_populates='brand', cascade_delete=True)

class Model(SQLModel, table=True):
    id: int|None = Field(default=None, primary_key=True, index=True)
    name: str
    average_price: int
    brand_id: int = Field(default=None, foreign_key='brand.id', ondelete='CASCADE', index=True)
    brand: Brand|None = Relationship(back_populates='models')
    created_at: datetime = Field(default_factory=datetime.now)
