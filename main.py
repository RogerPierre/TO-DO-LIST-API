from fastapi import FastAPI
from todo_api.aplication.tasksRouter import routerTask
from fastapi import APIRouter
from todo_api.aplication.root import router as root


app=FastAPI()




app.include_router(router=root)
app.include_router(router=routerTask,prefix="/tarefas")