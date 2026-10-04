from fastapi import FastAPI
from to_do_list_api import routerTask
from to_do_list_api.aplication.root import router as root


app=FastAPI()



##rota raiz
app.include_router(router=root)

##rota de tarefas
app.include_router(router=routerTask,prefix="/tarefas")