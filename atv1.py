import json
from datetime import datetime

ARQUIVO = 'tarefasat1.json'

def carregar_tarefas():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ")
    prazo = input("Prazo Final (AAAA-MM-DD): ")
    try:
        datetime.strptime(prazo, "%Y-%m-%d") 
    except ValueError:
        print(" Formato de data inválido.")
        return

    tarefas = carregar_tarefas()
    tarefas.append({
        "descricao": descricao,
        "prazo": prazo,
        "concluida": False
    })
    salvar_tarefas(tarefas)
    print(" Tarefa adicionada com sucesso!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas.sort(key=lambda x: x['prazo'])

    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas):
        status = "Positivo" if tarefa['concluida'] else "Espere"
        print(f"{i + 1}. [{status}] {tarefa['descricao']} - Prazo: {tarefa['prazo']}")

def concluir_tarefa():
    tarefas = carregar_tarefas()
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]['concluida'] = True
            salvar_tarefas(tarefas)
            print(" Tarefa marcada como concluída!")
        else:
            print(" Número inválido.")
    except ValueError:
        print("⚠️ Entrada inválida.")

def menu():
    while True:
        print("\n MENU DE TAREFAS")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            concluir_tarefa()
        elif opcao == '4':
            print("Finalizando")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
