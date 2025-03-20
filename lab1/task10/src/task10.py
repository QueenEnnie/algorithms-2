import os, sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def apples_order(height, change_numbers):
    for i in range(len(change_numbers)):
        elem = change_numbers[i]
        change_numbers[i] += [elem[1] - elem[0], i + 1]

    plus_change = [elem for elem in change_numbers if elem[2] > 0]
    minus_change = [elem for elem in change_numbers if elem[2] <= 0]
    plus_change.sort(key=lambda x: x[0])
    minus_change.sort(key=lambda x: x[2], reverse=True)
    order = []
    for a, b, difference, number in plus_change + minus_change:
        height -= a
        if height > 0:
            order.append(number)
            height += b
        else:
            return -1
    return order


def task10():
    print("Задание №10")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    height = int(data[0].split()[1])
    change_numbers = [list(map(int, elem.split())) for elem in data[1:]]
    result = apples_order(height, change_numbers)
    result = " ".join(map(str, result)) if not isinstance(result, int) else str(result)
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task10()
