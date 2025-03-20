import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from lab2.utils import read_from_file, write_in_file

PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


def inorder_traversal(tree):
    nodes_in_traversal, stack = [], []
    current_node = 0
    while stack or current_node != -1:
        if current_node != -1:
            stack.append(current_node)
            current_node = tree[current_node][1]
        else:
            current_node = stack.pop()
            nodes_in_traversal.append(tree[current_node][0])
            current_node = tree[current_node][2]
    return nodes_in_traversal


def preorder_traversal(tree):
    nodes_in_traversal, stack = [], [0]
    while stack:
        current_node = stack.pop()
        if current_node != -1:
            nodes_in_traversal.append(tree[current_node][0])
            stack.append(tree[current_node][2])
            stack.append(tree[current_node][1])
    return nodes_in_traversal


def postorder_traversal(tree):
    nodes_in_traversal, stack = [], [(0, False)]
    while stack:
        current_node, already_visited = stack.pop()
        if current_node != -1:
            if already_visited:
                nodes_in_traversal.append(tree[current_node][0])
            else:
                stack.append((current_node, True))
                stack.append((tree[current_node][2], False))
                stack.append((tree[current_node][1], False))
    return nodes_in_traversal


def task1():
    print("Задание №1")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    data = read_from_file(PATH_INPUT)
    tree = [tuple(map(int, elem.split())) for elem in data[1:]]
    nodes_in_inorder_traversal = " ".join(map(str, inorder_traversal(tree)))
    nodes_in_preorder_traversal = " ".join(map(str, preorder_traversal(tree)))
    nodes_in_postorder_traversal = " ".join(map(str, postorder_traversal(tree)))
    result = "\n".join([nodes_in_inorder_traversal, nodes_in_preorder_traversal,
                        nodes_in_postorder_traversal])
    write_in_file(str(result), PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task1()
