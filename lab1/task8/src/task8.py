import os, sys, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def schedule_lectures(timing):
    timing.sort(key=lambda x: (x[1], x[0]))
    count = 1
    previous_ending = timing[0][1]
    for start, ending in timing[1:]:
        if previous_ending <= start:
            count += 1
            previous_ending = ending
    return count


def task8():
    print("Задание №8")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    timing = [list(map(int, elem.split())) for elem in data[1:]]
    result = schedule_lectures(timing)
    write_in_file(str(result), PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task8()