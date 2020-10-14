class Truck:
    def __init__(self):
        self.truck = []
        self.speed = 18
        self.miles = 0
        self.capacity = 16

    def add_package(self, package):
        self.truck.append(package)
        self.capacity -= 1

    def remove_package(self, package):
        self.truck.remove(package)
        self.capacity += 1

    def add_miles(self, miles):
        self.miles += miles
