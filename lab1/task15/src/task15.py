import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab1.utils import read_from_file, write_in_file

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def matching_brackets(first, second):
    return ((first == "(" and second == ")") or
            (first == "[" and second == "]") or
            (first == "{" and second == "}"))


def restore_sequence(left, right, pairs, string):
    if left > right:
        return ""
    if pairs[left][right] == -1:
        return ""
    if pairs[left][right] == (left, right):
        return string[left] + restore_sequence(left + 1, right - 1, pairs, string) + string[right]
    m = pairs[left][right][0]
    return restore_sequence(left, m, pairs, string) + restore_sequence(m + 1, right, pairs, string)


def max_correct_sequence(string):
    n = len(string)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    bracket_pairs = [[-1 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            if matching_brackets(string[left], string[right]):
                dp[left][right] = dp[left + 1][right - 1] + 2
                bracket_pairs[left][right] = (left, right)
            for m in range(left, right):
                if dp[left][right] < dp[left][m] + dp[m + 1][right]:
                    dp[left][right] = dp[left][right] + dp[m + 1][right]
                    bracket_pairs[left][right] = (m, m + 1)

    return restore_sequence(0, n - 1, bracket_pairs, string)


def task15():
    print("Задание №15")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    result = max_correct_sequence(data[0].strip()) if len(data) > 0 else ""
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task15()
