from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
router = APIRouter()

# Modelo de post
class Post(BaseModel):
    id: int
    titulo: str
    conteudo: str
    autor: str
    data_criacao: str
    tags: List[str]

# Lista temporária simulando um banco de dados
posts_db: List[Post] = []

@router.get("/posts", response_model=List[Post])
def listar_posts():
    return posts_db

@router.get("/posts/{post_id}", response_model=Post)
def obter_post(id: int):
    for post in posts_db:
        if post.id == id:
            return post
        raise HTTPException(status_code=404, detail="Post não encontrado")
    
@router.post("/posts", response_model=Post)
def criar_post(post: Post):
    posts_db.append(post)
    return post