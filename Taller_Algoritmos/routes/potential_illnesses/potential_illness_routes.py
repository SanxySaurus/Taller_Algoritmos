from flask import Blueprint, request
from routes.potential_illnesses import potential_illness_controller

potential_illness_bp = Blueprint("potential_illness_bp", __name__)


@potential_illness_bp.route("/getAll", methods=["GET"])
def getAll():
    return potential_illness_controller.getALL()

@potential_illness_bp.route("/create", methods=["POST"])
def createPotentialIllness():
    data = request.json
    return potential_illness_controller.createPotentialIllness(data)

@potential_illness_bp.route("/delete/<int:id>", methods=["DELETE"])
def deletePotentialIllness(id):
    return potential_illness_controller.deletePotentialIllness(id)

@potential_illness_bp.route('/update/<int:id>', methods=["PUT"])
def update_potential_illness(id):
    data = request.get_json()
    return potential_illness_controller.update_potential_illness(id, data)