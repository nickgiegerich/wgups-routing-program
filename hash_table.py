class Hash:
    def __init__(self, size=10):
        """
        constructs a list with None at a given size
        :param size: size of list
        """
        self.size = size * 2  # double the size on construction
        self.list = [None] * self.size  # fill a list with None as place holders

    def add(self, key, value):
        """
        adds a package to the list (hash table) if that index is None,
        if that index is not None then that package already exist,
        for this program we are assuming all packages have a unique ID

        :rtype: bool
        :param key: unique ID
        :param value: a package object
        :return: True if added, False otherwise
        """
        hashed_key = self._hash_key(key)
        kvp = [key, value]

        if self.list[hashed_key] is None:
            self.list[hashed_key] = list(kvp)
            return True
        else:  # we have a collision
            print('ERROR: that package id already exist')
            return False

    def get(self, key):
        """
        gets a singular package by the ID (key),
        if that ID is None then there is no package there
        :rtype: object
        :param key: unique key
        :return: value associated to key, otherwise False
        """
        try:
            hashed_key = self._hash_key(key)
            kvp = self.list[hashed_key]

            if self.list[hashed_key] is None:
                return False
            else:
                return kvp[1]
        except IndexError:
            return False

    def _hash_key(self, key):
        """
        private method that generates a index (bucket) by
        taking the key mod size of the list and returning that
        value
        :rtype: int
        :param key:
        :return:
        """
        return int(key)
