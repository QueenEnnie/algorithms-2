import os
import sys
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab4.utils import read_from_file, write_in_file
PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def naive_subsequence_search(subsequence, sequence):
    indices = []
    for i in range(len(sequence) - len(subsequence) + 1):
        if sequence[i:i + len(subsequence)] == subsequence:
            indices.append(i + 1)
    return indices


def check_for_incorrect_input(data):
    if len(data) != 2:
        return "there should be two strings in input data"
    subsequence, sequence = data[0].strip(), data[1].strip()
    if len(subsequence) > len(sequence):
        return "the subsequence length is greater than sequence's"
    if len(subsequence) == 0 or len(sequence) == 0:
        return "empty strings are not allowed"


def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    check_result = check_for_incorrect_input(data)
    if check_result:
        result = check_result
    else:
        subsequence, sequence = data[0].strip(), data[1].strip()
        result = naive_subsequence_search(subsequence, sequence)
        result = str(len(result)) + "\n" + " ".join(map(str, result))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
