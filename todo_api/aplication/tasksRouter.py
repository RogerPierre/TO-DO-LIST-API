from fastapi import APIRouter,Query
from todo_api import PostTask,GetTaskById,GetTask,DeleteTask,PutTask,TaskSquema
from typing import Annotated
from datetime import date
routerTask=APIRouter()

@routerTask.get("/")
def GetAll(
    concluida:Annotated[bool,
        Query( title="Concluida",
              description="Un valor booleano."
        )
    ]=None,
    tag:Annotated[str,
        Query( title="tag",
                  description="Un valor str."
            )
        ]=None,
    titulo:Annotated[str,
        Query( title="titulo",
            description="Un valor str."
            )
        ]=None,
    ordenar_por:Annotated[str,
        Query( title="campo",
               description="Un valor str."
            )
        ]=None,
    
    ordem:Annotated[str,
        Query( title="ordem",
                description="Pode ser asc ou desc"
            )
        ]="asc",
    pagina:Annotated[int,
                    Query( title="pagina",
                          description="Um valor inteiro"
                    )
                ]=1,
    limite:Annotated[int,
                        Query( title="limite por pagina",
                              description="Um valor inteiro"
                        )
                    ]=10,
    data_inicio:Annotated[date,
                        Query( title="data inicio",
                              description="Um valor do tipo date(datetime)"
                        )
                    ]=None,
    data_fim:Annotated[date,
                        Query( title="data fim",
                              description="Um valor do tipo date(datetime)"
                        )
                    ]=None
    
):
    return GetTask(concluida=concluida,
                   tag=tag,titulo=titulo,
                   ordenar_por=ordenar_por,
                   ordem=ordem,
                   pagina=pagina,
                   limite=limite,
                   data_inicio=data_inicio,
                   data_fim=data_fim
                )

@routerTask.get("/{id}")
def GetById(id:int):
    return GetTaskById(id)

@routerTask.post("/")
def Post(task:TaskSquema):
    PostTask(task)
    return task

@routerTask.put("/{id}")
def Put(id:int,Task:TaskSquema):
    return PutTask(id=id,task=Task)

@routerTask.delete("/{id}",status_code=204)
def Delete(id:int):
    DeleteTask(id=id)