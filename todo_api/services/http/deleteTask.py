from todo_api.repository.InMemoryDB import db
from fastapi import HTTPException


def DeleteTask(id:int):
    for i,u in enumerate(db):
        if u.id==id:
            print(u)
            del db[i]
            return
    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada."
    )