from fila_voo import fila_voos

def mostrarResultadoVoos():
    if not fila_voos:
        print("\n Nenhum resultado para mostrar.")
        return "Busca vazia."

    print("\n Resultados da busca de voos:")
    for v in fila_voos:
        status = " Disponível" if v["disponivel"] else " Indisponível"
        print(f"• Voo {v['numero']} — Horário: {v['horario']} — {status} — Assentos: {v['assentos']}")
    return "Busca concluída!"