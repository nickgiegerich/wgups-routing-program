class HashTable:
    # initiates a empty hash table and the sets the capacity to a specified size
    def __init__(self, size):
        self.size = size
        self.table = []
        for _ in range(size):
            self.table.append([])

    # inserts the key into the hash table
    def set_package(self, key, value):
        index = self._hash(key)

        inner_list = self.table[index]

        inner_list.append(int(key))
        self.table[index].append(value)

    # returns all items in the hash table
    def get_all(self):
        for item in range(len(self.table)):
            inner_list = self.table[item]
            return inner_list

    def get_package_by_id(self, key):
        index = self._hash(key)
        inner_list = self.table[index]

        if key in inner_list:
            return inner_list[1]
        else:
            return "Error"

    def get_package_by_address(self, addr):
        address = addr.lower()
        # initialize temp array to store found packages with the same address
        temp = []

        for item in range(len(self.table)):
            inner_list = self.table[item]
            current_addr = inner_list[1][1]
            string = ' '.join(map(str, current_addr))
            string = string.lower()
            if string == "address: " + address:
                temp.append(inner_list[1])
        if len(temp) == 0:
            return "ERROR - Address Not Found or Incomplete\n" \
                   "please use this format:\n" \
                   " -----------------\n" \
                   "| 1234 W State St |\n" \
                   " -----------------"
        else:
            for item in range(len(temp)):
                return temp

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

    # creates a unique key for hash table values
    def _hash(self, key):
        return int(key) % self.size
