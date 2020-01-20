#!/usr/bin/env python
#Written by Liam Amadio
#01/12/2020
import csv
import datetime
import database_reference
import time

input_list = []
num_of = []
inventory_dict = {}
print("\nWelcome to inventory_barcode_scanner V1.1\n\nBegin Scanning Items. Type enter when done:")
while True: #Puts user input into input_list
    items = input(">> ")
    time.sleep(0.18)
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
#error prevention (checks if a UID doesnt have a name assigned to it in database)
for id in num_of:
    if id not in database:
        print("Error:",id, "not in database; given name 'no_name given'")
        database[id] = "no_name_given"

with open("./inventories/inventory_{}.csv".format(datetime.date.today()), "w+") as output:
    output.write("uid,name,qty\n")
    for UID in num_of:
        for database_UID in database:
            if UID == database_UID:
                output.write("{},{},{}\n".format(UID,database[UID],inventory_dict[UID]))

