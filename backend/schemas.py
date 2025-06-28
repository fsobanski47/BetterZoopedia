from pydantic import BaseModel

class AnimalBase(BaseModel):
    name: str
    species: str
    habitat: str
    lifespan: float

class AnimalCreate(AnimalBase):
    pass

class AnimalRead(AnimalBase):
    id: int

    class Config:
        orm_mode = True