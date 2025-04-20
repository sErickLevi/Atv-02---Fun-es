import json
import os

ARQUIVO = 'reservasat3.json'
LINHAS = 5 
COLUNAS = 5  

def gerar_mapa_inicial():
    mapa = {}
    for i in range(LINHAS):
        linha = chr(65 + i) 
        for j in range(1, COLUNAS + 1):
            mapa[f"{linha}{j}"] = False  
    return mapa
def carregar_mapa():
        mapa = gerar_mapa_inicial()
        return mapa

def exibir_mapa(mapa):
    print("\n  Mapa de Assentos (✅ livre | ❌ reservado)")
    for i in range(LINHAS):
        linha = chr(65 + i)
        for j in range(1, COLUNAS + 1):
            assento = f"{linha}{j}"
            if mapa[assento]:
                print("❌", end=' ')
            else:
                print("✅", end=' ')
        print(f" ← Linha {linha}")
    print("   1   2   3   4   5")

def reservar_assento(mapa):
    assento = input("Digite o código do assento (ex: B2): ").upper()
    if assento in mapa:
        if not mapa[assento]:
            mapa[assento] = True
            print(f"✔️ Assento {assento} reservado com sucesso!")
        else:
            print("⚠️ Esse assento já está reservado.")
    else:
        print("❌ Assento inválido.")

def cancelar_reserva(mapa):
    assento = input("Digite o código do assento a cancelar (ex: C4): ").upper()
    if assento in mapa:
        if mapa[assento]:
            mapa[assento] = False
            print(f" Reserva do assento {assento} cancelada.")
        else:
            print(" Esse assento não está reservado.")
    else:
        print(" Assento inválido.")

def menu():
    mapa = carregar_mapa()

    while True:
        print("\n MENU - Sistema de Reservas")
        print("1. Visualizar mapa de assentos")
        print("2. Reservar assento")
        print("3. Cancelar reserva")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_mapa(mapa)
        elif opcao == '2':
            reservar_assento(mapa)
        elif opcao == '3':
            cancelar_reserva(mapa)
        elif opcao == '4':
            print(" Encerrando sistema de reservas.")
            break
        else:
            print(" Opção inválida.")

if __name__ == "__main__":
    menu()
