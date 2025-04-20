import json

ARQUIVO = 'estoqueat2.json'

def carregar_estoque():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO, 'w') as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto():
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço unitário (R$): "))
    except ValueError:
        print("⚠️ Valores inválidos.")
        return

    estoque = carregar_estoque()
    estoque.append({
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    })
    salvar_estoque(estoque)
    print("Produto adicionado com sucesso!")
    
def exibir_estoque():
    estoque = carregar_estoque()
    if not estoque:
        print("Estoque vazio.")
        return

    total = 0
    print("\n Produtos no estoque:")
    for i, produto in enumerate(estoque, 1):
        subtotal = produto['quantidade'] * produto['preco']
        total += subtotal
        print(f"{i}. {produto['nome']} - Qtde: {produto['quantidade']} - Preço: R${produto['preco']:.2f} - Subtotal: R${subtotal:.2f}")

    print(f"\n Valor total do estoque: R${total:.2f}")

def menu():
    while True:
        print("\n CONTROLE DE ESTOQUE")
        print("1. Adicionar Produto")
        print("2. Exibir Estoque")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            exibir_estoque()
        elif opcao == '3':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
