from sqlmodel import Session, create_engine, SQLModel
from sqlalchemy import event

DATABASE_URL_CONNECTION = 'sqlite:///./nexu.db'
engine = create_engine(DATABASE_URL_CONNECTION, connect_args={'check_same_thread': False})

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
