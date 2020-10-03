import csv
from HashTable import HashTable


class Package:
    """ This class handles loading in and sorting package information """

    # setting the file manually here optionally can have this input by the user, or a generic file reader class could
    # work
    def __init__(self):
        self.file = open('WGUPS Package File.csv')

    def read_file(self):
        row_count = 0
        for line in self.file:
            row_count += 1
        h = HashTable(row_count)
        with open('WGUPS Package File.csv', mode='r', encoding='utf-8-sig') as csv_data:
            csv_data.seek(0)
            data = csv.reader(csv_data, delimiter=',')
            for row in data:
                key = row[0]
                package_id = [row[0]]
                address = [row[1]]
                city = [row[2]]
                state = [row[3]]
                zip_code = [row[4]]
                delivery_time = [row[5]]
                weight = [row[6]]
                notes = [row[7]]
                values = [package_id, address, city, state, zip_code, delivery_time, weight, notes]

                h.set_package(key, values)

        h.get_all()
        first_object = h.get_package(1)
        print(first_object)
        return True