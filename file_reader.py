import csv
from hash_table import Hash
from package import Package


class File:
    def __init__(self, file):
        self.file = file
        self.row_count = 0

    def parse_package_data(self):

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
        for line in self.file:
            self.row_count += 1
        return self.row_count

    def parse_distance_data(self):

        with open(self.file, mode='r', encoding='utf-8-sig', newline='') as csv_data:
            csv_data.seek(0)  # since we read the file once already we want to make sure we reset the pointer
            data = csv.reader(csv_data, delimiter=',')

            raw_data = []
            for row in data:
                raw_data.append(row)

            return raw_data
