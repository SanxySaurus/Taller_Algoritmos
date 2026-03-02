from common.http import ok, bad_request, created, not_found
from routes.therapeutic_groups import therapeutic_groups_service


def get_all():
    data, err = therapeutic_groups_service.get_all()
    if err:
        return bad_request(message="No se pudo obtener Grupos Terapeuticos", errors=err)
    return ok(data=[d.to_dict() for d in data], message=" Grupos Terapeuticos obtenidos con éxito")

def create(data):
    obj, err = therapeutic_groups_service.create(data)
    if err:
        return bad_request(message="Error creando Grupo Terapeutico", errors=err)
    return created(data=obj.to_dict(), message="Grupo Terapeutico creado con éxito")


def update(item_id: int, data):
    obj, err = therapeutic_groups_service.update(item_id, data)
    if err == "not_found":
        return not_found(message="Grupo Terapeutico no encontrado")
    if err:
        return bad_request(message="Error actualizando Grupo Terapeutico", errors=err)
    return ok(data=obj.to_dict(), message="Grupo Terapeutico actualizado con éxito")


def delete(item_id: int):
    ok_delete, err = therapeutic_groups_service.delete(item_id)
    if err == "not_found":
        return not_found(message="Grupo Terapeutico no encontrado")
    if err:
        return bad_request(message="Error eliminando Grupo Terapeutico", errors=err)
    return ok(data={"deleted": ok_delete}, message="Grupo Terapeutico eliminado con éxito")