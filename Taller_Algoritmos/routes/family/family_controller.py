from flask import request

from common.http import ok, bad_request
from routes.family import family_service


def getALL():
    data, error = family_service.getAll()
    if error:
        return bad_request(
            message="No se pudieron obtener los grupos familiares",
            errors=error
        )
    return ok(
        data=[d.to_dict() for d in data],
        message="Grupos familiares obtenidos con éxito"
    )

def createFamilyGroup(data):
    result, error = family_service.createFamilyGroup(request.get_json())
    if error:
        return bad_request(
            message="Error creando grupo familiar",
            errors=error
        )
    return ok(
        data=[r.to_dict() for r in result],
        message="Grupo familiar creado correctamente"
    )

def deleteFamilyGroup(id):
    result, err = family_service.deleteFamilyGroup(id)
    if err:
        return bad_request(
            message="Error eliminando grupo familiar", 
            errors=err
        )

    return ok(
        data={"delete": result},
        message=f"Grupo familiar con id {id} eliminado exitosamente"
    )

def update_family_group(id: int, data):
    result, err = family_service.updateFamilyGroup(id, data)
    if err:
        return bad_request(
            message="Error actualizando grupo familiar",
            errors=err
        )

    return ok(
        data={"update": result.to_dict()},
        message=f"Grupo familiar con id {id} actualizado exitosamente"
    )