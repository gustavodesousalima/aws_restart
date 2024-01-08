myInventoryList = []

import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():

    print("{} : {}".format(key, value))
    
    
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    linecount = 0
    for row in csvReader:
        if linecount == 0:
            print(f'column names are: {", ".join(row)}')
            linecount += 1
            
        else:
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            linecount += 1
            print(f'Processed {linecount} lines.')
        
        
    for myCarProperties in myInventoryList:
        print('-------------------------------')
        for key, value in myCarProperties.items():
            print('{} : {}'.format(key, value))
        