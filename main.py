from distance import Distance
from hash_table import Hash
from truck import Truck
from file_reader import File

# driver code

# ____________________________________________
# | FIRST: load package data into hash table |
# |   - step 1: read in package file         |
# |   - step 2: get the num of rows in data  |
# |   - step 3: create hash table object     |
# |   - step 4: parse data into hash table   |
# ____________________________________________

package_data = File('WGUPS Package File.csv')

size = package_data.get_row_count()

package_hash_table = Hash(size)

package_hash_table = package_data.parse_package_data()

# ____________________________________________
# | SECOND: load distance data into table    |
# |   - step 1: read in raw distance data    |
# |   - step 2: clean up distance data       |
# |   - step 3: create hash table object     |
# |   - step 4: parse data into hash table   |
# ____________________________________________

distance_table = File('WGUPS Distance Table.csv')

raw_data = distance_table.parse_distance_data()

d = Distance(raw_data)

distance_data = d.clean_and_sort_data()

distance_labels = d.get_labels()  # MIGHT NOT NEED THIS

# ____________________________________________
# | THIRD: load trucks and deliver packages  |
# |   - step 1: read in raw distance data    |
# |   - step 2: clean up distance data       |
# |   - step 3: create hash table object     |
# |   - step 4: parse data into hash table   |
# ____________________________________________

# we have a max of three trucks
truck_one = Truck()
truck_two = Truck()
truck_three = Truck()


# STEP 1: Load the packages onto the truck based on constraints while not at capacity
# if the package is not None
# if the truck is not full
# if the pkg time is not EOD meaning it has a certain time to be delivered
# or if
print(package_hash_table.list)
iteration = 0
while len(truck_one.truck) != truck_one.capacity:
    for i in range(len(package_hash_table.list)):
        if package_hash_table.list[i] is not None and package_hash_table.list[i] not in truck_one.truck:
            if len(truck_one.truck) != truck_one.capacity:
                if package_hash_table.list[i][1].delivery_time != 'EOD':
                    truck_one.add_package(package_hash_table.list[i])
                elif iteration == 1 and package_hash_table.list[i][1].notes != 'Can only be on truck 2':
                    truck_one.add_package(package_hash_table.list[i])
    iteration += 1  # we have gone through the whole list increment iteration
print(truck_one.truck)

# STEP 2: Organize/find the addresses that the truck needs to visit

addresses_to_visit = []  # list to hold the addresses that we need to visit

for pkg in truck_one.truck:
    if pkg[1].address not in addresses_to_visit:
        addresses_to_visit.append(pkg[1].address)
print(addresses_to_visit)

# STEP 3: Take each of those addresses and organize by closest to preceding address starting at HUB
#   then deliver pkgs when we find the next closest addr to go to
starting_addr = 'HUB'
next_addr = ''

nearest_dist = 0  # value to store the nearest distance from the start address
total_miles = 0  # total miles, gets incremented at each address stop

closest_dists = []  # a list of the closest distances in miles
visited_addresses = []  # a list of the addresses that were visited
iterations = 0

while len(addresses_to_visit) != 0:  # remove an address from this list every time it becomes the starting address

    for i in range(len(distance_data)):  # for each index in distance data

        if distance_data[i][0] == starting_addr:  # if the distance data 'key' is equal to the starting address

            for addrs in distance_data[i][1]:  # for each address tied to starting address

                if addrs[0] in addresses_to_visit:  # if the address that we are at is in addresses to visit comp dist
                    if float(addrs[1]) < nearest_dist or nearest_dist == 0:
                        nearest_dist = float(addrs[1])
                        next_addr = addrs[0]
                        iterations += 1
            closest_dists.append(nearest_dist)
            total_miles += nearest_dist
            addresses_to_visit.remove(next_addr)
            visited_addresses.append(next_addr)
            starting_addr = next_addr
            nearest_dist = 0
            break
print(addresses_to_visit)
print(total_miles)
print(distance_data)
print(closest_dists)
print(visited_addresses)


# now we add packages that are the closest regardless of other constraints - CURRENT
# temp_hash = package_hash_table  # might not need temp
# closest_addr = ''
# closest_distance = None
# boolean = True
# current_addr = 'HUB'
# found_current_addr = False
# index_of_addr = 0
# address_dist_pair = ['', '']
# address_queue = []
#
# while len(address_queue) != truck_one.capacity:
#     if len(address_queue) == 0:  # base case, the truck is empty and at the HUB, find closest addr to HUB
#         for item in distance_data[0][1]:
#
#             if closest_distance is None:
#                 closest_distance = float(item[1])  # could be 0.0
#
#             compare_dist = float(item[1])  # could also be 0.0
#             if compare_dist < closest_distance and compare_dist != 0.0 or closest_distance == 0.0:
#                 closest_distance = compare_dist
#                 closest_addr = item[0]
#                 address_dist_pair = [closest_addr, closest_distance]
#         address_queue.append(address_dist_pair)
#         print(address_queue)
#         print('The closest distance to the', current_addr, 'is:', closest_distance, 'and the address is:', closest_addr)
#     else:  # the truck already has packages on it
#
#         current_addr = closest_addr  # the curr addr now becomes the closest addr
#         closest_distance = None  # reset the closest dist to None
#
#         for i in range(len(distance_data)):  # iterate over the distance data to find where the current addr lives
#             if distance_data[i][0] == current_addr:  # found where the current_addr key is
#                 index_of_addr = i
#                 break
#
#         for item in distance_data[index_of_addr][1]:
#
#             if closest_distance is None:  # first iteration closest distance is None
#                 closest_addr = item[0]  # this will be HUB
#                 closest_distance = float(item[1])  # setting the closest distance to first address regardless
#
#             compare_dist = float(item[1])  # getting the distance, on first iteration same as closest
#
#             if compare_dist < closest_distance and compare_dist != 0.0 or closest_distance == 0.0:
#                 closest_distance = compare_dist
#                 closest_addr = item[0]
#                 address_dist_pair = [closest_addr, closest_distance]
#
#             elif closest_addr == 'HUB' or closest_addr in address_queue:
#                 closest_distance = compare_dist
#                 closest_addr = item[0]
#                 address_dist_pair = [closest_addr, closest_distance]
#
#         address_queue.append(address_dist_pair)
#         # print(address_queue)
#         # break
# print(address_queue)

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
