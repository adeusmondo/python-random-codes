# 3.1.1 Numbers

def main():
    '''
        Operators: +, -, *, / work just
        like in most other languages.
        () can be used for grouping
    '''
    sum_ints = 2 + 2
    print(">>> 2 + 2\n", sum_ints)
    
    mix_operators = 50 - 5 * 6
    print(">>> 50 - 5 * 6\n", mix_operators)

    grouping_numbers = (50 - 5 * 6) / 4
    print(">>> (50 - 5 * 6) / 4\n", grouping_numbers)

    # Division always returns a floating point number
    division_returns_floating = 8 / 5
    print(">>> 8 / 5\n", division_returns_floating)

    # Floor division to get a integer result (discarding any fractional result)
    division_returns_floor = 8 // 5
    print(">>> 8 // 5\n", division_returns_floor)

    remainder = 5 % 2
    print(">>> 5 % 2\n", remainder)

    # Powers = elevar a potência, valor a direita é sempre a potência
    powers = 5 ** 2
    print(">>> 5 ** 2\n", powers)


if __name__ == "__main__":
    main()