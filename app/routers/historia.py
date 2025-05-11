from fastapi import APIRouter
router = APIRouter()

@router.get("/historia")
def get_historia():
    return {
        "historia": "Nossa história",
        "conteudo": "A Associação Vem Sonhar foi fundada com o propósito de unir e fortalecer a comunidade surda..."
    }