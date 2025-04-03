import os
import sys
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab3.utils import read_from_file, write_in_file, check_vertexes

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def create_adjacency_list(edges, vertex_number):
    adjacency = {i: [] for i in range(1, vertex_number + 1)}
    for first, second in edges:
        adjacency[first].append(second)
        adjacency[second].append(first)
    return adjacency


def bfs(start, end, adjacency_list):
    queue = deque([start])
    already_visited = {start}
    while queue:
        current_elem = queue.popleft()
        if current_elem == end:
            return True
        for edge in adjacency_list[current_elem]:
            if edge not in already_visited:
                already_visited.add(edge)
                queue.append(edge)
    return False


def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    vertex_number = int(data[0].split()[0])
    edges = [list(map(int, elem.split())) for elem in data[1:-1]]
    u, v = map(int, data[-1].split())
    if check_vertexes(edges, vertex_number):
        result = "1" if bfs(u, v, create_adjacency_list(edges, vertex_number)) else "0"

    else:
        result = "incorrect input data"
    write_in_file(str(result), PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
