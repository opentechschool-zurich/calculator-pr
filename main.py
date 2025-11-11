def calculate(a, op, b):
    if op == '+':
        return a + b
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

if __name__ == '__main__':
    main()
