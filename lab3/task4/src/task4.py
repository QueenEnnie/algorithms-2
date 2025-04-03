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


def topological_sort(adjacency, vertex_number):
    edges_in_vertex = {i: 0 for i in range(1, vertex_number + 1)}
    for start in range(1, vertex_number + 1):
        for end in adjacency[start]:
            edges_in_vertex[end] += 1
    queue = deque()
    for vertex in range(1, vertex_number + 1):
        if edges_in_vertex[vertex] == 0:
            queue.append(vertex)
    topological_order = []
    while queue:
        start = queue.popleft()
        topological_order.append(start)
        for end in adjacency[start]:
            edges_in_vertex[end] -= 1
            if edges_in_vertex[end] == 0:
                queue.append(end)
    return topological_order


def task4():
    print("Задание №4")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    vertex_number = int(data[0].split()[0])
    edges = [list(map(int, elem.split())) for elem in data[1:]]
    adjacency_list = create_adjacency_list(edges, vertex_number)
    if check_vertexes(edges, vertex_number):
        result = " ".join(map(str, topological_sort(adjacency_list, vertex_number)))
    else:
        result = "incorrect input data"

    write_in_file(result, PATH_OUTPUT)
    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task4()
