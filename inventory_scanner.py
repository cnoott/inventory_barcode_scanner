#Written by Liam Amadio
#01/12/2020
from collections import Counter
import csv
import datetime
import database_reference

input_list = []
num_of = []
inventory_dict = {}
print("Welcome to inventory_barcode_scanner V0.1\nBegin Scanning Items. Type enter when done: ")
while True: #Puts user input into input_list
    items = input(">> ")
    if items == "":
        break
    input_list.append(items)

for id in input_list: #Counts qty of unique items in input_list
    counter = 0
    if id not in num_of:
        num_of.append(id)
        for unique in input_list:
            if unique == id:
                counter = counter + 1
        inventory_dict[str(id)] = counter
print("File saved at","inventory_{}".format(datetime.date.today()))
print("barcode | quantity\n")

for keys in inventory_dict:
    print(keys,"      ",inventory_dict[keys])

#writing to new file
database = database_reference.database
#error prevention

with open("./inventories/inventory_{}.csv".format(datetime.date.today()), "w+") as output:
    output.write("uid,name,qty\n")
    for UID in num_of:
        for database_UID in database:
            if UID == database_UID:
                output.write("{},{},{}\n".format(UID,database[UID],inventory_dict[UID]))

