# Um algoritmo que mostre o percentual que uma despesa mensal representa
# do seu salário total.

def main():
    salario = float(input("Informe seu salário\n -> R$ "))
    despesas = float(input("Informe o montante das suas despesas\n -> R$ "))
    total = (despesas * 100) / salario
    print(f"Suas despesas correspondem a {total:.2f}% do seu salário") 


if __name__ == "__main__":
    main()
