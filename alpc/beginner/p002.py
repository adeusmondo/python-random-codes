# Algoritmo p/ calcular a quantidade de carne necessária para um churrasco de
# acordo com o número de pessoas convidadas. Considere que todas são adultas
# e que um adulto consome 250 gramas de carne por refeição

CONSUMO_GRAMAS_ADULTO = 0.250

def main():
    qts_adultos = int(input("Quantos adultos convidados: "))
    kgs = qts_adultos * CONSUMO_GRAMAS_ADULTO
    print(f"Será necessário {kgs:.2f} Kg de carne")


if __name__ == "__main__":
    main()
