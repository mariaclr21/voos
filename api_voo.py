import re
from pesquisar_voo import pesquisarVoo

def api_voos():
    termo = input("Digite o número do voo (ex: 1234) ou o horário (ex: 14:30): ").strip()

    # Validação: permite apenas número ou formato HH:MM
    formato_horario = re.match(r"^\d{1,2}:\d{2}$", termo)
    if not (termo.isdigit() or formato_horario):
        print(" Erro: digite apenas um número de voo (ex: 1234) ou um horário válido (ex: 14:30).")
        return None  # não prossegue para o banco de dados

    return pesquisarVoo(termo)