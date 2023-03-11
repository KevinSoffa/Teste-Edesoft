from requests import request



def atualizar_repository(pk: str, dto):

    atual = request(
        'PUT',
        'https://fakestoreapi.com/products/' + pk,
        headers={
            'Content-Type': 'application/json'
        },
    )
    print(atual)

    response = atual.json()
    print(response)

    return response
