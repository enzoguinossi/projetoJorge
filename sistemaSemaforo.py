import random
import os
import time

ruas = [
    {"nome": "A", "qtd_carros": random.randint(0, 10), "aberta": True},
    {"nome": "B", "qtd_carros": random.randint(0, 10), "aberta": False},
    {"nome": "C", "qtd_carros": random.randint(0, 10), "aberta": False},
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def representar_ruas():
    for rua in ruas:
        if(rua["aberta"]):
            simbolo = '|   |'
        else: simbolo = '| X |'
        print(simbolo, end="  ")
    print()

def representar_carros():
    for rua in ruas:
        print(f"Rua {rua['nome']}: {rua['qtd_carros']} carros")
        print("\n")

def simular():
    indice_aberto = 0
    while True:
        limpar_tela()
        representar_ruas()
        representar_carros()

        aberta = ruas[indice_aberto]
        aberta["qtd_carros"] = max(0, aberta["qtd_carros"] - random.randint(1, 3))

        ruas[indice_aberto]["aberta"] = False
        indice_aberto = (indice_aberto + 1) % len(ruas)
        ruas[indice_aberto]["aberta"] = True

        time.sleep(1)

if __name__ == "__main__":    
    simular()