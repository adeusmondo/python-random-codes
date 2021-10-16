# Algoritmo que retorne o valor total de revelação de um filme de 24 poses,
# solicite o número de fotos reveladas. E considere que o valor unitário da
# revelação por foto é de R$ 0,90

PRECO_FOTO = 0.9

def main():
    num_fotos = int(input("Informe o número de fotos a serem reveladas.\n -> "))
    total_preco_fotos = num_fotos * PRECO_FOTO

    print(f"Custo total das fotos reveladas: R$ {total_preco_fotos:.2f}")


if __name__ == "__main__":
    main()
