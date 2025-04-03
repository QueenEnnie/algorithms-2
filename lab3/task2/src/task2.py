import os
import sys

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


def dfs(vertex, already_visited, adjacency):
    already_visited.add(vertex)
    for neighbor in adjacency[vertex]:
        if neighbor not in already_visited:
            dfs(neighbor, already_visited, adjacency)


def find_components_number(adjacency, vertex_number):
    already_visited, components_count = set(), 0
    for vertex in range(1, vertex_number + 1):
        if vertex not in already_visited:
            components_count += 1
            dfs(vertex, already_visited, adjacency)
    return components_count


def task2():
    print("Задание №2")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    vertex_number = int(data[0].split()[0])
    edges = [list(map(int, elem.split())) for elem in data[1:]]
    if check_vertexes(edges, vertex_number):
        result = find_components_number(create_adjacency_list(edges, vertex_number), vertex_number)
    else:
        result = "incorrect input data"
    write_in_file(str(result), PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task2()
