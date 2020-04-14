from os import walk
from inventories import meta
import csv
from item import Item
directoryList = []

for r,d,f in walk("./inventories/{}".format(meta.lastPeriod)):
    for files in f:
        if files != "periodinfo.txt": #exclusing period info
            directoryList.append(files)


listofItems=[] #list of Item objects
for files in directoryList:
    itemList = []
    with open('./inventories/{}/{}'.format(meta.lastPeriod, files)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) #skips row with titles
        for row in csv_reader:
            itemList.append(Item(row[0],row[2],row[1]))
        listofItems.append(itemList)


sumItem = [] #an Item object list that contains the sum
tempUid = []

for lists in range(len(listofItems)):
    for items in listofItems[lists]:
        if items.uid not in tempUid:
            tempUid.append(items.uid)
            sumItem.append(Item(items.name,items.uid))


for items in sumItem:
    for lists in range(len(listofItems)):
        for qtys in listofItems[lists]:
            if items.uid == qtys.uid:
                items.qty = int(items.qty) + int(qtys.qty)

for items in sumItem:
    print(items.name, " : ",items.qty)


