from typing import List, Tuple, Any
from contextlib import contextmanager
from db.db import SessionLocal
from db.models import family

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getAll() -> Tuple[List[family], Any]:
    try:
        with get_db() as db:
            families = db.query(family).all()
            return families, None
    except Exception as e:
        return None, str(e)

def createFamilyGroup(data) -> Tuple[Any, Any]:
    try:
        with get_db() as db:

            
            if isinstance(data, dict):
                data = [data]

            created_families = []

            for item in data:
                fam = family(
                    name=item.get("name"),
                    potential_illness_id=item.get("potential_illness_id")
                )

                db.add(fam)
                created_families.append(fam)

            db.commit()

            
            for fam in created_families:
                db.refresh(fam)

            return created_families, None

    except Exception as e:
        return None, str(e)

def deleteFamilyGroup(id: int):
    try:
        with get_db() as db:
            family_exist = db.query(family).filter(family.id == id).first()

            if not family_exist:
                return False, "Family group not found"

            db.delete(family_exist)
            db.commit()
            return True, None
    except Exception as e:
        return False, str(e)

def deleteFamilyGroup(id: int):
    try:
        with get_db() as db:
            family_exist = db.query(family).filter(family.id == id).first()

            if not family_exist:
                return False, "Family group not found"

            db.delete(family_exist)
            db.commit()
            return True, None
    except Exception as e:
        return False, str(e)

def updateFamilyGroup(id: int, data):
    try:
        with get_db() as db:
            families = db.query(family).filter(family.id == id).first()

            if not family:
                return None, "Family group not found"

            if "name" in data:
                families.name = data.get("name")
            if "potential_illness_id" in data:
                families.potential_illness_id = data.get("potential_illness_id")

            db.commit()
            db.refresh(families)
            return families, None
    except Exception as e:
        return None, str(e)