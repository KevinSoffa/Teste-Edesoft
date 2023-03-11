from repository import listagem_repository
from fastapi import HTTPException


def listagem_service():

    respose = listagem_repository()

    lista = []

    for r in respose:
        lista.append(r)

    if respose:
        return {
            "response": lista
        }
    
    print(respose)
    
    raise HTTPException(
        status_code=404
    )
