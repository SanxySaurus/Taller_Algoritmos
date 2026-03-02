from flask import Blueprint, request
from routes.therapeutic_groups import therapeutic_groups_controller

therapeutic_groups_bp = Blueprint("therapeutic_groups_bp", __name__)

@therapeutic_groups_bp.route("/getAll", methods=["GET"])
def get_all():
    return therapeutic_groups_controller.get_all()

@therapeutic_groups_bp.route("/create", methods=["POST"])
def create():
    return therapeutic_groups_controller.create(request.get_json() or {})

@therapeutic_groups_bp.route("/update/<int:item_id>", methods=["PUT", "PATCH"])
def update(item_id: int):
    return therapeutic_groups_controller.update(item_id, request.get_json() or {})

@therapeutic_groups_bp.route("/delete/<int:item_id>", methods=["DELETE"])
def delete(item_id: int):
    return therapeutic_groups_controller.delete(item_id)