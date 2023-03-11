from repository import atualizar_repository
from model.dto import AtualizarDTO
from fastapi import HTTPException


def atualizar_service(pk: str, dados_dto: AtualizarDTO):
    dados = dados_dto.__dict__

    response = atualizar_repository(
        pk,
        dados
    )

    if response is None:
        return HTTPException(500)
    
    if response:
        return response
    
    raise HTTPException(404)
