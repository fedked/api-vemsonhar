from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Membro(BaseModel):
    id: int
    nome: str
    cargo: str
    descricao: str

# Lista de dexemplo (simulando um banco de dados)
membros_db: List[Membro] = [
    Membro(id=1, nome="João Silva", cargo="Presidente", descricao="Responsável geral pela associação."),
    Membro(id=2, nome="Maria Souza", cargo="Vice-presidente", descricao="Auxilia o presidente e substitui quando necessário."),
    Membro(id=3, nome="Carlos Lima", cargo="Tesoureiro", descricao="Cuida da parte financeira.")
]

@router.get("/membros", response_model=List[Membro])
def listar_membros():
    return membros_db

@router.get("/membros/{membros_id}", response_model=Membro)
def obter_membro(id: int):
    for membro in membros_db:
        if membro.id == id:
            return membro
    raise HTTPException(status_code=404, detail="Membro não encontrado")