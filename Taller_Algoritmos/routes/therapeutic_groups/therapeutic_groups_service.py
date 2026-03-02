from typing import Any, Dict, List, Tuple, Optional

from sqlalchemy.exc import IntegrityError

from db.session import get_db
from db.models import therapeutic_groups


def get_all() -> Tuple[List[therapeutic_groups], Any]:
    with get_db() as db:
        return db.query(therapeutic_groups).order_by(therapeutic_groups.id).all(), None


def get_by_id(item_id: int) -> Tuple[Optional[therapeutic_groups], Any]:
    with get_db() as db:
        return db.query(therapeutic_groups).get(item_id), None


def create(data: Dict[str, Any]) -> Tuple[Optional[therapeutic_groups], Any]:
    name = (data.get("name") or "").strip()
    if not name:
        return None, {"name": "is required"}
    with get_db() as db:
        try:
            obj = therapeutic_groups(name=name)
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj, None
        except IntegrityError as e:
            db.rollback()
            return None, str(e.orig)


def update(item_id: int, data: Dict[str, Any]) -> Tuple[Optional[therapeutic_groups], Any]:
    with get_db() as db:
        obj = db.query(therapeutic_groups).get(item_id)
        if not obj:
            return None, "not_found"
        if "name" in data:
            value = (data.get("name") or "").strip()
            if not value:
                return None, {"name": "cannot be empty"}
            obj.name = value
        try:
            db.commit()
            db.refresh(obj)
            return obj, None
        except IntegrityError as e:
            db.rollback()
            return None, str(e.orig)


def delete(item_id: int) -> Tuple[bool, Any]:
    with get_db() as db:
        obj = db.query(therapeutic_groups).get(item_id)
        if not obj:
            return False, "not_found"
        try:
            db.delete(obj)
            db.commit()
            return True, None
        except IntegrityError as e:
            db.rollback()
            return False, str(e.orig)