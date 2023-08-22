# Sam Miranda, 001144463
import hash
import distance
import package
import truck
import datetime
import csv

if __name__ == '__main__':
    packageHash = hash.ChainingHashTable()
    packageHash = package.loadPackageData('WGUPS Package File.csv')

    aDistances = []
    aDistances = distance.loadDistanceData('WGUPS Distance Table.csv')


    truck1 = truck.Truck()
    truck1.truckid = 1
    truck1.packages = [1, 6, 17, 24, 25, 26, 28, 29, 31, 32, 33, 34, 40]
    truck1.starting_time = datetime.time(hour=9, minute=5)

    truck2 = truck.Truck()
    truck2.truckid = 2
    truck2.packages = [3, 13, 14, 15, 16, 18, 19, 20, 30, 37, 36, 38]
    truck2.starting_time = datetime.time(hour=8, minute=0)

    truck3 = truck.Truck()
    truck3.truckid = 3
    # manual update of the package #9 address update updated at 10:20AM
    packageHash.search(9).address = '410 S State St'
    truck3.packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 21, 22, 23, 27, 35, 39]
    truck3.starting_time = datetime.time(hour=10, minute=20)

    # Attempt at Greedy Algo
    def short_distance(plist, a):
        l = {}
        for package in plist:
            goingto = packageHash.search(package).address
            leg = distance.findDistance(aDistances, a, goingto)
            l.update({package: leg})
        return (min(l, key=l.get))

    #creates a list of the all addresses from the last starting point
    def truck_shortest_path(truck_list):
        start = 'HUB'
        plist = []
        remaining_packages = truck_list.copy()
        while remaining_packages:
            #adds to the list the shortest distance to the next
            node = short_distance(remaining_packages, start)
            plist.append(node)
            # sets current package address as the next iteration
            start = packageHash.search(node).address
            remaining_packages.remove(node)
        return(plist)


    # Make a list of the distance and the time
    def deliver_packages(the_truck):
        start = 'HUB'
        total_distance = 0.0
        current_time = the_truck.starting_time
        best_route = truck_shortest_path(the_truck.packages)
        for delivery in best_route:
            # sets the first address to visit
            goingto = packageHash.search(delivery).address
            # calculates the "leg" of the trip by taking current stop to next stop
            leg = distance.findDistance(aDistances, start, goingto)
            # tallies amount of distance
            total_distance = total_distance + leg
            start = goingto
            # takes amount of miles traveled and divides by 0.3 (0.3 miles per minute)
            delta = datetime.timedelta(minutes=(leg/0.3))
            # adds date to time object so delta can be added
            current_time = (datetime.datetime.combine(datetime.date(1, 1, 1), current_time) + delta).time()
            package_to_update = packageHash.search(delivery)
            package_to_update.delivery_time = current_time
            package_to_update.status = 'Delivered'
            package_to_update.departure_time = the_truck.starting_time
            package_to_update.truck_id = the_truck.truckid
        the_truck.mileage = total_distance

    # Delivering the packages
    deliver_packages(truck1)
    deliver_packages(truck2)
    deliver_packages(truck3)

    def print_package_deliveries(the_truck, user_time):
        for delivered in the_truck.packages:
            p = packageHash.search(delivered)
            print(p, p.get_status_for_time(user_time), 'Truck ID:', the_truck.truckid)

    def print_apackage_delivery(a, user_time):
        p = packageHash.search(a)
        print(p, p.get_status_for_time(user_time), 'Truck ID:', p.truck_id)

    # Adds all the mileage from all trucks
    total_truck_mileage = truck1.mileage + truck2.mileage + truck3.mileage

    print('****************Welcome to WGUPS Package Deliver Service****************')
    print('Packages were successfully delivered with a total mileage of **', total_truck_mileage, '**!!!')

    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1. Get All Package Data by Time")
        print("2. Find Status/Data of single package")
        print("3. Exit the Program")
        option = input("Chose an option (1,2 or 3): ")
        if option == "1":
            print('Please enter time in Military time, (HH)[ENTER], (MM)[ENTER] ')
            user_requested_time = datetime.time(hour=int(input('Please enter hour:')), minute=int(input('Enter minutes:')))
            print_package_deliveries(truck1, user_requested_time)
            print_package_deliveries(truck2, user_requested_time)
            print_package_deliveries(truck3, user_requested_time)
        elif option == "2":
            print('Please enter time in Military time, (HH)[ENTER], (MM)[ENTER] ')
            user_requested_time = datetime.time(hour=int(input('Please enter hours:')), minute=int(input('Enter minutes:')))
            package_id = int(input('Please enter package id:'))
            print_apackage_delivery(package_id, user_requested_time)
        elif option == "3":
            isExit = False
        else:
            print("Wrong option, please try again!")