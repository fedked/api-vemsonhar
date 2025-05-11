from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
router = APIRouter()

class Contato(BaseModel):
    nome: str
    email: EmailStr
    assunto: str
    mensagem: str

@router.post("/contato")
def enviar_contato(contato: Contato):
    return {
        "mensagem": "Mensagem recebida com sucesso!",
        "dados": contato
    }