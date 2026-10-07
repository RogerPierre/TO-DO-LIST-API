import pytest
from httpx import ASGITransport, AsyncClient
from todo_api.repository.InMemoryDB import db
from main import app

@pytest.fixture(autouse=True)
def limpar_db():
    db.clear()
@pytest.fixture
async def popular_database(client,task):
    tarefas = [
        {**task, "titulo": "Estudar Python", "descricao": "Revisar conceitos básicos", "tags": ["python", "estudo"], "concluida": False},
        {**task, "titulo": "Fazer exercícios", "descricao": "Praticar programação", "tags": ["exercicios", "programacao"], "concluida": False},
        {**task, "titulo": "Organizar projetos", "descricao": "Atualizar tarefas pendentes", "tags": ["organizacao", "projetos"], "concluida": True},
    ]
    for tarefa in tarefas:
        await client.post("/tarefas/", json=tarefa)
@pytest.fixture
async def client():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://127.0.0.1:8000"
    ) as client:
        yield client
@pytest.fixture
def task():
    return {"titulo": "Estudar PPI",
                "descricao": "Revisar bibliotecas e comandos",
                "tags": ["python", "estudo","PPI"],
                "concluida":True
                }