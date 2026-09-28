import pytest
@pytest.mark.anyio
async def test_criar_task(tasks,client):
    for task in tasks:  
        response = await client.post("/tarefas/",json=task)
        print(response.json())
        assert response.status_code == 201
        assert response.json()["titulo"] != "","titulo nâo pode ser vazio"
        assert response.json()["descricao"] != "","descricao nâo pode ser vazio"
        assert response.json()["tags"] != [],"tags nâo podem ser vazias"
        assert response.json()["data_criacao"] != "","data_cricao nâo pode ser vazia"
        assert response.json()["data_atualizacao"] != "","data_atualizacao nâo pode ser vazia"
        assert response.json()["concluida"] == False,"concluida nâo pode ser true"
        assert isinstance(response.json()["id"],int),"id nao pode ser vazio"
