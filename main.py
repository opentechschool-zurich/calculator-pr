def calculate(a, op, b):
    if op == '+':
        return a + b
    return None

def calculate_list(term):
    pass

def main():
    assert calculate(3, '+', 2) == 5

    term = input('>')
    term = filter(lambda c: not c.isspace(), term)
    result = calculate_list(term)
    print(result)

if __name__ == '__main__':
    main()
