class Package:
    """
    A class to create a package object that then gets
    stored into a hash table and truck object.
    """
    def __init__(self,
                 package_id='',
                 address='',
                 city='',
                 state='',
                 zipcode='',
                 delivery_time='',
                 weight='',
                 status='',
                 notes=''):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_time = delivery_time
        self.weight = weight
        self.status = status
        self.notes = notes

    def set_id(self, package_id):
        self.package_id = package_id

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    def set_status(self, status):
        self.status = status

    def set_notes(self, notes):
        self.notes = notes

    def __repr__(self):
        return "Package Info - ID: {0}, " \
               "ADDRESS: {1}, " \
               "CITY: {2}, " \
               "STATE: {3}, " \
               "ZIP: {4}, " \
               "DELIVERY TIME: {5}, " \
               "WEIGHT: {6}, " \
               "STATUS: {7}, " \
               "NOTES: {8}".format(self.package_id,
                                   self.address,
                                   self.city,
                                   self.state,
                                   self.zipcode,
                                   self.delivery_time,
                                   self.weight,
                                   self.status,
                                   self.notes)
