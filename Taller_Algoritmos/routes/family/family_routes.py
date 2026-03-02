from flask import Blueprint, request
from routes.family import family_controller


family_bp = Blueprint("family_bp", __name__)


@family_bp.route("/getAll", methods=["GET"])
def getAll():
    return family_controller.getALL()

@family_bp.route("/create", methods=["POST"])
def createFamilyGroup():
    data = request.json
    return family_controller.createFamilyGroup(data)


@family_bp.route("/delete/<int:item_id>", methods=["DELETE"])
def deleteFamilyGroup(item_id):
    return family_controller.deleteFamilyGroup(item_id)

@family_bp.route('/update/<int:item_id>', methods=["PUT"])
def update_family_group(item_id):
    data = request.get_json()
    return family_controller.update_family_group(item_id, data)