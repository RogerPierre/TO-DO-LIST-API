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
async def teste_api_response_respeita_modelo(client,popular_database):
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
async def teste_api_erro_tarefa_inexistente(client,popular_database):
    res=await client.get(f"/tarefas/{99}")
    #validar consulta
    assert res.status_code==404

# testes Metodo:POST------------------------------
@pytest.mark.anyio
async def teste_api_criar_tarefa_codigo_retorna_201(client,task):
    response= await client.post("/tarefas/",json=task)
    assert response.status_code==201,"Código errado"
@pytest.mark.anyio
async def teste_api_validar_response_json_tarefas(task,client):
    res=await client.post("/tarefas/",json=task)
    task=TaskDB.model_validate(res.json())

    #testes especificos- validação da estrutura do response
    assert task.id
    assert task.concluida==False
    assert task.data_atualizacao
    assert task.data_criacao

@pytest.mark.anyio
async def teste_api_Erro_titulo_vazio(client,task):
    task_Notitle=task
    task_Notitle["titulo"]=None
    res=await client.post("/tarefas/",json=task_Notitle)
    assert res.status_code==422



# testes Metodo:PUT------------------------------

@pytest.mark.anyio
async def teste_api_atualizar_titulo_tarefa(client,popular_database,task):
    task_title_changed=task
    task_title_changed["titulo"]="Estudar POI"
    resGet=await client.get(f"/tarefas/{1}")
    resPut=await client.put(f"/tarefas/{1}",json=task_title_changed)
    assert resPut.json()["titulo"]!=resGet.json()["titulo"]
@pytest.mark.anyio
async def teste_api_atualizar_tarefa_conclusao_true(client,popular_database,task):
    task_concluida_changed=task
    task_concluida_changed["concluida"]=not task['concluida']
    resGet=await client.get(f"/tarefas/{1}")
    resPut=await client.put(f"/tarefas/{1}",json=task_concluida_changed)
    assert resPut.json()["concluida"] is not resGet.json()['concluida']
@pytest.mark.anyio
async def teste_api_atualizar_tarefa_tags(client,popular_database,task):
    task_tags_changed=task
    task_tags_changed["tags"][0]=task_tags_changed['tags'][1]
    resGet=await client.get(f"/tarefas/{1}")
    resPut=await client.put(f"/tarefas/{1}",json=task_tags_changed)
    assert resPut.json()["tags"][0]!=resGet.json()["tags"][0]

@pytest.mark.anyio
async def teste_api_atualizar_tarefa_data_atualizacao(client,popular_database,task):
    resGet=await client.get(f"/tarefas/{1}")
    resPut=await client.put(f"/tarefas/{1}",json=task)
    assert resPut.json()["data_atualizacao"]!=resGet.json()["data_atualizacao"]
@pytest.mark.anyio
async def teste_api_atualizar_tarefa_data_criacao(client,popular_database,task):
    resGet=await client.get(f"/tarefas/{1}")
    resPut=await client.put(f"/tarefas/{1}",json=task)
    assert resPut.json()["data_criacao"]==resGet.json()["data_criacao"]
@pytest.mark.anyio
async def teste_api_erro_atualizar_tarefa_inexistente(client,popular_database,task):
    res=await client.put(f"/tarefas/{99}",json=task)
    #validar consulta
    assert res.status_code==404


# testes Metodo:DELETE------------------------------

# esse teste engloba:
# Se é possível excluir uma tarefa existente.
# Se a resposta possui o código HTTP apropriado, como 204 No Content.
@pytest.mark.anyio
async def teste_api_exclusao_tarefa_existente(client,popular_database):
    #deleta
    res=await client.delete(f"/tarefas/{1}")
    assert res.status_code==204

@pytest.mark.anyio
async def teste_api_tarefa_existente_excluida_aparece_lista(client,popular_database):
    #verificar se a tarefa existe
    res_get_f= await client.get(f"/tarefas/")
    assert res_get_f.json()['dados'][0]['id']==1

    #deleta
    await client.delete(f"/tarefas/{1}")

    #verificar se a tarefa nao existe
    res_get_l= await client.get(f"/tarefas/")
    assert res_get_l.json()['dados'][0]['id']!=1
@pytest.mark.anyio
async def teste_api_exclusao_codigo_404(client,popular_database):
    #verificar se a tarefa existe
    res_get_f= await client.get(f"/tarefas/{1}")
    assert res_get_f.status_code==200

    #deleta
    await client.delete(f"/tarefas/{1}")

    #verificar se a tarefa nao existe
    res_get_l= await client.get(f"/tarefas/{1}")
    assert res_get_l.status_code==404

@pytest.mark.anyio
async def teste_api_exclusao_tarefa_inexistente_retorna_404(client,popular_database):
    #deleta
    res=await client.delete(f"/tarefas/{99}")
    assert res.status_code==404