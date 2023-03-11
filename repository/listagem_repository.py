from requests import request
from decouple import config


# Requisação na API
def listagem_repository():

    listagem = request(
        'GET',
        '%s/' % (
            config('URL_GET_ALL_PRODUTOS')
        ),
        headers={
            'Content-Type': 'application/json'
        }
    )

    response = listagem.json()
    print(response)
    
    
    return response