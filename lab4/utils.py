def read_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data


def write_in_file(data,path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)


