import pyodbc
from utils import *

def retornar_cursor_banco_dados():
    connection = pyodbc.connect(retorna_string_conexao_banco_dados())
    cursor = connection.cursor()
    return cursor, connection

def retorna_string_conexao_banco_dados():
    return(
        "DRIVER={SQL Server};"
        "SERVER=HOESQL633;"
        "DATABASE=SkillUp_ECASSU1;"
        "Trusted_Connection=yes;"
    )

def insert_banco_dados(cliente):
    cursor, connection = retornar_cursor_banco_dados()
    insert_query = '''
    INSERT INTO projeto_ada_cliente (id_cliente, nome, cpf, rg, data_nascimento, cep, numero_residencia, logradouro, complemento, bairro, cidade, estado)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    values = (cliente['Nome'],
              cliente['CPF'],
              cliente['RG'],
              cliente['Data de Nascimento'],
              cliente['CEP']['CEP'],
              cliente['Número da Residência'],
              cliente['CEP']['Logradouro'],
              cliente['Complemento'],
              cliente['Bairro'],
              cliente['Cidade'],
              cliente['Estado'])
    cursor.execute(insert_query, values)
    connection.commit()

def update_banco_dados(cpf):
    update_cliente = {
        "Nome": input("Digite o nome: "),
        "CPF": valida_cpf(input("Digite o CPF: ")),
        "RG": valida_rg(input("Digite o RG: ")),
        "Data de Nascimento": valida_data_nascimento(input("Digite a data de Nascimento [formato: dd/mm/yyyy]: ")),
        "CEP": buscar_cep(input("Digite o CEP: ")),
        "Número da Residência": int(input("Digite o Número da Residência: ")),
        "Logradouro": input("Digite o Logradouro: "),
        "Complemento": input("Digite o Complemento: "),
        "Bairro": input("Digite o Bairro: "),
        "Cidade": input("Digite a Cidade: "),
        "Estado": input("Digite o Estado: ")
    }
    
    cursor, connection = retornar_cursor_banco_dados()
    update_query = "UPDATE projeto_ada_cliente SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ?, logradouro = ?, complemento = ?, bairro = ?, cidade = ?, estado = ? WHERE cpf = '" + cpf + "';"
    
    values = (update_cliente['Nome'],
              update_cliente['CPF'],
              update_cliente['RG'],
              update_cliente['Data de Nascimento'],
              update_cliente['CEP']['CEP'],
              update_cliente['Número da Residência'],
              update_cliente['CEP']['Logradouro'],
              update_cliente['Complemento'],
              update_cliente['Bairro'],
              update_cliente['Cidade'],
              update_cliente['Estado'])
    
    cursor.execute(update_query, values)
    connection.commit()

def select_cliente_banco_dados(cpf):
    clear()
    cursor, connection = retornar_cursor_banco_dados()
    select_query = "select * from projeto_ada_cliente where cpf = '" + cpf + "';"
    cursor.execute(select_query)
    cliente = cursor.fetchall()

    if len(cliente) == 0:
        print("--- Cliente não existe. Tente novamente ---")
    else:
        for i in cliente:
            print("ID do Cliente: "        + str(i[0]))
            print("Nome: "                 + str(i[1]))
            print("CPF: "                  + str(i[2]))
            print("RG: "                   + str(i[3]))
            print("Data de Nascimento: "   + str(i[4]))
            print("CEP: "                  + str(i[5]))
            print("Número da Residência: " + str(i[6]))
            print("Logradouro: "           + str(i[7]))
            print("Complemento: "          + str(i[8]))
            print("Bairro: "               + str(i[9]))
            print("Cidade: "               + str(i[10]))
            print("Estado: "               + str(i[11]))

            x = input("--- Pressione ENTER para voltar ao menu anterior ---")
            clear()

    connection.commit()

def delete_banco_dados(cpf):
    cursor, connection = retornar_cursor_banco_dados()
    delete_query = "DELETE FROM projeto_ada_cliente WHERE cpf = '" + cpf + "';"
    cursor.execute(delete_query)
    connection.commit()

def select_banco_dados():
    cursor, connection = retornar_cursor_banco_dados()
    cursor.execute("select * from projeto_ada_cliente")
    clientes = cursor.fetchall()
    
    for c in clientes:
        print("\n")
        print("ID do Cliente: "        + str(c[0]))
        print("Nome: "                 + str(c[1]))
        print("CPF: "                  + str(c[2]))
        print("RG: "                   + str(c[3]))
        print("Data de Nascimento: "   + str(c[4]))
        print("CEP: "                  + str(c[5]))
        print("Número da Residência: " + str(c[6]))
        print("Logradouro: "           + str(c[7]))
        print("Complemento: "          + str(c[8]))
        print("Bairro: "               + str(c[9]))
        print("Cidade: "               + str(c[10]))
        print("Estado: "               + str(c[11]))
        print("\n")
    
        x = input("--- Pressione ENTER para voltar ao menu anterior ---")
        clear()
    
    connection.commit()