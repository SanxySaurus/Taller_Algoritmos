from typing import List, Tuple, Any
from contextlib import contextmanager
from db.db import SessionLocal
from db.models import  potential_illness

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getAll() -> Tuple[List[potential_illness], Any]:
    try:
        with get_db() as db:
            illnesses = db.query(potential_illness).all()
            return illnesses, None
    except Exception as e:
        return None, str(e)

def createPotentialIllness(data) -> Tuple[potential_illness, Any]:
    try:
        with get_db() as db:
            illness = potential_illness(
                name=data.get("name")
            )
            db.add(illness)
            db.commit()
            db.refresh(illness)
            return illness, None
    except Exception as e:
        return None, str(e)

def deletePotentialIllness(id: int):
    try:
        with get_db() as db:
            illness_exist = db.query(potential_illness).filter(potential_illness.id == id).first()

            if not illness_exist:
                return False, "Potential illness not found"

            db.delete(illness_exist)
            db.commit()
            return True, None
    except Exception as e:
        return False, str(e)

def updatePotentialIllness(id: int, data):
    try:
        with get_db() as db:
            illness = db.query(potential_illness).filter(potential_illness.id == id).first()

            if not illness:
                return None, "Potential illness not found"

            illness.name = data.get("name")

            db.commit()
            db.refresh(illness)
            return illness, None
    except Exception as e:
        return None, str(e)