from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class therapeutic_groups(Base):
    __tablename__ = "therapeutic_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class family(Base):
    __tablename__ = "family"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(), nullable=False)
    
    potential_illness_id = Column(Integer, ForeignKey('potential_illness.id'), nullable=True)
    
    potential_illness = relationship("potential_illness", backref="families")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "potential_illness_id": self.potential_illness_id
        }

class laboratories(Base):
    __tablename__ = "laboratories" 
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class potential_illness(Base):
    __tablename__ = "potential_illness"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }