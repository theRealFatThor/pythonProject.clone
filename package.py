# package class object
import csv
import datetime
import hash

hashtable = hash.ChainingHashTable()


class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight, status, delivery_time,
                 special_notes):
        self.id = package_id  # int
        self.address = address  # string
        self.city = city  # string
        self.state = state  # string
        self.zip = zip_code  # int
        self.delivery_deadline = delivery_deadline  # datetime object
        self.weight = weight  # int
        self.status = status  #Using a string for now,,, set to 'HUB'
        self.delivery_time = delivery_time  # datetime object, possible set to None
        self.special_notes = special_notes
        self.departure_time = None

    def __str__(self):  # Overrides printing the address
        return "ID: %d, Address: %s, City: %s, ST: %s, Zip: %d, Deadline: %s, Weight: %d, Notes: %s" % (
        self.id, self.address, self.city, self.state, self.zip, self.delivery_deadline, self.weight,
        self.special_notes)

    def get_status_for_time(self, user_requested_time):
        #use if statements to figure the status between self.delivertime, user_requested_time, and self.departure_time
        if (user_requested_time > self.departure_time) and (user_requested_time < self.delivery_time):
            return 'Status: En Route'
        elif user_requested_time >= self.delivery_time:
            return 'Status: Delivered - %s' % (self.delivery_time)
        return 'Status: HUB'

# takes package csv file and loads the package data as package objects into the hash table.
def loadPackageData(filename):
    with open(filename) as packageList:
        packageData = csv.reader(packageList, delimiter=',')
        next(packageData)  # skipping headers
        for row in packageData:
            pID = int(row[0])
            pAddress = row[1]
            pCity = row[2]
            pState = row[3]
            pZip = int(row[4])
            pDeliveryDeadline = row[5]
            pWeight = int(row[6])
            pStatus = ''
            pDeliveryTime = datetime.time(0, 0, 0)
            pSpecialNote = row[7]

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeliveryDeadline, pWeight, pStatus, pDeliveryTime,
                        pSpecialNote)

            hashtable.insert(pID, p)
        return hashtable
