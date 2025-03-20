import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))


from lab2.utils import read_from_file, write_in_file


PATH_INPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'input.txt'))
PATH_OUTPUT = os.path.abspath(os.path.join(os.path.split(os.getcwd())[0], 'txtf', 'output.txt'))


class Node:
    def __init__(self, key):
        self.key = key
        self.right_child = None
        self.left_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertion(self, key):
        if not self.root:
            self.root = Node(key)
            return
        current_node = self.root
        while True:
            if key < current_node.key:
                if current_node.left_child is None:
                    current_node.left_child = Node(key)
                    return
                current_node = current_node.left_child
            elif key > current_node.key:
                if current_node.right_child is None:
                    current_node.right_child = Node(key)
                    return
                current_node = current_node.right_child
            else:
                return

    def delete_min_greater_after(self, value):
        current_node = self.root
        answer = 0
        while current_node:
            if current_node.key > value:
                answer = current_node.key
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return answer


def do_operations(operations):
    tree = BinarySearchTree()
    min_greater_keys = []
    for elem in operations:
        if "+" in elem:
            tree.insertion(int(elem.split()[1]))
        else:
            min_greater_keys.append(tree.delete_min_greater_after(int(elem.split()[1])))
    return min_greater_keys


def task3():
    print("Задание №3")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    operations = read_from_file(PATH_INPUT)
    result = "\n".join(map(str, do_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task3()
