class Truck:
    """
    A class used to create a truck object that will hold a
    package object.
    """
    def __init__(self):
        self.truck = []
        self.speed = 18
        self.miles = 0
        self.capacity = 16
        self.status = 'At HUB'

    def add_package(self, package):
        self.truck.append(package)

    def remove_package(self, package):
        self.truck.remove(package)

    def add_miles(self, miles):
        self.miles += miles

    def set_status(self, status):
        self.status = status
