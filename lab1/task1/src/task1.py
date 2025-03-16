import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def fractional_knapsack(capacity, things):
    for i in range(len(things)):
        things[i] += [things[i][0] / things[i][1]]
    things.sort(key=lambda x: x[2], reverse=True)
    max_sum = 0
    for value, weight, price in things:
        if capacity - weight >= 0:
            max_sum += value
            capacity -= weight
        else:
            max_sum += capacity * price
            break
    return f"{round(max_sum, 4):.4f}"


def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    capacity = int(data[0].split()[1])
    things = [list(map(int, elem.split())) for elem in data[1:]]
    result = fractional_knapsack(capacity, things)
    write_in_file(str(result), PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
