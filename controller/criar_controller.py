from service import criar_service
from model.dto import CriarDTO
from .router import router
from fastapi import status


@router.post('', status_code=status.HTTP_201_CREATED)
def criar_controller(dto: CriarDTO):
    print(dto)
    return criar_service(dto)
