from requests import request
from decouple import config


def criar_repository(dto):

    criar = request(
        'POST',
        '%s/' % (
            config('URL_POST_PRODUTOS')
        ),
        headers={
            'Content-Type': 'application/json'
        },
    )

    response = criar.json()

    return response