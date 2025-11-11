def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a // b
        else:
            raise Exception('division by 0')
    return None

def calculate_list(list_to_calculate):
    result = 0
    if len(list_to_calculate) < 3:
        return list_to_calculate[1]
    for u in range(0, len(list_to_calculate)-3, 3):
        result = calculate(list_to_calculate[u], list_to_calculate[u+1], list_to_calculate[u+2])
        list_to_calculate[u+2] = result
    return result

def main():
    assert calculate(3, '+', 2) == 5
    assert calculate(4, '-', 2 ) == 2
    try:
        calculate(10,'/', 0)
        assert False
    except Exception:
        pass
    assert calculate(10, '*', 5) == 50
    assert calculate(10, '/', 5) == 2

if __name__ == '__main__':
    main()
