import os, sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def find_min_height(heights, number, epsilon):
    lower_bound, upper_bound = 0, heights[0]
    last_height = float("-inf")
    while upper_bound > (lower_bound + epsilon):
        mid_height = (lower_bound + upper_bound) / 2
        previous_height = heights[0]
        current_height = mid_height
        is_above_ground_flag = current_height > 0
        for i in range(2, number):
            next_height = 2 * current_height - previous_height + 2
            if next_height <= 0:
                is_above_ground_flag = False
            previous_height = current_height
            current_height = next_height
        if is_above_ground_flag:
            upper_bound = mid_height
            last_height = current_height
        else:
            lower_bound = mid_height
    return last_height


def task2():
    print("Задание №2")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    number, first_bulb_height = map(float, data[0].split())
    number = int(number)
    bulb_heights = [first_bulb_height] + [0 for _ in range(number - 1)]
    epsilon = 10 ** -6 / (number - 1)
    result = str(find_min_height(bulb_heights, number, epsilon))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task2()
