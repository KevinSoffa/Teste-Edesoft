from service import atualizar_service
from model.dto import AtualizarDTO
from fastapi import status
from .router import router


@router.put('/{pk}', status_code=status.HTTP_200_OK)
def atualizar_controller(pk: str, atualizar_dto: AtualizarDTO):
    return atualizar_service(pk, atualizar_dto)
