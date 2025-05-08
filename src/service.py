from sqlmodel import Session, select
from fastapi import HTTPException
from src.models import Brand, Model
from src.schemas import BrandCreate, ModelCreate
# import schemas


class BrandService():

    def get_all_brands(self, session: Session) -> list[Brand]:
        brands = session.exec(select(Brand)).all()
        return brands

    def create_brand(self, session: Session, brand_data:BrandCreate) -> Brand:
        brand_data_dict  = brand_data.model_dump()
        new_brand = Brand(**brand_data_dict)

        query = select(Brand).where(
            Brand.name == new_brand.name
        )

        existing_model = session.exec(query).first()
        if existing_model:
            raise HTTPException(status_code=400, detail="This brand already exists in the database.")

        session.add(new_brand)
        session.commit()
        session.refresh(new_brand)
        return new_brand

class ModelService():

    def get_all_models_by_brand(self, session: Session, brand_id: int) -> list[Model]:
        query = select(Model).where(Model.brand_id == brand_id)
        models = session.exec(query).all()
        return models

    def create_model_for_brand(self, session: Session, brand_id: int, model_data:ModelCreate) -> Model:
        model_data_dict  = model_data.model_dump()
        new_model = Model(**model_data_dict)
        new_model.brand_id = brand_id

        query = select(Model).where(
            Model.brand_id == brand_id,
            Model.name == new_model.name
        )

        existing_model = session.exec(query).first()
        if existing_model:
            raise HTTPException(status_code=400, detail="Model name must be unique within the brand.")

        session.add(new_model)
        session.commit()
        session.refresh(new_model)
        return new_model

    def update_model(self, session: Session, model_id:int, model_data:ModelCreate) -> Model:
        model_data_dict = model_data.model_dump()
        update_model_data = Model(**model_data_dict)
        model = session.get(Model, model_id)

        if not model:
            raise HTTPException(status_code=404, detail="Model not found.")
        model.average_price = update_model_data.average_price
        session.add(model)
        session.commit()
        session.refresh(model)
        return model
    
    def get_model_by_params(self, session: Session, greater: int|None, lower: int|None):
        query = select(Model)

        if greater is None and lower is None:
            results = session.exec(query)
        else:
            if greater is not None:
                query = query.where(Model.average_price > greater)
            if lower is not None:
                query = query.where(Model.average_price < lower)

            results = session.exec(query)
        return results.all()
