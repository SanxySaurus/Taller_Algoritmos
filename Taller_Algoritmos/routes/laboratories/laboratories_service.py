from typing import List, Tuple, Any
from contextlib import contextmanager
from db.db import SessionLocal 
from db.models import laboratories

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getAll() -> Tuple[List[laboratories], Any]:
    try:
        with get_db() as db:
            laboratory = db.query(laboratories).all()
            return laboratory, None
    except Exception as e:
        return None, str(e)

def createLaboratories(data) -> Tuple[laboratories, Any]:
    try:
        with get_db() as db:
            laboratory = laboratories(
                name=data.get("name")
            )
            db.add(laboratory)
            db.commit()
            db.refresh(laboratory)
            return laboratory, None
    except Exception as e:
        return None, str(e)

def deleteLaboratories(id: int):
    try:
        with get_db() as db:
            lab_exist = db.query(laboratories).filter(laboratories.id == id).first()

            if not lab_exist:
                return False, "Laboratory not found"

            db.delete(lab_exist)
            db.commit()
            return True, None
    except Exception as e:
        return False, str(e)

def updateLaboratories(id: int, data):
    try:
        with get_db() as db:
            laboratory = db.query(laboratories).filter(laboratories.id == id).first()

            if not laboratory:
                return None, "Laboratory not found"

            laboratory.name = data.get("name")

            db.commit()
            db.refresh(laboratory)
            return laboratory, None
    except Exception as e:
        return None, str(e)