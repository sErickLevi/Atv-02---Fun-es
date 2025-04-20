import json
import os
import getpass

ARQUIVO = 'bancoat4.json'

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    else:
        return {}

def salvar_dados(dados):
    with open(ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4)

def criar_conta():
    dados = carregar_dados()
    usuario = input(" Nome de usuário: ")
    if usuario in dados:
        print(" Usuário já existe.")
        return
    senha = getpass.getpass(" Senha: ")

    dados[usuario] = {
        "senha": senha,
        "saldo": 0.0,
        "transacoes": []
    }

    salvar_dados(dados)
    print(" Conta criada com sucesso!")

def login():
    dados = carregar_dados()
    usuario = input(" Usuário: ")
    senha = getpass.getpass(" Senha: ")

    if usuario in dados and dados[usuario]['senha'] == senha:
        print(f" Login bem-sucedido! Bem-vindo, {usuario}.")
        menu_conta(usuario)
    else:
        print(" Usuário ou senha incorretos.")

def menu_conta(usuario):
    dados = carregar_dados()
    while True:
        print("\n MENU BANCÁRIO")
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Ver Extrato")
        print("5. Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            print(f" Saldo atual: R${dados[usuario]['saldo']:.2f}")
        elif op == '2':
            valor = float(input("Valor para depósito: R$"))
            dados[usuario]['saldo'] += valor
            dados[usuario]['transacoes'].append(f"Depósito: +R${valor:.2f}")
            salvar_dados(dados)
            print(" Depósito realizado!")
        elif op == '3':
            valor = float(input("Valor para saque: R$"))
            if valor <= dados[usuario]['saldo']:
                dados[usuario]['saldo'] -= valor
                dados[usuario]['transacoes'].append(f"Saque: -R${valor:.2f}")
                salvar_dados(dados)
                print(" Saque realizado!")
            else:
                print(" Saldo insuficiente.")
        elif op == '4':
            print(" Extrato:")
            for t in dados[usuario]['transacoes']:
                print(f" - {t}")
            if not dados[usuario]['transacoes']:
                print("Nenhuma transação registrada.")
        elif op == '5':
            print(" Saindo da conta.")
            break
        else:
            print(" Opção inválida.")

def menu():
    while True:
        print("\n SISTEMA BANCÁRIO")
        print("1. Criar conta")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_conta()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print(" Encerrando sistema.")
            break
        else:
            print(" Opção inválida.")

if __name__ == '__main__':
    menu()
