import csv
from hash_table import Hash
from package import Package

class File:
    """
        TOTAL:
        -----------------------
        |  RUNTIME -> O(n)    |
        -----------------------
    """
    def __init__(self, file):
        """
        - construct a file object
        - initialize row count = 0
        :param file:
        """
        self.file = file
        self.row_count = 0

    def parse_package_data(self):
        """

        - instantiate a hash table with corresponding size to row count
        - use the built in csv reader to open, read, and delimit file
        - create a package object with the data in the csv
        - store the package object in the hash table

        -----------------------
        |  RUNTIME -> O(n)    |
        -----------------------

        :return: hash table with package objects
        """
        hash_table = Hash(self.get_row_count())  # initiate hash table using num rows

        with open(self.file, mode='r', encoding='utf-8-sig') as csv_data:
            csv_data.seek(0)  # since we read the file once already we want to make sure we reset the pointer
            data = csv.reader(csv_data, delimiter=',')

            for row in data:
                key = row[0]
                package_id = row[0]
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]
                delivery_time = row[5]
                weight = row[6]
                status = 'At HUB'
                notes = row[7]

                p = Package(package_id, address, city, state, zip_code, delivery_time, weight, status, notes)

                hash_table.add(key, p)  # add the key/values to the hash table

        return hash_table

    def get_row_count(self):
        """

        - count each row in the file

        -----------------------
        |  RUNTIME -> O(n)    |
        -----------------------

        :return: return number of rows in file
        """
        for line in self.file:
            self.row_count += 1
        return self.row_count

    def parse_distance_data(self):
        """

        - use the built in csv reader to open, read, and delimit file
        - for each row of data store into a list

        -----------------------
        |  RUNTIME -> O(n)    |
        -----------------------

        :return: raw-ish distance data
        """
        with open(self.file, mode='r', encoding='utf-8-sig', newline='') as csv_data:
            csv_data.seek(0)  # since we read the file once already we want to make sure we reset the pointer
            data = csv.reader(csv_data, delimiter=',')

            raw_data = []
            for row in data:
                if row[0] == '5383 S 900 East #104':
                    row[0] = '5383 South 900 East #104'
                raw_data.append(row)

            return raw_data
