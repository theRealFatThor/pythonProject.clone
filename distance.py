import csv

class distance:
    pass

def loadDistanceData(fileName):
    addressDistance = []
    with open(fileName, mode='r', encoding='utf-8-sig') as distanceList:
        distanceData = csv.reader(distanceList)
        for row in distanceData:
            addressDistance.append(row)
    return addressDistance

def findDistance(list, a, b):
    for row in list:
        if a in row:
            rowindex = list.index(row)
        elif a == -1:
            print("Data error")
        if b in row:
            bindex = list.index(row)
        elif b == -1:
            print("Data error")
    if list[rowindex][bindex + 1] == '':
        return float(list[bindex][rowindex + 1])
    else:
        return float(list[rowindex][bindex + 1])


