import pytest
from src.todo_api.squemas.taskSquema import TaskDB
# funções auxiliares-----------------------------

    

# testes Metodo:GET------------------------------
# OBS: os get tem que ser os primeiros, porque eles presisam de um retorno vazio. Isso evita mais operações.
@pytest.mark.anyio
async def teste_api_tarefas_retorna_vazio_quando_vazio(client):
    res=await client.get("/tarefas/")
    print(res.json()['dados'])
    assert res.json()['dados']==[]

# esse teste engloba:
# Se a API retorna todas as tarefas cadastradas.
# Se a quantidade de tarefas retornadas corresponde à quantidade de tarefas cadastradas.
@pytest.mark.anyio
async def teste_api_retorna_todas_tarefas_cadastradas(client,popular_database):
    res=await client.get("/tarefas/")
    assert len(res.json()["dados"])==3# o popular_database retorna sempre 3


@pytest.mark.anyio
async def teste_response_respeita_modelo(client,popular_database):
    res=await client.get("/tarefas/")
    task=TaskDB.model_validate(res.json()["dados"][0])



# testes Metodo:GET- com id------------------------------

# esse teste engloba:
# Se é possível consultar uma tarefa existente pelo identificador.
# Se a tarefa retornada possui os dados corretos.
@pytest.mark.anyio
async def teste_api_retorna_pelo_id_tarefa_persistida(client,popular_database):
    res=await client.get(f"/tarefas/{1}")

    #validar consulta
    assert res.status_code==200

    #validar response
    TaskDB.model_validate(res.json())

@pytest.mark.anyio
async def teste_erro_tarefa_inexistente(client,popular_database):
    res=await client.get(f"/tarefas/{99}")
    #validar consulta
    assert res.status_code==404

# testes Metodo:POST------------------------------
@pytest.mark.anyio
async def teste_criar_tarefa_codigo_retorna_201(client,task):
    response= await client.post("/tarefas/",json=task)
    assert response.status_code==201,"Código errado"
@pytest.mark.anyio
async def teste_validar_response_json_tarefas(task,client):
    res=await client.post("/tarefas/",json=task)
    task=TaskDB.model_validate(res.json())

    #testes especificos- validação da estrutura do response
    assert task.id
    assert task.concluida==False
    assert task.data_atualizacao
    assert task.data_criacao

@pytest.mark.anyio
async def teste_Erro_titulo_vazio(client,task):
    task_Notitle=task
    task_Notitle["titulo"]=None
    res=await client.post("/tarefas/",json=task_Notitle)
    assert res.status_code==422



# testes Metodo:PUT------------------------------



