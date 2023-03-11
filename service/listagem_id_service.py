from repository import listagem_id_repository
from fastapi import HTTPException


def listagem_id_service(pk: str):
    response = listagem_id_repository(pk)

    if response is None:
        raise HTTPException(500)
    
    if response:
        return response
    
    raise HTTPException(
        404,
        detail='Id não encontrado!'
    )
