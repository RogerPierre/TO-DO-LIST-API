from fastapi import APIRouter
from ..services.http.getAllTask import GetTask
from ..services.http.postTask import PostTask
from ..squemas.taskSquema import TaskSquema
routerTask=APIRouter( prefix="/tarefas")

@routerTask.get("/tarefas")
def GetAll():
    return GetTask()

@routerTask.post("/tarefas")
def Post(task:TaskSquema):
    PostTask(task)
    return task