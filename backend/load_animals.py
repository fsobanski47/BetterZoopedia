import os
import json
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

DATA_DIR = "./data/animals"

def load_animals():
    db: Session = SessionLocal()
    try:
        for filename in sorted(os.listdir(DATA_DIR)):
            if filename.endswith(".json"):
                filepath = os.path.join(DATA_DIR, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                animal_create = schemas.AnimalCreate(**data)
                crud.create_animal(db=db, animal=animal_create)
                print(f"Loaded {filename}")
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error: ", e)
    finally:
        db.close()

if __name__ == "__main__":
    load_animals()