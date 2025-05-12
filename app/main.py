# main.py
from fastapi import FastAPI
from app.routers import historia, contato, posts, estatuto, membros
from app.config.database import Base, engine
from app.models import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(historia.router)
app.include_router(contato.router)
app.include_router(posts.router)
app.include_router(estatuto.router)
app.include_router(membros.router)

@app.get("/")
def home(): 
    return {"mensagem": "API Vem Sonhar funcionando!"}
