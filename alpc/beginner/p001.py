# Algoritmo que solicite o número de horas que um trabalhador realiza por dia,
# solicite o número de dias trabalhados em um mês e apresente o número total de 
# horas trabalhadas no mês

def main(test: bool = False, **params):
    if test is True:
        num_horas_dia = params.get("num_horas_dia", 0)
        dias_trabalhados_mes = params.get("dias_trabalhados_mes", 0)
        return {num_horas_dia * dias_trabalhados_mes}

    num_horas_dia = int(input("Número de horas trabalhadas por dia: "))
    dias_trabalhados_mes = int(input("Número de dias trabalhados no mês: "))

    print("Total de horas trabalhadas no mês: " + \
        f"{num_horas_dia * dias_trabalhados_mes} horas")


if __name__ == "__main__":
    main()
