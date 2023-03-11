from service import listagem_service
from .router import router
from fastapi import status


# Rotas
@router.get('', status_code=status.HTTP_200_OK)
def listagem_controller():
    return listagem_service()