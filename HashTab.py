class HashTabElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTab:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size


def has_func(string, max) -> int:
    num = 5381
    for char in string:
        num = (num * 33) + ord(char)
    return num % max


def hash_tab_insert(hash_table: HashTab, key, value):
    i = has_func(key, hash_table.size)
    newDataElement = HashTabElement(key, value)
    if hash_table.data[i] is not None:
        hash_table.data[i].append(newDataElement)
    else:
        hash_table.data[i] = [newDataElement]


def hash_tab_delete(hash_table, key):
    i = has_func(key, hash_table.size)
    if hash_table.data[i] is not None:
        for j in range(0, len(hash_table.data[i])):
            if hash_table.data[i][j].key == key:
                hash_table.data[i].pop(j)
                break


def hash_tab_find(hash_table, key):
    i = has_func(key, hash_table.size)
    if hash_table.data[i] is None:
        return None
    else:
        for j in range(0, len(hash_table.data[i])):
            if hash_table.data[i][j].key == key:
                return hash_table.data[i][j].value
        


if __name__ == '__main__':
    h_tab = HashTab(8)

    hash_tab_insert(h_tab, "121", "Cat")
    hash_tab_insert(h_tab, "111", "Dog")
    hash_tab_insert(h_tab, "333", "Bird")

    hash_tab_delete(h_tab, "111")

    print(hash_tab_find(h_tab, "333"))
