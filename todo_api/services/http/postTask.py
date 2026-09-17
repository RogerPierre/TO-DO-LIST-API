
from todo_api.repository.InMemoryDB import db
from ...squemas.taskSquema import TaskSquema,TaskDB
#serviço http de post de tarefa
def PostTask(request:TaskSquema):
    task_with_id=TaskDB( id=len(db)+1,**request.model_dump())
    db.append(task_with_id)
    return task_with_id