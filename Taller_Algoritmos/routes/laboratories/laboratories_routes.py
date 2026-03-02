from flask import Blueprint, request
from routes.laboratories import laboratories_controller

laboratories_bp = Blueprint("laboratories_bp", __name__)

@laboratories_bp.route("/getAll", methods=["GET"])
def getAll():
    return laboratories_controller.getALL()


@laboratories_bp.route("/create", methods=["POST"])
def createLaboratories():
    data = request.json
    return laboratories_controller.createLaboratory(data)


@laboratories_bp.route("/delete/<int:id>", methods=["DELETE"])
def deleteLaboratories(id):
    return laboratories_controller.deleteLaboratory(id)


@laboratories_bp.route('/update/<int:id>', methods=["PUT"])
def update_laboratories(id):
    data = request.get_json()
    return laboratories_controller.update_laboratory(id, data)