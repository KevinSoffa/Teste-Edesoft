from requests import request


def deletar_repository(pk: str):
    deletar = request(
        'DELETE',
        'https://fakestoreapi.com/products/' + pk,
        headers={
            'Content-Type': 'application/json'
        }
    )

    resposta = deletar.json()

    return resposta
