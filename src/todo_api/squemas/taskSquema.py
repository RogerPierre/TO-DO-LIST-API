from pydantic import BaseModel
from datetime import datetime
#esquemas em pydantic como camada model da aplicação
class TaskSquema(BaseModel):
    titulo:str
    descricao:str
    concluida:bool=False
    tags:list[str]
    data_criacao:datetime=datetime.today()
    data_atualizacao:datetime|None=None

class TaskDB(TaskSquema):
    id:int
