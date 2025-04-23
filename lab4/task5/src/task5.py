import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import read_from_file, write_in_file

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def prefix_function_creation(string):
    prefix_function_values = [0] * len(string)
    for i in range(1, len(string)):
        previous = prefix_function_values[i - 1]
        while previous > 0 and string[i] != string[previous]:
            previous = prefix_function_values[previous - 1]
        if string[i] == string[previous]:
            previous += 1
        prefix_function_values[i] = previous
    return prefix_function_values


def task5():
    print("Задание №5")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    result = " ".join(map(str, prefix_function_creation(data[0])))
    write_in_file(str(result), PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task5()
