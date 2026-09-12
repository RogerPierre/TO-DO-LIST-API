from todo_api.repository.InMemoryDB import db
from fastapi import HTTPException
from datetime import date,datetime
def Includes(lista:list[str],tag:str):
        for tg in lista:
            if tg==tag:
                   return True

            else:
                return False

def GetTask(
        concluida:bool|None,
        tag:str|None,
        titulo:str|None,
        ordenar_por:str|None,
        ordem:str,
        pagina:int,
        limite:int,
        data_inicio:date|None,
        data_fim:date|None
):
    listaResultado=db
    
    
    for i,u in enumerate(listaResultado):
        if concluida is not None:
            listaResultado=[
                task for task in listaResultado
                if u.concluida is concluida
                ]
        if tag is not None:
            listaResultado=[
                task for task in listaResultado
                    if Includes(lista=task.tags,tag=tag)
                ]
        if titulo is not None:
            listaResultado=[
                task for task in listaResultado
                    if task.titulo==titulo
                ]
        if ordenar_por is not None:
            if ordenar_por == "id":
                listaResultado=sorted( listaResultado,key=lambda task:task.id,reverse=ordem=="desc")
            elif ordenar_por == "titulo":
                listaResultado=sorted( listaResultado,key=lambda task:task.titulo,reverse=ordem=="desc")
            elif ordenar_por == "data_criacao":
                listaResultado=sorted( listaResultado,key=lambda task:task.data_criacao,reverse=ordem=="desc")
            elif ordenar_por == "data_atualizacao":
                listaResultado=[
                     task for task in listaResultado
                     if task.data_atualizacao is not None
                ]
                listaResultado=sorted( listaResultado,key=lambda task:task.data_atualizacao,reverse=ordem=="desc")
            else:
                 raise HTTPException(
                      status_code=400,
                      detail="Ordenar por recebeu um valor invalido."
                 )
        if data_fim is not None:
            listaResultado=[
                task for task in listaResultado
                if datetime.combine(data_fim,datetime.min.time()) > task.data_criacao 
            ]
        if data_inicio is not None:
            listaResultado=[
                task for task in listaResultado
                if datetime.combine(data_inicio,datetime.min.time()) < task.data_criacao 
            ]
        inicio=((pagina-1)*limite)
        paginaRen=listaResultado[inicio:inicio + limite]
    return {
        "pagina": pagina,
        "limite": limite,
        "total": len(listaResultado),
        "dados": paginaRen
    }
    