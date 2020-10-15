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
print(package_hash_table.list[1])
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

for item in distance_data[0][1]:
    print(item[1])
print(distance_data[0][1][0])

# ____________________________________________
# | THIRD: load distance data into table    |
# ____________________________________________

# we have a max of three trucks
truck_one = Truck()
truck_two = Truck()
truck_three = Truck()


# now we add packages that are the closest regardless of other constraints - CURRENT
temp_hash = package_hash_table  # might not need temp
while len(truck_one.truck) != truck_one.capacity:
    if len(truck_one.truck) == 0:  # nothing is added so we find closest address to the HUB
        closest_distance = 10000000
        current_addr = 'HUB'
        for item in distance_data[0][1]:
            if float(item[1]) != 0:
                if
                closest_addr = item[0]
                closest_distance = item[1]



# let's add packages to the trucks regardless of constraints - OLD
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

# print(truck_one.truck[0][1].status)
# print(truck_two.truck)
# print(truck_three.truck)
miles = 0
while len(truck_one.truck) != 0:
    status = truck_one.truck[0][1].status
    if status == 'At HUB':
        for i in range(len(truck_one.truck)):  # changes all statuses of the packages
            truck_one.truck[i][1].set_status('en route')
        current_addr = 'HUB'
        next_addr = truck_one.truck[0][1].address
        for i in range(len(distance_data)):
            if distance_data[i][0] == current_addr:
                for item in distance_data[i][1]:
                    if item[0] == next_addr:
                        miles += float(item[1])
                        current_addr = next_addr
    else:
        next_addr = truck_one.truck[0][1].address
        for i in range(len(distance_data)):
            if distance_data[i][0] == current_addr:
                for item in distance_data[i][1]:
                    if item[0] == next_addr:
                        miles += float(item[1])
                        current_addr = next_addr
    truck_one.remove_package(truck_one.truck[0])
print(miles)

