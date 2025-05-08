from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from src.service import BrandService, ModelService
from src.database import get_session
from src.schemas import (
    Model,
    BaseModel,
    ModelCreate,
    Brand,
    BrandBase,
    BrandCreate
)

brand_router = APIRouter()
models_router = APIRouter()
brand_service = BrandService()
model_service = ModelService()

@brand_router.get("/", status_code=status.HTTP_200_OK, response_model=list[Brand])
def get_all_brands(session: Session = Depends(get_session)) -> dict:
    brands = brand_service.get_all_brands(session)
    return brands


@brand_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Brand)
def create_brand(brand_data: BrandCreate, session: Session = Depends(get_session)) -> dict:
    new_brand = brand_service.create_brand(session, brand_data)
    return new_brand


@brand_router.get("/{id}/models", status_code=status.HTTP_200_OK, response_model=list[Model])
def get_all_models_by_brand(id: int, session: Session = Depends(get_session)) -> dict:
    models = model_service.get_all_models_by_brand(session, int(id))
    return models


@brand_router.post("/{id}/models", status_code=status.HTTP_201_CREATED, response_model=Model)
def create_model_for_brand(model_data: ModelCreate, id:int, session: Session = Depends(get_session)) -> dict:
    new_model = model_service.create_model_for_brand(session, id, model_data)
    return new_model


@models_router.put("/models/{id}", status_code=status.HTTP_200_OK, response_model=Model)
def update_model(model_data: ModelCreate, id:int, session: Session = Depends(get_session)) -> dict:
    updated_model = model_service.update_model(session, id, model_data)
    return updated_model


@models_router.get("/models", status_code=status.HTTP_200_OK, response_model=list[Model])
def get_model_by_params(greater: int|None = None, lower:int|None = None, session: Session = Depends(get_session)) -> dict:
    models = model_service.get_model_by_params(session, greater, lower)
    return models
