import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from src.main import app
from src.database import get_session
from src.seed import seed
import os


test_engine = create_engine(
    "sqlite:///./nexu_test.db",
    connect_args={"check_same_thread": False}
)

@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    if os.path.exists("nexu_test.db"):
        os.remove("nexu_test.db")
    SQLModel.metadata.create_all(test_engine)

@pytest.fixture
def session():
    with Session(test_engine) as session:
        seed()
        yield session

@pytest.fixture
def client(session):
    def override_get_session():
        yield session
    app.dependency_overrides[get_session] = override_get_session
    client = TestClient(app)
    return client
