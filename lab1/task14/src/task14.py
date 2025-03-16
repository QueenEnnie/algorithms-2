import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def do_operation(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second


def max_expression_value(expression):
    numbers = [int(elem) for i, elem in enumerate(expression) if i % 2 == 0]
    operations = [elem for i, elem in enumerate(expression) if i % 2 != 0]
    dp_min = [[0 for _ in range(len(numbers))] for _ in range(len(numbers))]
    dp_max = [[0 for _ in range(len(numbers))] for _ in range(len(numbers))]

    for i in range(len(numbers)):
        dp_min[i][i] = numbers[i]
        dp_max[i][i] = numbers[i]

    for length in range(1, len(numbers)):
        for l in range(len(numbers) - length):
            r = l + length
            min_value = float('inf')
            max_value = float('-inf')
            for m in range(l, r):
                operation = operations[m]
                a = do_operation(dp_max[l][m], dp_max[m + 1][r], operation)
                b = do_operation(dp_max[l][m], dp_min[m + 1][r], operation)
                c = do_operation(dp_min[l][m], dp_max[m + 1][r], operation)
                d = do_operation(dp_min[l][m], dp_min[m + 1][r], operation)
                min_value = min(min_value, a, b, c, d)
                max_value = max(max_value, a, b, c, d)
            dp_min[l][r] = min_value
            dp_max[l][r] = max_value
    return dp_max[0][len(numbers) - 1]


def task14():
    print("Задание №14")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)[0].strip()
    result = str(max_expression_value(data))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task14()
