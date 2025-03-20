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

    def delete(self, key):
        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left_child = _delete(node.left_child, key)
            elif key > node.key:
                node.right_child = _delete(node.right_child, key)
            else:
                if not node.left_child:
                    return node.right_child
                if not node.right_child:
                    return node.left_child
                min_greater_node = self.min_node(node.right_child)
                node.key, node.right_child = min_greater_node.key, _delete(node.right_child, min_greater_node.key)
            return node
        self.root = _delete(self.root, key)

    def min_node(self, node):
        while node.left_child:
            node = node.left_child
        return node

    def exists(self, key):
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                return "true"
            current_node = current_node.left_child if key < current_node.key \
                else current_node.right_child
        return "false"

    def next(self, key):
        current_node, answer = self.root, None
        while current_node is not None:
            if current_node.key > key:
                answer = current_node.key
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return answer if answer is not None else "none"

    def prev(self, key):
        answer, current_node = None, self.root
        while current_node:
            if current_node.key < key:
                answer = current_node.key
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return answer if answer is not None else "none"


def do_operations(operations):
    tree = BinarySearchTree()
    result = []
    for elem in operations:
        operation, number = elem.split()
        if "insert" in operation:
            tree.insertion(int(number))
        elif "exists" in operation:
            result.append(tree.exists(int(number)))
        elif "prev" in operation:
            result.append(tree.prev(int(number)))
        elif "next" in operation:
            result.append(tree.next(int(number)))
        else:
            tree.delete(int(number))
    return result


def task5():
    print("Задание №5")
    print("Входные данные:")
    print("".join(read_from_file(PATH_INPUT)))

    operations = read_from_file(PATH_INPUT)
    result = "\n".join(map(str, do_operations(operations)))
    write_in_file(result, PATH_OUTPUT)

    print("Выходные данные:")
    print(result)


if __name__ == "__main__":
    task5()
