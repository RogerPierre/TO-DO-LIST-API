from pydantic import BaseModel
from datetime import date
class TaskSquema(BaseModel):
    titulo:str
    descricao:str
    concluida:bool
    tags_lista:list[str]
    data_criacao:date=date.today()
    data_atualizacao:date|None=None

class TaskDB(TaskSquema):
    id:int
