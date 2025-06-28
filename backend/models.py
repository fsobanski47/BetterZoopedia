from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, ARRAY
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

class InteractivityEnum(enum.Enum):
    exhibit = "exhibit"
    habitat = "habitat"

class EditionEnum(enum.Enum):
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

class IUCNStatusEnum(enum.Enum):
    domesticated = "domesticated"
    least_concern = "least concern"
    near_threatened = "near threatened"
    vulnerable = "vulnerable"
    endangered = "endangered"
    critically_endangered = "critically endangered"
    extinct_in_the_wild = "extinct in the wild"

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    latin_name = Column(String, nullable=False)

    zoopedia_description = relationship("ZoopediaDescription", back_populates="animal", uselist=False)
    gameplay = relationship("Gameplay", back_populates="animal", uselist=False)
    origins = relationship("Origins", back_populates="animal", uselist=False)
    habitat = relationship("Habitat", back_populates="animal", uselist=False)
    social = relationship("Social", back_populates="animal", uselist=False)
    reproduction = relationship("Reproduction", back_populates="animal", uselist=False)

class ZoopediaDescription(Base):
    __tablename__ = "zoopedia_descriptions"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    population_in_the_wild = Column(String)
    general = Column(String)
    social = Column(String)
    reproduction = Column(String)

    animal = relationship("Animal", back_populates="zoopedia_description")

class Gameplay(Base):
    __tablename__ = "gameplay"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    interactivity = Column(Enum(InteractivityEnum))
    edition = Column(Enum(EditionEnum))

    animal = relationship("Animal", back_populates="gameplay")

class Origins(Base):
    __tablename__ = "origins"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    continents = Column(ARRAY(String))
    regions = Column(ARRAY(String))
    iucn_status = Column(Enum(IUCNStatusEnum))

    animal = relationship("Animal", back_populates="origins")

class Habitat(Base):
    __tablename__ = "habitat"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    fence_grade = Column(Integer)
    fence_height = Column(String)
    land_area = Column(Float)
    climbing_area = Column(Float)
    water_area = Column(Float)
    temperature_lower_bound = Column(Float)
    temperature_upper_bound = Column(Float)
    biomes = Column(ARRAY(String))

    animal = relationship("Animal", back_populates="habitat")

class Social(Base):
    __tablename__ = "social"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    group_size_lower_bound = Column(Integer)
    group_size_upper_bound = Column(Integer)
    group_size_upper_bound_male = Column(Integer)
    group_size_upper_bound_female = Column(Integer)
    male_group_size_lower_bound = Column(Integer)
    male_group_size_upper_bound = Column(Integer)
    female_group_size_lower_bound = Column(Integer)
    female_group_size_upper_bound = Column(Integer)

    animal = relationship("Animal", back_populates="social")

class Reproduction(Base):
    __tablename__ = "reproduction"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    difficulty = Column(String)
    maturity = Column(Float)
    sterility = Column(String)
    gestation = Column(Float)
    interbirth = Column(Float)

    animal = relationship("Animal", back_populates="reproduction")