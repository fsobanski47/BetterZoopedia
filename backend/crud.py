from sqlalchemy.orm import Session
import models, schemas

def create_animal(db: Session, animal: schemas.AnimalCreate):
    db_animal = models.Animal(**animal.dict())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

def get_animals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Animal).offset(skip).limit(limit).all()

def get_zoopedia_by_animal_id(db: Session, animal_id: int):
    return db.query(models.ZoopediaDescription).filter(models.ZoopediaDescription.animal_id == animal_id).first()

def get_gameplay_by_animal_id(db: Session, animal_id: int):
    return db.query(models.Gameplay).filter(models.Gameplay.animal_id == animal_id).first()

def get_origins_by_animal_id(db: Session, animal_id: int):
    return db.query(models.Origins).filter(models.Origins.animal_id == animal_id).first()

def get_habitat_by_animal_id(db: Session, animal_id: int):
    return db.query(models.Habitat).filter(models.Habitat.animal_id == animal_id).first()

def get_social_by_animal_id(db: Session, animal_id: int):
    return db.query(models.Social).filter(models.Social.animal_id == animal_id).first()

def get_reproduction_by_animal_id(db: Session, animal_id: int):
    return db.query(models.Reproduction).filter(models.Reproduction.animal_id == animal_id).first()

def get_animal_by_id(db: Session, animal_id: int):
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()