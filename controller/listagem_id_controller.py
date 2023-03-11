from service import listagem_id_service
from fastapi import status
from .router import router


@router.get('/{pk}', status_code=status.HTTP_200_OK)
def listagem_id_controller(pk: str):
    return listagem_id_service(pk)
