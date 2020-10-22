from distance import Distance
from hash_table import Hash
from truck import Truck
from file_reader import File
import delivery_process

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

# TODO: make a separate file for loading trucks and delivering packages - DONE
# TODO: parameters to pass into the algorithm should be distance data, package data, *optional time
# TODO: make the algorithm keep track of time starting at 8:00
# TODO: allow for user input via the command line
# TODO: calculate my run time -- off first glance I think my algo runs in O(n^2)
print('WELCOME TO THE WGUPS COMMAND LINE INTERFACE')

delivery_process.deliver_packages(package_hash_table, distance_data)

print('See the options below for more WGUPS features:')
print(' - for package inquiry type inquiry [i]')
print(' - fo add a package type add [a]')
print(' - to print details of all packages type all [ap]')


user_input = input('Enter Here:')
