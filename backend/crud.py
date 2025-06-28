from sqlalchemy.orm import Session
import models, schemas

def create_animal(db: Session, animal: schemas.AnimalCreate):
    db_animal = models.Animal(
        name=animal.name,
        latin_name=animal.latin_name,
    )
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)

    db_zoopedia = models.ZoopediaDescription(
        animal_id=db_animal.id, **animal.zoopedia_description.model_dump()
    )
    db_gameplay = models.Gameplay(
        animal_id=db_animal.id, **animal.gameplay.model_dump()
    )
    db_origins = models.Origins(
        animal_id=db_animal.id, **animal.origins.model_dump()
    )
    db_habitat = models.Habitat(
        animal_id=db_animal.id, **animal.habitat.model_dump()
    )
    db_social = models.Social(
        animal_id=db_animal.id, **animal.social.model_dump()
    )
    db_reproduction = models.Reproduction(
        animal_id=db_animal.id, **animal.reproduction.model_dump()
    )

    db.add_all([db_zoopedia, db_gameplay, db_origins, db_habitat, db_social, db_reproduction])
    db.commit()

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