import json
import os

ARQUIVO = 'contatos.json'

def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    else:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO, 'w') as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato():
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    contatos = carregar_contatos()
    contatos.append({
        "nome": nome,
        "telefone": telefone,
        "email": email
    })
    salvar_contatos(contatos)
    print("✅ Contato adicionado com sucesso!")

def buscar_contato():
    termo = input("Digite o nome para buscar: ").strip().lower()
    contatos = carregar_contatos()
    encontrados = [c for c in contatos if termo in c['nome'].lower()]

    if encontrados:
        print("\n Contatos encontrados:")
        for c in encontrados:
            print(f" Nome: {c['nome']}")
            print(f" Telefone: {c['telefone']}")
            print(f" E-mail: {c['email']}")
            print("—" * 20)
    else:
        print(" Nenhum contato encontrado com esse nome.")

# Menu principal
def menu():
    while True:
        print("\n GERENCIADOR DE CONTATOS")
        print("1. Adicionar contato")
        print("2. Buscar contato por nome")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            buscar_contato()
        elif opcao == '3':
            print(" Encerrando o gerenciador de contatos.")
            break
        else:
            print(" Opção inválida.")

if __name__ == '__main__':
    menu()
