import os

def main():
    clear_terminal()
    print("\n\n============ Calculadora de consumo energético ============\n\n");
    capacidade_fonte = float(input("Qual a capacidade energética do aparelho? (W)\n"));
    horas_dia = float(input("Em média, quantas horas o aparelho fica ligado por dia?\n"));
    dias_mes = int(input("Quantos dias por mês o aparelho é utilizado?\n"));
    
    energia_kwh = (dias_mes * horas_dia ) * capacidade_fonte / 1000

    # energia_kwh é o consumo estimado por mês em kWh
    print(f"O consumo estimado de energia do aparelho é: {energia_kwh:.2f} kWh por mês")
    
    calcular_custo = input("Deseja calcular o custo? (S/N)\n").strip().lower()
    if calcular_custo.startswith("s"):
        preco_por_kwh = float(input("Insira o preço do kWh: \n"))
        custo = energia_kwh * preco_por_kwh
        print(f"O custo estimado por mês é R$ {custo:.2f}")



def clear_terminal():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else: 
        _ = os.system('clear')

main()