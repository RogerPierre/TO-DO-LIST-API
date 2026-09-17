from fastapi import APIRouter

router=APIRouter()
#rota raiz
@router.get("/")
def raiz():
    return{
        "":""
    }
