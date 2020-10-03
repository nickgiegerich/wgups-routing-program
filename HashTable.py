
class HashTable:
    # initiates a empty hash table and the sets the capacity to a specified size
    def __init__(self, size):
        self.size = size
        self.table = []
        for _ in range(size):
            self.table.append([])

    # creates a unique key for hash table values
    def _hash(self, key):
        return int(key) % self.size

    # inserts the key into the hash table
    def set_package(self, key, value):
        hash_index = self._hash(key)
        inner_list = self.table[hash_index]

        inner_list.append(hash_index)

        inner_list.append(value)

    # prints the hash table
    def get_all(self):
        print(self.table, '\n')

    def get_package(self, key):
        index = self._hash(key)
        print(index)
        inner_list = self.table[index]

        if key in inner_list:
            package_index = inner_list.index(key)
            print(inner_list[package_index])
            print(inner_list[1][1])
            return inner_list[package_index]
        else:
            return None

    def is_full(self):
        count_none_items = 0
        for item in range(len(self.table)):
            if self.table[item] is None:
                count_none_items += 1
        if count_none_items == 0:
            return True
        else:
            return False

    def increase_size(self):
        new_hash_table = HashTable(4 * len(self.table))
        new_size = self.size * 4
        for item in range(len(self.table)):
            new_hash_table.insert_key(self.table[item][0], self.table[item][1])
        self.table = new_hash_table
        self.size = new_size
