from todo_api.repository.InMemoryDB import db
from fastapi import HTTPException

def GetTaskById(id:int):
    if id>len(db) or id<=0:
        raise HTTPException(
            status_code=404,
            detail="tarefa não encotrada."
        )
    Task=db[id-1]
    return Task