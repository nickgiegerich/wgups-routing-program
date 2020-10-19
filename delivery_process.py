from truck import Truck
import datetime


def load_truck(truck, package_data, addresses_to_visit, truck_number):
    if truck_number == 1:
        count = 0  # keeps track of each iteration of loading pkgs
        while len(truck.truck) != truck.capacity:
            for i in range(len(package_data.list)):

                if package_data.list[i] is not None and package_data.list[i] not in truck.truck and package_data.list[i][1].status == 'At HUB':

                    if len(truck.truck) != truck.capacity:

                        pkg_data = package_data.list[i]
                        pkg = package_data.list[i][1]
                        pkg_id = float(package_data.list[i][0])
                        notes = package_data.list[i][1].notes
                        delivery_time = package_data.list[i][1].delivery_time
                        address = package_data.list[i][1].address
                        pkgs_needed = [13,14,15,16,19,20]

                        if pkg_id in pkgs_needed:

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

            count += 1
    elif truck_number == 2:
        count = 0  # keeps track of each iteration of loading pkgs
        while len(truck.truck) != truck.capacity:
            for i in range(len(package_data.list)):

                if package_data.list[i] is not None and package_data.list[i] not in truck.truck and package_data.list[i][1].status == 'At HUB':

                    if len(truck.truck) != truck.capacity:

                        pkg_data = package_data.list[i]
                        pkg = package_data.list[i][1]
                        notes = package_data.list[i][1].notes
                        delivery_time = package_data.list[i][1].delivery_time
                        address = package_data.list[i][1].address

                        if notes == 'Can only be on truck 2':
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 1 and address in addresses_to_visit:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 2 and 'Delayed' in notes:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

                        elif count >= 3:
                            truck.add_package(pkg_data)
                            pkg.set_status('ON TRUCK TWO')
                            if address not in addresses_to_visit:
                                addresses_to_visit.append(address)

            count += 1
    elif truck_number == 3:
        count = 0  # keeps track of each iteration of loading pkgs
        while count < 1:
            for i in range(len(package_data.list)):

                if package_data.list[i] is not None and package_data.list[i] not in truck.truck and package_data.list[i][
                    1].status == 'At HUB':

                    if len(truck.truck) != truck.capacity:
                        truck.add_package(package_data.list[i])
                        package_data.list[i][1].set_status('ON TRUCK THREE')
                        if package_data.list[i][1].address not in addresses_to_visit:
                            addresses_to_visit.append(package_data.list[i][1].address)
            count += 1
    else:
        return 'Truck DNE'

    return truck, addresses_to_visit


def start_delivery(truck, package_data, distance_data, addresses_to_visit, time, total_miles=0):
    # addresses_to_visit = []
    #
    # for pkg in truck.truck:
    #     if pkg[1].address not in addresses_to_visit:
    #         addresses_to_visit.append(pkg[1].address)

    start_addr = 'HUB'
    delivery_addr = ''

    nearest_addr = 0
    visited_addresses = []

    while len(addresses_to_visit) != 0:
        for i in range(len(distance_data)):
            if distance_data[i][0] == start_addr:
                for addrs in distance_data[i][1]:
                    if addrs[0] in addresses_to_visit:
                        if float(addrs[1]) < nearest_addr or nearest_addr == 0:
                            nearest_addr = float(addrs[1])
                            delivery_addr = addrs[0]
                total_miles += nearest_addr
                addresses_to_visit.remove(delivery_addr)
                visited_addresses.append(delivery_addr)
                start_addr = delivery_addr
                nearest_addr = 0
                break
    # print(visited_addresses)
    return total_miles, truck,



def deliver_packages(package_data, distance_data, hour=8, min=0):
    # TODO: start time at 0 or 8:00
    # TODO: load and start delivery of truck one first and wait until 9:05 to let truck two leave
    # TODO: Once truck one is back at the hub let truck three go out for delivery
    # TODO: write a separate function for specific details about a package at certain time

    # if hour == 8 and min == 0:  # default start time,
    #     time = datetime.datetime(year=100,month=1,day=1,hour=8,minute=0)
    # else:  # time has been specified for a status at that time, run program until that specified time
    #     time = datetime.datetime(year=100,month=1,day=1,hour=hour,minute=min)
    # seconds = 103.666666667 * 60
    # b = time + datetime.timedelta(0, seconds)
    # print(b.time())

    time = datetime.datetime(year=100, month=1, day=1, hour=8, minute=0)

    # construct truck one to load
    truck_one = Truck()
    truck_two = Truck()
    truck_three = Truck()

    t1_addresses_to_visit = []
    t2_addresses_to_visit = []
    t3_addresses_to_visit = []

    # load each truck starting with truck 1
    load_truck(truck_one, package_data, t1_addresses_to_visit, 1)
    load_truck(truck_two, package_data, t2_addresses_to_visit, 2)
    load_truck(truck_three, package_data, t3_addresses_to_visit, 3)

    best_t1_route = two_opt(t1_addresses_to_visit, distance_data)
    t1_miles = cost(best_t1_route, distance_data)

    print('BEST ROUTE FOR T1:', best_t1_route)
    print('THE BEST DISTANCE FOR T1:', t1_miles)

    best_t2_route = two_opt(t2_addresses_to_visit, distance_data)
    t2_miles = cost(best_t2_route, distance_data)

    print('BEST ROUTE FOR T2:', best_t2_route)
    print('THE BEST DISTANCE FOR T2:', t2_miles)

    best_t3_route = two_opt(t3_addresses_to_visit, distance_data)
    t3_miles = cost(best_t3_route, distance_data)

    print('BEST ROUTE FOR T3:', best_t3_route)
    print('THE BEST DISTANCE FOR T3:', t3_miles)

    print('TOTAL MILEAGE USING 2-OPT:', t1_miles+t2_miles+t3_miles)

    # print(cost(t1_addresses_to_visit, distance_data))

    truck_one_miles = start_delivery(truck_one, package_data,  distance_data, t1_addresses_to_visit, time)[0]
    truck_two_miles = start_delivery(truck_two, package_data, distance_data, t2_addresses_to_visit, time)[0]
    truck_three_miles = start_delivery(truck_three, package_data, distance_data, t3_addresses_to_visit, time)[0]

    total_miles = truck_one_miles + truck_two_miles + truck_three_miles

    # print('Truck one miles:', truck_one_miles)
    # print(truck_one.truck)
    # print('Truck two miles:', truck_two_miles)
    # print('Truck three miles:', truck_three_miles)
    # print('Total Miles traveled:', total_miles, 'mi')

def two_opt(route, cost_data):
    route.insert(0,'HUB')
    route.append('HUB')
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - 1 == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                cost_one = cost(new_route, cost_data)
                cost_two = cost(best, cost_data)
                if cost_one < cost_two:
                    best = new_route
                    improved = True
        route = best
    return best



def cost(route, cost_data):
    start_addr = route[0]
    total_miles = 0
    visited_addr = []
    visited_addr.append(start_addr)
    count = 0

    while len(visited_addr) != len(route)-1:
        check = False
        for i in range(len(cost_data)):
            if check: break
            if cost_data[i][0] == start_addr:
                for addr in cost_data[i][1]:
                    if addr[0] == route[count+1]:
                        total_miles += float(addr[1])
                        visited_addr.insert(0,addr[0])
                        start_addr = addr[0]
                        count += 1
                        check = True
                        break

    return total_miles




