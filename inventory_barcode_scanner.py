from item import Item
import csv
import os
from inventories import meta
from datetime import date

def scanItems():
    itemList = []
    directoryList = []
    for r, d, f in walk("./databases/"): #creates list of file in directory
        directoryList.extend(f)
        break

    print("Choose database to scan from: ")
    for files in directoryList:
        print("1. ",files)

    chosenFile = input("Type in the number of the database you want to access")

    with open('./databases/{}'.format(directoryList[int(chosenFile)-1])) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            itemList.append(Item(row[0],row[1])) #creates list of Item objects


    #scanning
    uidList = [] #input goes here
    while True:
       uid = input(">> ")
       time.sleep(0.14)
       if uid == "":
           break
       uidList.append(uid)

    for i in size(uidList):
        print(i)


def endPeriod():
    '''
    ends period and modifies periodinfo.txt
    '''
    if meta.lastPeriod == "":
        pass
    else:
        print("Ending period...")
        oldFile = open("./inventories/{}/periodinfo.txt".format(meta.lastPeriod), 'a+')
        today = date.today()
        oldFile.write("DATE ENDED: {} ".format(today))
        oldFile.close()

def newPeriod():
    '''
    creates new folder and modifies meta.py
    '''
    newPeriodName = input("Enter name of new period:")
    newMeta = open("./inventories/meta.py","w")
    newMeta.write("lastPeriod = '{}'".format(newPeriodName)) #overwrite old meta file
    newMeta.close()
    os.mkdir("./inventories/{}".format(newPeriodName))
    periodInfo = open('./inventories/{}/periodinfo.txt'.format(newPeriodName), 'w')
    today = date.today() #gets current date
    periodInfo.write("PERIOD INFO\nDATE CREATED:{}".format(today))




option = input("1. Start Scanning 2. Start a new period 3. Help\n Choose an option: ")

while True:
    if option == "1":
        scanItems()
        break
    elif option == "2":
        endPeriod()
        newPeriod()
        break
    elif option == "3":
        print("HELP PAGE:\n To start scanning, type 1 and press enter\n To start a new inventory scan period type 2 and press enter.\n")
        print("WHAT IS A SCAN PERIOD?: A scan period is a folder than contains all the scans done within the specified period, including a master file that contains the sum of all scans done within said period. Creating a new period stops the current one, creating a new folder that will contain the next scan period.")
        break
    else:
        print("Invalid option, try again")
        break



