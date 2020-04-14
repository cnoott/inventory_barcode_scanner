from item import Item
import csv
import os
import sys
from os import walk
import time
import datetime
from datetime import datetime
from datetime import date
from inventories import meta
import settings
def changeDatabase():
    directoryList = []
    for r, d, f in walk("./databases/"): #creates list of file in directory
        directoryList.extend(f)
        break
    print("Choose database to scan from: ")
    x = 1
    for files in directoryList:
        print(x, files)
        x += 1
    chosenFile = input("Type the number of the database you want to access")
    writeFile = open('./settings.py','w')
    writeFile.write("currentDatabase = '{}'".format(directoryList[int(chosenFile)-1]))
    writeFile.close()
    python = sys.executable #restarts program
    os.execl(python, python, * sys.argv)

def scanItems():
    itemList = []

    with open('./databases/{}'.format(settings.currentDatabase)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) #skips row with name,uid
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

    for uid in uidList: #error prevention: for when theres a barcode that isnt within the database
            counter = 0
            for item in itemList:
                if uid == item.uid:
                    counter += 1
            if counter == 0:
                itemList.append( Item('no name',uid))
                print("Error: ", uid, "not in database; given name 'no_name'")

    for uid in uidList:
        for item in itemList:
            if uid == item.uid:
                item.incrimentQty()

    #writing to file
    newnumInv = meta.numInv + 1
    with open("./inventories/{}/inventory_{}.csv".format(meta.lastPeriod, newnumInv),"w+") as output: 
        output.write("name,qty,uid\n")
        metaFile = open("./inventories/meta.py","w") #updates meta file with new numInv value
        metaFile.write("lastPeriod = '{}'\n".format(meta.lastPeriod))
        metaFile.write("numInv = {}\n".format(newnumInv))
        metaFile.flush()
        metaFile.close()
        openFile = open("./inventories/{}/periodinfo.txt".format(meta.lastPeriod), 'a+') #adds meta info to periodinfo.txt
        now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        openFile.write("inventory_{} created:: {}\n".format(newnumInv,dt_string) )
        openFile.flush()
        openFile.close()

        for item in itemList:
            output.write("{},{},{}\n".format(item.name,item.qty,item.uid))


def endPeriod():
    '''
    ends period and modifies periodinfo.txt
    '''
    from inventories import meta
    if meta.lastPeriod == "":
        pass
    else:
        print("Ending period...")
        oldFile = open("./inventories/{}/periodinfo.txt".format(meta.lastPeriod), 'a+')
        today = date.today()
        oldFile.write("DATE ENDED: {} ".format(today))
        oldFile.flush()
        oldFile.close()

def newPeriod():
    '''
    creates new folder and modifies meta.py to include new period name
    '''
    newPeriodName = input("Enter name of new period:")
    newMeta = open("./inventories/meta.py","w")
    newMeta.write("lastPeriod = '{}'\n".format(newPeriodName)) #overwrite old meta file
    newMeta.write("numInv = 0\n")
    newMeta.flush()
    os.fsync(newMeta.fileno())
    newMeta.close()
    os.mkdir("./inventories/{}".format(newPeriodName))

    periodInfo = open('./inventories/{}/periodinfo.txt'.format(newPeriodName), 'w') #initializes periodinfo.txt 
    today = date.today() #gets current date
    periodInfo.write("PERIOD INFO\nDATE CREATED:{}\n".format(today))
    periodInfo.write("Inventory scans:\n")
    periodInfo.flush()
    periodInfo.close()
    #restarting program
    python = sys.executable
    os.execl(python, python, * sys.argv)





while True:
    option = input("1. Start Scanning 2. Start a new period 3. Change database 4. Help\n Choose an option: ")
    if option == "1":
        scanItems()
        break
    elif option == "2":
        endPeriod()
        newPeriod()
    elif option == "3":
        changeDatabase()
    elif option == "4":
        print("HELP PAGE:\n To start scanning, type 1 and press enter\n To start a new inventory scan period type 2 and press enter.\n")
        print("WHAT IS A SCAN PERIOD?: A scan period is a folder than contains all the scans done within the specified period, including a master file that contains the sum of all scans done within said period. Creating a new period stops the current one, creating a new folder that will contain the next scan period.")
        break
    else:
        print("Invalid option, try again")


