from fastapi import APIRouter
router = APIRouter()

@router.get("/estatuto")
def get_estatuto():
    return {
        "titulo": "Estatuto da Associação Vem Sonhar",
        "conteudo": "Este é o estatuto oficial da associação Vem Sonhar. Aqui constam os direitos, deveres, finalidades e organização interna..."
    }