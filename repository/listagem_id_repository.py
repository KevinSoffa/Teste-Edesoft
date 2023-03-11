from requests import request
from fastapi import HTTPException

def listagem_id_repository(pk: str):
    listagem = request(
        'GET',
        'https://fakestoreapi.com/products/' + pk,
         headers={
            'Content-Type': 'application/json'
        }
    )

    print(listagem)

    reposta = listagem.json()

    return reposta
