from distance import Distance
from hash_table import Hash
from truck import Truck
from file_reader import File

# driver code

# ____________________________________________
# | FIRST: load package data into hash table |
# ____________________________________________

# construct a file reader object
package_data = File('WGUPS Package File.csv')

# get the size of the data list
size = package_data.get_row_count()

# construct the hash table using size
package_hash_table = Hash(size)

# parse the data into a hash table
package_hash_table = package_data.parse_package_data()

# printing out hash table details for packages
print(package_hash_table.list)
print(package_hash_table.size)
print(package_hash_table.get(34))

# ____________________________________________
# | SECOND: load distance data into table    |
# ____________________________________________
# code for testing distance table
distance_table = File('WGUPS Distance Table TEST.csv')

# set up empty data arrays
raw_data = []
distance_data = []
distance_labels = []

# parse and store the raw_data
raw_data = distance_table.parse_distance_data()

# set up a distance object
d = Distance(raw_data)

# cleaned data list
distance_data = d.clean_and_sort_data()

# distance labels
distance_labels = d.get_labels()

print(distance_labels)

# ____________________________________________
# | THIRD: load distance data into table    |
# ____________________________________________

# we have a max of three trucks
truck_one = Truck()
truck_two = Truck()
truck_three = Truck()

# let's add packages to the trucks regardless of constraints
temp_hash = package_hash_table  # might not need temp
for i in range(temp_hash.size):
    if temp_hash.list[i] is not None:
        if len(truck_one.truck) != truck_one.capacity:
            truck_one.add_package(temp_hash.list[i])
        elif len(truck_two.truck) != truck_two.capacity:
            truck_two.add_package(temp_hash.list[i])
        elif len(truck_three.truck) != truck_three.capacity:
            truck_three.add_package(temp_hash.list[i])
        else:
            print("No room on trucks!")

print(truck_one.truck[0])
print(truck_two.truck)
print(truck_three.truck)

# while len(truck_one.truck) != 0:
