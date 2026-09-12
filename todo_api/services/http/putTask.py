from todo_api.repository.InMemoryDB import db
from todo_api.squemas.taskSquema import TaskSquema,TaskDB
from fastapi import HTTPException
from datetime import datetime

def PutTask(id:int,task:TaskSquema):
    for i,u in enumerate(db):
        if u.id==id:

            Task_updated=TaskDB(id=id,**task.model_dump())
            Task_updated.data_atualizacao=datetime.today()
            db[i]=Task_updated

            return Task_updated

    raise HTTPException(
        status_code=404,
        detail="Tarefa nâo encontrada"
    )
        