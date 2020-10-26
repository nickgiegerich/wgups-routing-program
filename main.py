from distance import Distance
from hash_table import Hash
from file_reader import File
import delivery_process
from package import Package

# ******** IDENTIFICAION INFORMATION ********
# * First Name: Nicholas                    *
# * Last Name: Giegerich                    *
# * ID: 001059303                           *
# *                                         *
# *******************************************

#        PROGRAM TOTAL:
#        -----------------------
#       |  RUNTIME -> (n^2)    |
#       -----------------------

def load_package_data():
    """
    -- pass package csv into file reader class
    -- get the number of rows from csv
    -- construct a hash table based on size
    -- parse through package data to construct a hash table

    -----------------------
    |  RUNTIME -> O(n^2)  |
    -----------------------

    :return: package data in  a hash table
    """
    package_data = File('WGUPS Package File.csv')
    size = package_data.get_row_count()
    package_hash_table = Hash(size)
    package_hash_table = package_data.parse_package_data()
    return package_hash_table

def load_distance_table():
    """
    -- pass distance csv into file reader class
    -- pull out the raw data from the csv
    -- clean up raw data and store in a readable way

    -----------------------
    |  RUNTIME -> O(n^2)  |
    -----------------------

    :return: distance data
    """
    distance_table = File('WGUPS Distance Table.csv')
    raw_data = distance_table.parse_distance_data()
    d = Distance(raw_data)
    distance_data = d.clean_and_sort_data()
    return distance_data

def command_prompt(rerun=False):
    """
    -- print out all possible commands
    -- take in a user input
    -- based on user input the program does one of the following:
        -- insert a new package
        -- look up a package by id
        -- see package details at a specific time
        -- see all package details

    :param rerun: default False
    :return:
    """
    if not rerun:
        print('*********************** COMMANDS ***********************\n')
        print(' - to insert a package into the table type [a]dd')
        print(' - for package inquiry type [i]nquiry')
        print(' - to see package details at a specific time type [t]ime')
        print(' - to print details of all packages type [d]etails\n')
        print('!!!! To exit or quit the program type [q]uit !!!!\n')
        print('*********************** END COMMANDS ***********************')

    user_input = input('Enter command here (to see all commands type [h]elp):\n')

    if user_input == 'q' or user_input == 'quit': exit('Thank you for using WGUPS!')
    if user_input == 'h' or user_input == 'help': command_prompt(False)

    quit = False
    while not quit:

        if user_input == 'a' or user_input == 'add':
            try:
                package_id = int(input('Enter a package id:'))
                if package_id == 'q' or package_id == 'quit': exit('Thank you for using WGUPS!')
                address = str(input('Street address:'))
                city = str(input('City:'))
                state = str(input('State:'))
                zip_code = str(input('Zip code:'))
                delivery_time = str(input('Delivery time:'))
                weight = str(input('Weight:'))
                status = str(input('Status:'))
                notes = str(input('Notes:'))
                package = Package(str(package_id), address, city, state, zip_code, delivery_time, weight, status, notes)

                if package_hash_table.add(package_id, package):
                    print('The following package has been created:')
                    print(package)
                    command_prompt(True)
                else:
                    print('Please correct the issue')
                    command_prompt(True)

            except ValueError:
                print('\nERROR: package id must be a integer\n')
                command_prompt(True)

        if user_input == 'i' or user_input == 'inquiry':
            try:
                package_id = int(input('Enter a package id:'))
                if package_id == 'q' or package_id == 'quit': exit('Thank you for using WGUPS!')

                package = package_hash_table.get(package_id)
                if package:
                    print(package)
                    command_prompt(True)

            except ValueError:
                print('\nERROR: package id must be a integer\n')
                command_prompt(True)

        if user_input == 't' or user_input == 'type':
            try:
                package_id = int(input('Enter a package id:'))
                hour = int(input('Enter an hour (Ex. 10):'))
                minute = int(input('Enter a minute (Ex. 30):'))

                new_pkg_hash = load_package_data()
                new_dst_data = load_distance_table()
                delivery_process.deliver_packages(new_pkg_hash, new_dst_data, hour, minute, package_id)
                command_prompt(True)

            except ValueError:
                print('\nERROR: input must be an integer\n')
                command_prompt(True)

        if user_input == 'd' or user_input == 'details':
            print('All package data is below:')

            temp_list = []
            for pkg in package_hash_table.list:
                if pkg is not None:
                    print(pkg)
            command_prompt(True)

# ------------------------ DRIVER CODE ------------------------

print(
    '\n'
    '***********************************************\n'
    '* WELCOME TO THE WGUPS COMMAND LINE INTERFACE *\n'
    '***********************************************\n'
)

package_hash_table = load_package_data()  # get the package hash object
distance_data = load_distance_table()  # get the distance table object
delivery_process.deliver_packages(package_hash_table, distance_data)  # Call the delivery process when the program is run
command_prompt()  # call main CLI function


