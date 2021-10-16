# Algoritmo que calcule o valor de reembolso de despesas de combustível de um
# funcionário. Considere que o carro tem o consumo de 1 litro de gasolina a
# cada 13km rodado. E o preço do litro de gasolina é de R$ 2,20.

PRECO_GASOLINA = 2.20
KM_LT = 13

def main():
    kms = float(input("Quantos KMs foram rodados? \n -> "))
    total = kms * KM_LT * PRECO_GASOLINA
    print(f"Valor de reebolso será de R$ {total:.2f}")


if __name__ == "__main__":
    main()
