from repository import criar_repository
from model.dto import CriarDTO
from fastapi import HTTPException


def criar_service(criar: CriarDTO):
    dados = criar.__dict__

    dados.update({
        'title': criar.title,
        'price': criar.price,
        'description': criar.price,
        'image': criar.image,
        'category': criar.category
    })
    
    response = criar_repository(dados)

    if response:
        return response
    
    raise HTTPException(500)
