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
    return adjacency


def find_cyclic(adjacency, vertex_number):
    edges_in_vertex = {i: 0 for i in range(1, vertex_number + 1)}
    for start in range(1, vertex_number + 1):
        for end in adjacency[start]:
            edges_in_vertex[end] += 1
    queue = deque()
    for vertex in range(1, vertex_number + 1):
        if edges_in_vertex[vertex] == 0:
            queue.append(vertex)
    already_visited = 0
    while queue:
        start = queue.popleft()
        already_visited += 1
        for end in adjacency[start]:
            edges_in_vertex[end] -= 1
            if edges_in_vertex[end] == 0:
                queue.append(end)
    return already_visited != vertex_number


def task3():
    print("Задание №3")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    vertex_number = int(data[0].split()[0])
    edges = [list(map(int, elem.split())) for elem in data[1:]]
    if check_vertexes(edges, vertex_number):
        result = "1" if find_cyclic(create_adjacency_list(edges, vertex_number),
                                    vertex_number) else "0"
    else:
        result = "incorrect input data"

    write_in_file(result, PATH_OUTPUT)
    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task3()
