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

@app.get("/animals/id/{name}")
def get_animal_id_by_name(name: str, db: Session = Depends(get_db)):
    animal = crud.get_animal_by_name(db=db, name=name)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return {"id": animal.id}

@app.get("/animals/{animal_id}", response_model=schemas.AnimalRead)
def read_animal_by_id(animal_id: int, db: Session = Depends(get_db)):
    animal = crud.get_animal_by_id(db=db, animal_id=animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal

@app.get("/zoopedia/{animal_id}", response_model=schemas.ZoopediaDescriptionRead)
def read_zoopedia(animal_id: int, db: Session = Depends(get_db)):
    zoopedia = crud.get_zoopedia_by_animal_id(db=db, animal_id=animal_id)
    if not zoopedia:
        raise HTTPException(status_code=404, detail="Zoopedia description not found")
    return zoopedia

@app.get("/gameplay/{animal_id}", response_model=schemas.GameplayRead)
def read_gameplay(animal_id: int, db: Session = Depends(get_db)):
    gameplay = crud.get_gameplay_by_animal_id(db=db, animal_id=animal_id)
    if not gameplay:
        raise HTTPException(status_code=404, detail="Gameplay data not found")
    return gameplay

@app.get("/origins/{animal_id}", response_model=schemas.OriginsRead)
def read_origins(animal_id: int, db: Session = Depends(get_db)):
    origins = crud.get_origins_by_animal_id(db=db, animal_id=animal_id)
    if not origins:
        raise HTTPException(status_code=404, detail="Origins data not found")
    return origins

@app.get("/habitat/{animal_id}", response_model=schemas.HabitatRead)
def read_habitat(animal_id: int, db: Session = Depends(get_db)):
    habitat = crud.get_habitat_by_animal_id(db=db, animal_id=animal_id)
    if not habitat:
        raise HTTPException(status_code=404, detail="Habitat data not found")
    return habitat

@app.get("/social/{animal_id}", response_model=schemas.SocialRead)
def read_social(animal_id: int, db: Session = Depends(get_db)):
    social = crud.get_social_by_animal_id(db=db, animal_id=animal_id)
    if not social:
        raise HTTPException(status_code=404, detail="Social data not found")
    return social

@app.get("/reproduction/{animal_id}", response_model=schemas.ReproductionRead)
def read_reproduction(animal_id: int, db: Session = Depends(get_db)):
    reproduction = crud.get_reproduction_by_animal_id(db=db, animal_id=animal_id)
    if not reproduction:
        raise HTTPException(status_code=404, detail="Reproduction data not found")
    return reproduction