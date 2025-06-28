from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class InteractivityEnum(str, Enum):
    exhibit = "exhibit"
    habitat = "habitat"


class EditionEnum(str, Enum):
    standard = "standard"
    deluxe = "deluxe"
    dlc1 = "dlc1"
    dlc2 = "dlc2"
    dlc3 = "dlc3"
    dlc4 = "dlc4"
    dlc5 = "dlc5"
    dlc6 = "dlc6"
    dlc7 = "dlc7"
    dlc8 = "dlc8"
    dlc9 = "dlc9"
    dlc10 = "dlc10"
    dlc11 = "dlc11"
    dlc12 = "dlc12"
    dlc13 = "dlc13"
    dlc14 = "dlc14"
    dlc15 = "dlc15"
    dlc16 = "dlc16"
    dlc17 = "dlc17"
    dlc18 = "dlc18"
    dlc19 = "dlc19"
    dlc20 = "dlc20"


class IUCNStatusEnum(str, Enum):
    domesticated = "domesticated"
    least_concern = "least concern"
    near_threatened = "near threatened"
    vulnerable = "vulnerable"
    endangered = "endangered"
    critically_endangered = "critically endangered"
    extinct_in_the_wild = "extinct in the wild"


class ZoopediaDescriptionBase(BaseModel):
    population_in_the_wild: Optional[str]
    general: Optional[str]
    social: Optional[str]
    reproduction: Optional[str]


class ZoopediaDescriptionCreate(ZoopediaDescriptionBase):
    pass


class ZoopediaDescriptionRead(ZoopediaDescriptionBase):
    id: int

    class Config:
        orm_mode = True


class GameplayBase(BaseModel):
    interactivity: Optional[InteractivityEnum]
    edition: Optional[EditionEnum]


class GameplayCreate(GameplayBase):
    pass


class GameplayRead(GameplayBase):
    id: int

    class Config:
        orm_mode = True


class OriginsBase(BaseModel):
    continents: Optional[List[str]]
    regions: Optional[List[str]]
    iucn_status: Optional[IUCNStatusEnum]


class OriginsCreate(OriginsBase):
    pass


class OriginsRead(OriginsBase):
    id: int

    class Config:
        orm_mode = True


class HabitatBase(BaseModel):
    fence_grade: Optional[int]
    fence_height: Optional[str]
    land_area: Optional[float]
    climbing_area: Optional[float]
    water_area: Optional[float]
    temperature_lower_bound: Optional[float]
    temperature_upper_bound: Optional[float]
    biomes: Optional[List[str]]


class HabitatCreate(HabitatBase):
    pass


class HabitatRead(HabitatBase):
    id: int

    class Config:
        orm_mode = True


class SocialBase(BaseModel):
    group_size_lower_bound: Optional[int]
    group_size_upper_bound: Optional[int]
    group_size_upper_bound_male: Optional[int]
    group_size_upper_bound_female: Optional[int]
    male_group_size_lower_bound: Optional[int]
    male_group_size_upper_bound: Optional[int]
    female_group_size_lower_bound: Optional[int]
    female_group_size_upper_bound: Optional[int]


class SocialCreate(SocialBase):
    pass


class SocialRead(SocialBase):
    id: int

    class Config:
        orm_mode = True


class ReproductionBase(BaseModel):
    difficulty: Optional[str]
    maturity: Optional[float]
    sterility: Optional[str]
    gestation: Optional[float]
    interbirth: Optional[float]


class ReproductionCreate(ReproductionBase):
    pass


class ReproductionRead(ReproductionBase):
    id: int

    class Config:
        orm_mode = True


class AnimalBase(BaseModel):
    name: str
    latin_name: str


class AnimalCreate(AnimalBase):
    zoopedia_description: ZoopediaDescriptionCreate
    gameplay: GameplayCreate
    origins: OriginsCreate
    habitat: HabitatCreate
    social: SocialCreate
    reproduction: ReproductionCreate


class AnimalRead(AnimalBase):
    id: int
    zoopedia_description: Optional[ZoopediaDescriptionRead]
    gameplay: Optional[GameplayRead]
    origins: Optional[OriginsRead]
    habitat: Optional[HabitatRead]
    social: Optional[SocialRead]
    reproduction: Optional[ReproductionRead]

    class Config:
        orm_mode = True