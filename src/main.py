from fastapi import FastAPI
from src.routers.brand import brand_router, models_router
from src.database import create_db_and_tables
from src.seed import seed
from contextlib import asynccontextmanager

@asynccontextmanager
def life_span(app:FastAPI):
    print(f"server is starting... ")
    create_db_and_tables()
    seed()
    yield
    print(f"server has been stopped")

version = 'v1'

app = FastAPI(
    title="Nexu-test",
    description="A REST API",
    debug=True,
    version=version,
    lifespan=life_span
)


app.include_router(brand_router, prefix=f"/brands", tags=['brands'])
app.include_router(models_router) 