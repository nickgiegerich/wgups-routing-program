from distance import Distance
from hash_table import Hash
from truck import Truck
from file_reader import File
import delivery_process
from package import Package

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
print(' - to insert a package into the table type add [a]')
print(' - for package inquiry type inquiry [i]')
print(' - to see package details at a specific time type time [t]')
print(' - to print details of all packages type all [ap]')
print('To exit or quit the program please type quit [q]')

user_input = input('Enter command here:')

if user_input == 'q' or user_input == 'quit': exit('Thank you for using WGUPS')

quit = False
while not quit:
    if user_input == 'a' or user_input == 'add':
        try:
            package_id = int(input('Enter a package id:'))
        except ValueError:
            print('\nERROR: package id must be a integer\n')
            continue
        address = str(input('Street address:'))
        city = str(input('City:'))
        state = str(input('State:'))
        zip_code = str(input('Zip code:'))
        delivery_time = str(input('Delivery time:'))
        weight = str(input('Weight:'))
        status = str(input('Status:'))
        notes = str(input('Notes:'))
        package = Package(str(package_id),address,city,state,zip_code,delivery_time,weight,status,notes)
        if package_hash_table.add(package_id,package):
            print('The following package has been created:')
            print(package)
        else:
            print('Please correct the issue')
            continue


