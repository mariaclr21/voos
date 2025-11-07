from api_voo import api_voos
from mostrar_resultado_voos import mostrarResultadoVoos

def main():
    resultado = api_voos()
    if resultado is not None:  # só mostra se houve pesquisa válida
        mostrar_resultado_voos = mostrarResultadoVoos()

if __name__ == "__main__":
    main()