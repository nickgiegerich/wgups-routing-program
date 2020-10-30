from truck import Truck
import datetime

#        TOTAL:
#        -----------------------
#       |  RUNTIME -> (n^2)    |
#       -----------------------
#
def optimize(addresses_to_visit, distance_data):
    """

    - add the HUB to beginning and end of the list, start/finish of route
    - first loop through the length of the list minus start/finish
    - second loop though the length minus two start at index 2
    - construct a new route using 2-opt swap
    - run the cost function on the new route and current optimal route
    - if the new route total distance is better, assign that as the optimal
    - return the optimal route when done
    - ** UPDATE **
    - added a conditional to check if the address 4580 S 2300 E exist
    - then we want to keep that at the front of the list for first
    - delivery

    -----------------------
    |  RUNTIME -> O(n^2)  |
    -----------------------

    :param addresses_to_visit: unvisited address list
    :param distance_data: distance from address - address
    :return:
    """
    addresses_to_visit.insert(0,'HUB')
    addresses_to_visit.append('HUB')

    if '4580 S 2300 E' in addresses_to_visit:
        index = 2
    else:
        index = 1

    optimal_route = addresses_to_visit  # initialize optimal route to addresses passed in

    still_optimizing  = True
    while still_optimizing:
        still_optimizing = False

        for i in range(index, len(addresses_to_visit) - 1):
            for k in range(i + index, len(addresses_to_visit)):
                new_route = two_opt_swap(addresses_to_visit, i, k)  # 2-opt swap function
                cost_one = cost(new_route, distance_data)  # calculate cost of a new route
                cost_two = cost(optimal_route, distance_data)

                if cost_one[0] < cost_two[0]:
                    optimal_route = new_route
                    still_optimizing = True

        addresses_to_visit = optimal_route
    return optimal_route


def two_opt_swap(route, i, k):
    """

    - make a copy of the route passed in
    - slice the list and reverse the order of indexes i-k
    - return the new route

    -----------------------
    |  RUNTIME -> O(K)    |
    -----------------------

    :param route:
    :param i:
    :param k:
    :return:
    """
    new_route = route.copy()  # copy route
    new_route[i:k] = route[k - 1:i - 1:-1]  # reverse addresses from i to k, minus one, otherwise the ends swap
    return new_route  # return route with swapped addresses


def cost(route, cost_data, time=-1, pkg_data=None, check_time=0, package=None, pkg_search=False):
    """

    - this function loops through cost data to retrieve the distance from address to address
    - it will first find the node to leave from then it will find the next node to visit
    - the next node should have a distance value associated with it and that becomes the distance to travel
    - this function also calls the tick() function to increment the time
    - this function is also used to return status of a package at a certain time using the find_pkg_status()
    - an update of the pkg status is done before either looping again of returning miles, time

    -----------------------
    |  RUNTIME -> O(n^2)   |
    -----------------------

    :param route: route to travel; sorted
    :param cost_data: distance data from address to address
    :param time: optional starting time
    :param pkg_data: optional data of all packages
    :param check_time: optional time to check the status of a pkg
    :param package: optional single package object
    :return: either return total miles/time OR boolean of found package
    """
    start_addr = route[0]
    total_miles = 0
    visited_addr = []
    visited_addr.append(start_addr)
    count = 0

    while len(visited_addr) != len(route) - 1:
        check = False
        for i in range(len(cost_data)):
            if check: break
            if cost_data[i][0] == start_addr:
                for addr in cost_data[i][1]:
                    if addr[0] == route[count + 1]:
                        total_miles += float(addr[1])
                        visited_addr.insert(0, addr[0])
                        if time != -1: time = tick(float(addr[1]), time)
                        if check_time != 0 and time >= check_time and pkg_search:
                            found = find_pkg_status(package, check_time, pkg_data)
                            return found
                        elif check_time != 0 and time >= check_time:
                            return True
                        if pkg_data is not None: update_pkg_status(addr[0], pkg_data, time)
                        start_addr = addr[0]
                        count += 1
                        check = True
                        break
    if check_time != 0 and pkg_search: return find_pkg_status(package, check_time, pkg_data)
    elif check_time != 0 and not pkg_search: return False
    return [total_miles, time]

def tick(mile, time):
    """

    - simple function to increment passed in time

    -----------------------
    |  RUNTIME -> O(1)    |
    -----------------------

    :param mile: number to represent distance
    :param time: time instance to increment
    :return: new incremented time
    """
    time_in_hours = mile/18
    time_in_secs = (time_in_hours * 60) * 60
    time = time + datetime.timedelta(0, time_in_secs)
    return time


def update_pkg_status(address, pkg_data, time):
    """

    - finds the packages with the address and updates the status

    -----------------------
    |  RUNTIME -> O(n)    |
    -----------------------

    :param address:
    :param pkg_data:
    :param time:
    :return:
    """
    for pkg in pkg_data:
        if pkg[1].address == address:
            pkg[1].set_status('Delivered at ' + str(time.time()))


def find_pkg_status(package, check_time, pkg_data):
    """

    - loops through all package data to find the matching pkg id
    - if found it will print the info of that package at that time

    -----------------------
    |  RUNTIME -> O(n)    |
    -----------------------

    :param package:
    :param check_time:
    :param pkg_data:
    :return:
    """
    package_found = False
    for pkg in pkg_data:
        if pkg[1].package_id == package.package_id:
            package_found = True
            print('\nAt', check_time.time(), '\n\n', package)
            return package_found
    return package_found

def deliver_packages(package_data, distance_data, status='normal', hour=0, minute=0, pkg_id=0):
    """
    -----------------------
    |  RUNTIME -> O(n^2)  |
    -----------------------

    :param pkg_id: package id
    :param status: run status
    :param package_data: a hash table of package data
    :param distance_data: distance data adjacency matrix
    :param hour: optional hour
    :param minute: optional minute
    :return: details of package delivery, or package status at certain time
    """
    t1_time = datetime.datetime(year=100, month=1, day=1, hour=8, minute=0)
    t2_time = datetime.datetime(year=100, month=1, day=1, hour=9, minute=5)
    t3_time = datetime.datetime(year=100, month=1, day=1, hour=10, minute=30)

    # construct truck objects
    truck_one = Truck()
    truck_two = Truck()
    truck_three = Truck()

    # construct address list to store addresses to visit
    t1_addresses_to_visit = []
    t2_addresses_to_visit = []
    t3_addresses_to_visit = []

    # load the truck objects for truck 1 and truck 2
    load_truck(truck_one, package_data, t1_addresses_to_visit, 1)
    load_truck(truck_two, package_data, t2_addresses_to_visit, 2)

    # before loading truck 3 change the address of package 9
    package_data.get(9).set_address('410 S State St')
    package_data.get(9).set_city('Salt Lake City')
    package_data.get(9).set_zipcode('84111')

    # now load truck 3
    load_truck(truck_three, package_data, t3_addresses_to_visit, 3)

    # find the best routes for each truck
    best_t1_route = optimize(t1_addresses_to_visit, distance_data)
    best_t2_route = optimize(t2_addresses_to_visit, distance_data)
    best_t3_route = optimize(t3_addresses_to_visit, distance_data)

    if status == 'normal':

        t1_miles = cost(best_t1_route, distance_data, t1_time, truck_one.truck)

        t2_miles = cost(best_t2_route, distance_data, t2_time, truck_two.truck)

        t3_miles = cost(best_t3_route, distance_data, t3_time, truck_three.truck)

        print('')
        print('Delivery Details')
        print('--------------')
        print('Truck 1 Delivered all its packages in', t1_miles[0], 'miles')
        print('T1 left the HUB at:', t1_time.time())
        print('T1 returned to the HUB at:', t1_miles[1].time(), '\n')
        print('--------------')
        print('Truck 2 Delivered all its packages in', t2_miles[0], 'miles')
        print('T2 left the HUB at:', t2_time.time())
        print('T2 returned to the HUB at:', t2_miles[1].time(), '\n')
        print('--------------')
        print('Truck 3 Delivered all its packages in', t3_miles[0], 'miles')
        print('T3 left the HUB at:', t3_time.time())
        print('T3 returned to the HUB at:', t3_miles[1].time(), '\n')
        print('--------------------------')
        print('TOTAL TRUCK MILEAGE:', t1_miles[0]+t2_miles[0]+t3_miles[0])
        print('--------------------------\n')

    elif status == 'ap':
        if hour < 1 or hour > 24 or minute < 0 or minute > 59:
            print('Time is out of range')
            return
        else:
            time_to_check = datetime.datetime(year=100, month=1, day=1, hour=hour, minute=minute)

        if time_to_check < t1_time:
            print('Here is the status of all packages at', time_to_check.time(), '\n')
            for pkg in package_data.list:
                if pkg is not None:
                    print(pkg[1])
            return

        if cost(best_t1_route, distance_data, t1_time, truck_one.truck, time_to_check):
            print('Here is the status of all packages at', time_to_check.time(), '\n')
            for pkg in package_data.list:
                if pkg is not None:
                    print(pkg[1])
            return
        if cost(best_t2_route, distance_data, t2_time, truck_two.truck, time_to_check):
            print('Here is the status of all packages at', time_to_check.time(), '\n')
            for pkg in package_data.list:
                if pkg is not None:
                    print(pkg[1])
            return
        if cost(best_t3_route, distance_data, t3_time, truck_three.truck, time_to_check):
            print('Here is the status of all packages at', time_to_check.time(), '\n')
            for pkg in package_data.list:
                if pkg is not None:
                    print(pkg[1])
            return
        else:
            print('Here is the status of all packages at', time_to_check.time(), '\n')
            for pkg in package_data.list:
                if pkg is not None:
                    print(pkg[1])
            return

    else:
        time_to_check = datetime.datetime(year=100, month=1, day=1, hour=hour, minute=minute)

        if package_data.get(pkg_id):
            package = package_data.get(pkg_id)
        else:
            return

        if time_to_check < t1_time:
            print('No packages have been delivered or loaded yet. Try a time after 8:00 am.')
            print('Here is the package requested before it has left the HUB')
            print(package)
            return True

        if cost(best_t1_route, distance_data, t1_time, truck_one.truck, time_to_check, package, True):
            return True
        elif cost(best_t2_route, distance_data, t2_time, truck_two.truck, time_to_check, package, True):
            return True
        elif cost(best_t3_route, distance_data, t3_time, truck_three.truck, time_to_check, package, True):
            return True

def load_truck(truck, package_data, addresses_to_visit, truck_number):
    """
    -----------------------
    |  RUNTIME -> O(kn)   |
    -----------------------

    - For the length of package data find valid package
    - If the truck is not full determine truck number
    - Sort the packages on constraints
    - As the loop iterates loosen the constraints to fill the truck
    - Exit the loop when truck is full or no more packages are at the HUB

    :param truck: a truck object to organize packages into
    :param package_data: a hash table of package data
    :param addresses_to_visit: a complete list of all addresses to visit for package deliveries
    :param truck_number: identifies the truck currently being loaded
    :return: truck object, addresses to visit list

    """
    count = 0
    truck_empty = True
    while truck_empty:
        for i in range(len(package_data.list)):

            if package_data.list[i] is not None and package_data.list[i] not in truck.truck and package_data.list[i][1].status == 'At HUB':

                pkg_data = package_data.list[i]
                pkg = package_data.list[i][1]
                pkg_id = float(package_data.list[i][0])
                notes = package_data.list[i][1].notes
                delivery_time = package_data.list[i][1].delivery_time
                address = package_data.list[i][1].address
                pkgs_needed = [13, 14, 15, 16, 19, 20]

                if len(truck.truck) != truck.capacity:

                    if truck_number == 1:

                        if delivery_time == '9:00 AM':
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK ONE')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 1 and pkg_id in pkgs_needed:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK ONE')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 1 and delivery_time != 'EOD' and 'Delayed' not in notes and 'Wrong' not in notes:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK ONE')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 2 and 'Delayed' not in notes and notes != 'Can only be on truck 2' and address in addresses_to_visit and 'Wrong' not in notes:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK ONE')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 3 and notes != 'Can only be on truck 2' and 'Delayed' not in notes and 'Wrong' not in notes:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK ONE')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                    elif truck_number == 2:

                        if notes == 'Can only be on truck 2' and address != '2530 S 500 E':
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 1 and address in addresses_to_visit and address != '2530 S 500 E' and 'Wrong' not in notes:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 2 and 'Delayed' in notes and address != '2530 S 500 E' and 'Wrong' not in notes or address in addresses_to_visit and address != '2530 S 500 E' and 'Wrong' not in notes:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 3 and address != '2530 S 500 E' and 'Wrong' not in notes or address in addresses_to_visit and address != '2530 S 500 E' and 'Wrong' not in notes:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                    elif truck_number == 3:
                        if count >= 1: truck_empty = False
                        else:
                            truck.add_package(package_data.list[i])
                            package_data.list[i][1].set_status('ON TRUCK THREE')
                            if package_data.list[i][1].address not in addresses_to_visit:
                                addresses_to_visit.append(package_data.list[i][1].address)
                else:
                    truck_empty = False
        if truck_number == 3: truck_empty = False
        count += 1
    return truck, addresses_to_visit

