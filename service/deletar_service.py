from repository import deletar_repository
from fastapi import HTTPException


def deletar_service(pk):
    reponse = deletar_repository(pk)

    if reponse is None:
        return HTTPException(500)
    
    if reponse:
        return
    
    raise HTTPException(
        404, 
        detail='Id não encontrado'
    )
