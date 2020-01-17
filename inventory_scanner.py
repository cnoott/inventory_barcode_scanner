#Written by Liam Amadio
#01/12/2020
from collections import Counter
import csv

input_list = []
num_of = []
inventory_dict = {}

while True: #Puts user input into input_list
    items = input("Begin Scanning Items. Type enter when done.")
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
print(inventory_dict)

file = open('output.csv',"w+")
file.write("barcode,quantity\n")
for keys in inventory_dict:
    file.write("{},{}\n".format(keys,inventory_dict[keys]))
            
        

