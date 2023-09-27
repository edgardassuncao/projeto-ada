from cliente import menu_cliente
from utils import clear

def exibir_menu():
    opcao = 0
    validador_menu = True
    clear()

    while validador_menu == True:
        print(
            "Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da ExxonMobil."
            "\nSelecione uma das opções abaixo:"
            "\n"
            "\n 1 - Cliente"
            "\n 2 - Ordem"
            "\n 3 - Realizar análise da carteira"
            "\n 4 - Imprimir relatório da carteira"
            "\n 5 - Sair"
            "\n")
        opcao = int(input("Digite a opcao desejada: "))
        if opcao == 1:
            clear()
            menu_cliente()
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            clear()
            print(
                "\n"
                "--- Encerrando a execucao do programa ---"
                "\n")
            validador_menu = False
        else:
            clear()
            print()
            print("--- Opcao invalida! Tente novamente ---")

exibir_menu()