import random
import os
import time

ruas = [
    {"nome": "A", "qtd_carros": random.randint(0, 10), "qtd_pedestres": random.randint(5,8), "aberta": True},
    {"nome": "B", "qtd_carros": random.randint(0, 10), "qtd_pedestres": random.randint(5,8), "aberta": False},
    {"nome": "C", "qtd_carros": random.randint(0, 10), "qtd_pedestres": random.randint(5,8), "aberta": False},
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

def representar_carros_e_pedestres():
    for rua in ruas:
        print(f"Rua {rua['nome']}: {rua['qtd_carros']} carros")
        print(f"       {rua['qtd_pedestres']} pedestres")
        print("\n")

def simular():
    indice_aberto = 0
    while True:
        ruas[indice_aberto]["aberta"] = False
        indice_aberto = (indice_aberto + 1) % len(ruas)
        ruas[indice_aberto]["aberta"] = True

        time.sleep(1)

        limpar_tela()
        representar_ruas()
        representar_carros_e_pedestres()

        aberta = ruas[indice_aberto]
        aberta["qtd_carros"] = max(0, aberta["qtd_carros"] - random.randint(1, 3))
        aberta["qtd_pedestres"] = max(0, aberta["qtd_pedestres"] - random.randint(1, 3))



if __name__ == "__main__":    
    simular()