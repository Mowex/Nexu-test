# seed.py
import json
from sqlmodel import Session, select
from src.database import engine
from src.models import Brand, Model
from pathlib import Path


SEED_DATA_DIR = Path(__file__).resolve().parent / "seed_data"


def seed():
    with Session(engine) as session:
        existing = session.exec(select(Brand)).first()
        if existing:
            print("Seed already executed before... skipping...")
            return
        
        data_file = SEED_DATA_DIR / "models.json"

        with open(data_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            brand_name = item['brand_name']
            statement = select(Brand).where(Brand.name == brand_name)
            brand = session.exec(statement).first()

            if not brand:
                brand = Brand(name=brand_name)
                session.add(brand)
                session.commit()
                session.refresh(brand)

            car = Model(
                id=item["id"],
                name=item["name"],
                average_price=item["average_price"],
                brand_id=brand.id
            )
            session.add(car)
        session.commit()
        print("Seeding completed succesfully.")


