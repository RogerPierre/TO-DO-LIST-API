from to_do_list_api.repository.InMemoryDB import db
from fastapi import HTTPException
#serviço http de get pelo id
def GetTaskById(id:int): 
    for task in db:
        if task.id==id:
            return task
    raise HTTPException(
                status_code=404,
                detail="tarefa não encotrada."
            )     
    