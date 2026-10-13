
from todo_api.repository.InMemoryDB import db
from ...squemas.taskSquema import TaskSquema,TaskDB


#serviço http de post de tarefa
def PostTask(request:TaskSquema):
    newId=1
    for task in db:
        if task.id!=newId:
            newId=newId+(task.id-newId)
        newId=newId+1
        

    task_with_id=TaskDB( id=newId,**request.model_dump())
    db.append(task_with_id)
    return task_with_id