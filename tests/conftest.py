import pytest
from httpx import ASGITransport, AsyncClient
from todo_api.repository.InMemoryDB import db
from main import app

@pytest.fixture(autouse=True)
def limpar_db():
    db.clear()
@pytest.fixture
async def popular_database(client,task):
    await client.post("/tarefas/",json=task)
    await client.post("/tarefas/",json=task)
    await client.post("/tarefas/",json=task)
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
                "concluida":False
                }