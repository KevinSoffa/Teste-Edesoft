from service import deletar_service
from .router import router
from fastapi import status


@router.delete('/{pk}', status_code=status.HTTP_200_OK)
def deletar_controller(pk):
    return deletar_service(str(pk))
