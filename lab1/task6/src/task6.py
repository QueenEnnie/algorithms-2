import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


from lab1.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def largest_number(parts):
    parts.sort(key=lambda x: x * 4, reverse=True)
    max_number = "".join(parts)
    return max_number if max_number[0] != "0" else 0


def task6():
    print("Задание №6")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    parts = read_from_file(PATH_INPUT)[1].split()
    result = largest_number(parts)
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task6()
