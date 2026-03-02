from common.http import ok, bad_request
from routes.laboratories import laboratories_service

def getALL():
    data, error = laboratories_service.getAll()
    if error:
        return bad_request(
            message="No se pudieron obtener los laboratorios",
            errors=error
        )
    return ok(
        data=[d.to_dict() for d in data],
        message="Laboratorios obtenidos con éxito"
    )

def createLaboratory(data):
    result, error = laboratories_service.createLaboratories(data)
    if error:
        return bad_request(
            message="Error creando laboratorio",
            errors=error
        )
    return ok(
        data=result.to_dict(),
        message="Laboratorio creado correctamente"
    )

def deleteLaboratory(id):
    result, err = laboratories_service.deleteLaboratories(id)
    if err:
        return bad_request(
            message="Error eliminando laboratorio", 
            errors=err
        )

    return ok(
        data={"delete": result},
        message=f"Laboratorio con id {id} eliminado exitosamente"
    )

def update_laboratory(id: int, data):
    result, err = laboratories_service.updateLaboratories(id, data)
    if err:
        return bad_request(
            message="Error actualizando laboratorio",
            errors=err
        )

    return ok(
        data={"update": result.to_dict()},
        message=f"Laboratorio con id {id} actualizado exitosamente"
    )
