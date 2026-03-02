from common.http import ok, bad_request
from routes.potential_illnesses import potential_illness_service

def getALL():
    data, error = potential_illness_service.getAll()
    if error:
        return bad_request(
            message="No se pudieron obtener las enfermedades potenciales",
            errors=error
        )
    return ok(
        data=[d.to_dict() for d in data],
        message="Enfermedades potenciales obtenidas con éxito"
    )

def createPotentialIllness(data):
    result, error = potential_illness_service.createPotentialIllness(data)
    if error:
        return bad_request(
            message="Error creando enfermedad potencial",
            errors=error
        )
    return ok(
        data=result.to_dict(),
        message="Enfermedad potencial creada correctamente"
    )

def deletePotentialIllness(id):
    result, err = potential_illness_service.deletePotentialIllness(id)
    if err:
        return bad_request(
            message="Error eliminando enfermedad potencial", 
            errors=err
        )

    return ok(
        data={"delete": result},
        message=f"Enfermedad potencial con id {id} eliminada exitosamente"
    )

def update_potential_illness(id: int, data):
    result, err = potential_illness_service.updatePotentialIllness(id, data)
    if err:
        return bad_request(
            message="Error actualizando enfermedad potencial",
            errors=err
        )

    return ok(
        data={"update": result.to_dict()},
        message=f"Enfermedad potencial con id {id} actualizada exitosamente"
    )