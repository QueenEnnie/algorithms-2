import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def equal_subsets(numbers):
    if sum(numbers) % 2 != 0:
        return -1
    half = sum(numbers) // 2
    dp = [[False, []] for _ in range(half + 1)]
    dp[0][0] = True
    for i, elem in enumerate(numbers):
        for j in range(half, elem - 1, -1):
            if dp[j - elem][0]:
                dp[j][0] = True
                dp[j][1] = dp[j - elem][1] + [elem]
    if not dp[half][0]:
        return -1
    return dp[half][1]


def task12():
    print("Задание №12")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = list(map(int, read_from_file(PATH_INPUT)[1].split()))
    result = equal_subsets(data)
    result = str(len(result)) + '\n' + " ".join(map(str, result)) if not isinstance(result, int) else str(result)
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task12()
