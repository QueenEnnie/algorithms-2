import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import read_from_file, write_in_file

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def z_function(string):
    values = [0] * len(string)
    left, right = 0, 0
    for i in range(1, len(string)):
        if i <= right:
            values[i] = min(values[i - left], right - i + 1)
        while i + values[i] < len(string) and string[values[i]] == string[i + values[i]]:
            values[i] += 1
        if i + values[i] - 1 > right:
            left, right = i, i + values[i] - 1
    return values[1:]


def task6():
    print("Задание №6")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    result = " ".join(map(str, z_function(data[0])))
    write_in_file(str(result), PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task6()
