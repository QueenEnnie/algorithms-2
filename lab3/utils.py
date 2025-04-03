def read_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data


def write_in_file(data,path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)


def check_vertexes(edges, n):
    correct = list(range(1, n + 1))
    for pair in edges:
        if not(pair[0] in correct and pair[1] in correct and pair[0] != pair[1]):
            return False
    return True

