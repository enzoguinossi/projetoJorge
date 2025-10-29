import random
import os
import time

# Códigos ANSI para cores
VERDE = '\033[92m'  # Verde
VERMELHO = '\033[91m'  # Vermelho
RESET = '\033[0m'   # Resetar cor

# Define o estado inicial das ruas
ruas = [
    {"nome": "A", "qtd_carros": random.randint(0, 10), "qtd_pedestres": random.randint(5,8), "aberta": True},
    {"nome": "B", "qtd_carros": random.randint(0, 10), "qtd_pedestres": random.randint(5,8), "aberta": False},
    {"nome": "C", "qtd_carros": random.randint(0, 10), "qtd_pedestres": random.randint(5,8), "aberta": False},
]

# ---------------------------
# Funções de utilidade
# ---------------------------

def limpar_tela():
    """
    Limpa o terminal para melhor visualização da simulação.
    Funciona tanto em Windows ('cls') quanto em sistemas Unix ('clear').
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def representar_ruas():
    """
    Representa visualmente o estado atual dos semáforos de cada rua.
    Verde (|   |) indica rua aberta para passagem.
    Vermelho (| X |) indica rua fechada.
    """
    for rua in ruas:
        if(rua["aberta"]):
            simbolo = f"{VERDE}|   |{RESET}"
        else:
            simbolo = f"{VERMELHO}| X |{RESET}"
        print(simbolo, end="  ")
    print()

def representar_carros_e_pedestres():
    """
    Mostra a quantidade de carros e pedestres em cada rua.
    Exibe as informações de forma alinhada e organizada:
    - Nome da rua
    - Quantidade de carros
    - Quantidade de pedestres
    """
    for rua in ruas:
        print(f"Rua {rua['nome']:<10} {rua['qtd_carros']} carros")
        print(f"{'':<14} {rua['qtd_pedestres']} pedestres")
        print()

# ---------------------------
# Funções de lógica
# ---------------------------

def atualizar_rua_aberta(indice_atual):
    ruas[indice_atual]["aberta"] = False
    indice_atual = (indice_atual + 1) % len(ruas)
    ruas[indice_atual]["aberta"] = True
    return indice_atual

def passar_carros_e_pedestres(rua):
    """
    Simula carros e pedestres atravessando na rua aberta.
    Reduz quantidades aleatoriamente.
    """
    rua["qtd_carros"] = max(0, rua["qtd_carros"] - random.randint(1, 3))
    rua["qtd_pedestres"] = max(0, rua["qtd_pedestres"] - random.randint(1, 3))

def gerar_novos_carros_e_pedestres():
    """
    Adiciona novos carros e pedestres aleatoriamente às ruas.
    """
    for rua in ruas:
        # 30% de chance de aparecer novos carros/pedestres
        if random.random() < 0.3:
            rua["qtd_carros"] += random.randint(0, 2)
        if random.random() < 0.3:
            rua["qtd_pedestres"] += random.randint(0, 2)


def simular():
    """Executa a simulação principal do sistema de semáforos."""
    indice_aberto = 0
    while True:
        
        # Atualiza estado visual
        limpar_tela()
        representar_ruas()
        representar_carros_e_pedestres()

        # Atualiza quantidades
        passar_carros_e_pedestres(ruas[indice_aberto])
        gerar_novos_carros_e_pedestres()
        
        # Alterna rua aberta
        indice_aberto = atualizar_rua_aberta(indice_aberto)

        # Espera 1 segundo entre ciclos
        time.sleep(1)




if __name__ == "__main__":    
    simular()