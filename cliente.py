from banco_dados import *
from utils import *

def cadastrar_cliente():
    cliente = {
        "Nome": input("Digite o nome: "),
        "CPF": valida_cpf(input("Digite o CPF: ")),
        "RG": valida_rg(input("Digite o RG: ")),
        "Data de Nascimento": valida_data_nascimento(input("Digite a data de Nascimento [formato: dd/mm/yyy]: ")),
        "CEP": buscar_cep(input("Digite o CEP: ")),
        "Número da Residência": int(input("Digite o Número da Residência: ")),
        "Logradouro": input("Digite o Logradouro: "),
        "Complemento": input("Digite o Complemento: "),
        "Bairro": input("Digite o Bairro: "),
        "Cidade": input("Digite a Cidade: "),
        "Estado": input("Digite o Estado: ")
    }
    return cliente

def menu_cliente():
    opcao = 0
    validador_menu_cliente = True
    lista_cliente = []

    while validador_menu_cliente == True:
        print(
            "Seja bem vindo(a) ao menu do cliente."
            "\nSelecione uma das opções abaixo:"
            "\n"
            "\n 1 - Cadastrar Cliente"
            "\n 2 - Alterar Cliente"
            "\n 3 - Buscar Cliente"
            "\n 4 - Deletar Cliente"
            "\n 5 - Listar Clientes"
            "\n 6 - Voltar ao menu anterior"
            "\n")
        opcao = int(input("Digite a opcao desejada do menu do cliente: "))
        if opcao == 1:            
            clear()
            try:
                cliente = cadastrar_cliente()
                insert_banco_dados(cliente)
                lista_cliente.append(cliente)
            except:
                clear()
                print()
                print("--- Erro ao cadastrar cliente. Tente novamente ---")
        elif opcao == 2:
            clear()
            try:
                update_banco_dados(input("Digite o CPF: "))
            except:
                clear()
                print()
                print("--- Erro ao atualizar cliente. Tente novamente ---")
        elif opcao == 3:
            clear()
            try:
                select_cliente_banco_dados(input("Digite o CPF: "))
            except:
                clear()
                print()
                print("--- Erro ao buscar cliente. Tente novamente ---")
        elif opcao == 4:
            clear()
            try:        
                delete_banco_dados(input("Digite o CPF: "))
            except:
                clear()
                print()
                print("--- Erro ao deletar cliente. Tente novamente ---")
        elif opcao == 5:
            clear()
            try:
                select_banco_dados()
            except:
                clear()
                print()
                print("--- Erro ao listar clientes. Tente novamente ---")
        elif opcao == 6:
            clear()
            return
        else:
            clear()
            print()
            print("--- Opcao invalida. Tente novamente ---")

menu_cliente()