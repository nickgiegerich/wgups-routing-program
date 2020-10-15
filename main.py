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
# print(package_hash_table.list[1])
# print(package_hash_table.size)
# print(package_hash_table.get(34))

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

# for item in distance_data[0][1]:
#     print(item[1])
# print(distance_data[0][1][0])

# ____________________________________________
# | THIRD: load distance data into table    |
# ____________________________________________

# we have a max of three trucks
truck_one = Truck()
truck_two = Truck()
truck_three = Truck()

# now we add packages that are the closest regardless of other constraints - CURRENT
temp_hash = package_hash_table  # might not need temp
closest_addr = ''
while len(truck_one.truck) != truck_one.capacity:
    if len(truck_one.truck) == 0:  # base case, the truck is empty and at the HUB, find closest addr to HUB
        closest_distance = None
        current_addr = 'HUB'
        for item in distance_data[0][1]:
            if closest_distance is None:
                closest_distance = float(item[1])  # could be 0.0
            compare_dist = float(item[1])  # could also be 0.0
            if compare_dist < closest_distance and compare_dist != 0.0 or closest_distance == 0.0:
                closest_distance = compare_dist
                closest_addr = item[0]
                address_dist_pair = [closest_addr, closest_distance]
        truck_one.add_package(address_dist_pair)
        print(truck_one.truck)
        print('The closest distance to the', current_addr, 'is:', closest_distance, 'and the address is:', closest_addr)
        break
    else:  # the truck already has packages on it
        for i in range(len(distance_data)):
            if distance_data[i][0] == closest_addr:
                print('')



# let's add packages to the trucks regardless of constraints - OLD
# temp_hash = package_hash_table  # might not need temp
# for i in range(temp_hash.size):
#     if temp_hash.list[i] is not None:
#         if len(truck_one.truck) != truck_one.capacity:
#             truck_one.add_package(temp_hash.list[i])
#         elif len(truck_two.truck) != truck_two.capacity:
#             truck_two.add_package(temp_hash.list[i])
#         elif len(truck_three.truck) != truck_three.capacity:
#             truck_three.add_package(temp_hash.list[i])
#         else:
#             print("No room on trucks!")

# print(truck_one.truck[0][1].status)
# print(truck_two.truck)
# print(truck_three.truck)
# miles = 0
# while len(truck_one.truck) != 0:
#     status = truck_one.truck[0][1].status
#     if status == 'At HUB':
#         for i in range(len(truck_one.truck)):  # changes all statuses of the packages
#             truck_one.truck[i][1].set_status('en route')
#         current_addr = 'HUB'
#         next_addr = truck_one.truck[0][1].address
#         for i in range(len(distance_data)):
#             if distance_data[i][0] == current_addr:
#                 for item in distance_data[i][1]:
#                     if item[0] == next_addr:
#                         miles += float(item[1])
#                         current_addr = next_addr
#     else:
#         next_addr = truck_one.truck[0][1].address
#         for i in range(len(distance_data)):
#             if distance_data[i][0] == current_addr:
#                 for item in distance_data[i][1]:
#                     if item[0] == next_addr:
#                         miles += float(item[1])
#                         current_addr = next_addr
#     truck_one.remove_package(truck_one.truck[0])
# print(miles)
