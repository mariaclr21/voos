from banco_dados import colecao_voos
from fila_voo import filaVoo

def pesquisarVoo(termo):
    voos = list(colecao_voos.find({
        "$or": [
            {"numero": {"$regex": termo, "$options": "i"}},
            {"horario": {"$regex": termo, "$options": "i"}}
        ]
    }))
    filaVoo(voos)
    return voos