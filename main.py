from fastapi import FastAPI
from todo_api import routerTask
from todo_api.aplication.root import router as root


app=FastAPI()



##rota raiz
app.include_router(router=root)

##rota de tarefas
app.include_router(router=routerTask,prefix="/tarefas")