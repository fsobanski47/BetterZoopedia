from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/animals/", response_model=schemas.AnimalRead)
def create_animal(animal: schemas.AnimalCreate, db: Session = Depends(get_db)):
    return crud.create_animal(db=db, animal=animal)

@app.get("/animals/", response_model=list[schemas.AnimalRead])
def read_animals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_animals(db=db, skip=skip, limit=limit)

@app.get("/animals/names/", response_model=list[str])
def read_animal_names(db: Session = Depends(get_db)):
    animals = crud.get_animals(db=db)
    return [animal.name for animal in animals]

@app.get("/animals/{name}", response_model=schemas.AnimalRead)
def read_animal_by_name(name: str, db: Session = Depends(get_db)):
    animal = crud.get_animal_by_name(db=db, name=name)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal

@app.get("/animals/{name}/attributes/{attribute_name}")
def read_animal_attribute(name: str, attribute_name: str, db: Session = Depends(get_db)):
    animal = crud.get_animal_by_name(db=db, name=name)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    if not hasattr(animal, attribute_name):
        raise HTTPException(status_code=404, detail="Attribute not found")
    return {attribute_name: getattr(animal, attribute_name)}