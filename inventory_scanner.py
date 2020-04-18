from item import Item
from colorama import Fore, Back, Style
import csv
import os
import sys
from os import walk
import time
import datetime
from datetime import datetime
from datetime import date
import settings
#VARIABLE CONSTANTS
INVENTORY_DIR = "./inventories"



def createFolder():
    '''
    creates a new folder within the inventories directory in which new inventories will be stored. This also creates a meta file in which it will hold inventory names
    '''
    #Creates folder
    os.system('clear')
    print(Fore.GREEN + "  \n-= Inventory Barcode Scanner v2.3 =- \n" + Style.RESET_ALL)
    try:
        print(Fore.BLACK + Back.WHITE +"\nCREATE FOLDER" + Style.RESET_ALL)
        newFolderName = input("Enter name of new folder (type c to cancel): ")
        if newFolderName == 'c':
            print('canceled')
        else:
            os.mkdir("{}/{}".format(INVENTORY_DIR, newFolderName))

            #Writes  meta file that contains the last inventory name number
            newMeta = open("{}/{}/.meta.txt".format(INVENTORY_DIR, newFolderName),"w")
            newMeta.write("0") #remember to convert to int later on
            newMeta.flush(); newMeta.close()

            #Writes folder data file
            folderInfo = open("{}/{}/FOLDER_INFO.txt".format(INVENTORY_DIR,newFolderName),"w")
            folderInfo.write("FOLDER INFO\n===========\nDate Created: {}\n".format(date.today()))
            folderInfo.write("Inventory scans:\n")
            folderInfo.flush(); folderInfo.close()
            print("Folder '{}' successfully created".format(newFolderName))
            time.sleep(1.5)
    except:
        print("Folder name already exists. Try again")
        createFolder()



def chooseFolder():
    '''
    lists folders in inventories directory and returns chosen folder as string
    '''
    print(Fore.GREEN + "  \n-= Inventory Barcode Scanner v2.3 =- \n" + Style.RESET_ALL)
    directoryList = []
    for r, d, f in walk("{}/".format(INVENTORY_DIR)): #stores avaliable directories in list
        directoryList.extend(d)
        break
    x = 1
    print(Fore.BLACK + Back.WHITE + "CHOOSE FOLDER" + Style.RESET_ALL)
    for folder in directoryList:
        print("{}. {}".format(x,folder))
        x += 1
    while True:
        chosenDir = int(input("Choose a folder to start scanning in: "))
        if chosenDir-1 not in range(len(directoryList)):
            print("Invalid option, try again")
        else:
            directory = directoryList[chosenDir - 1]
            break
    os.system('clear')
    return directory


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

def scanItems():

    chosenDir = chooseFolder()
    itemList = []

    with open('./databases/{}'.format(settings.currentDatabase)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) #skips row with name,uid
        for row in csv_reader:
            itemList.append(Item(row[0],row[1])) #creates list of Item objects


    #scanning
    uidList = [] #input goes here
    os.system('clear')
    print(Fore.GREEN + "  \n-= Inventory Barcode Scanner v2.3 =- \n" + Style.RESET_ALL) #title
    print("BEGIN SCANNING")
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
                print(Fore.RED+"Error:"+Style.RESET_ALL + " Barcode ", uid, "not in database; given name 'no_name'")
                contin = input("Press ENTER to continue")

    for uid in uidList:
        for item in itemList:
            if uid == item.uid:
                item.incrimentQty()

    meta = open("{}/{}/.meta.txt".format(INVENTORY_DIR,chosenDir),"r")
    num = meta.readline()
    meta.close()
    newMeta = open("{}/{}/.meta.txt".format(INVENTORY_DIR,chosenDir),"w") #updates file
    num = int(num) + 1 #determines name for inventory file 
    newMeta.write("{}".format(num))
    newMeta.close()

    #writing to file    
    with open("{}/{}/inventory_{}.csv".format(INVENTORY_DIR,chosenDir, num),"w+") as output: 
        output.write("name,qty,uid\n")
        openFile = open("{}/{}/FOLDER_INFO.txt".format(INVENTORY_DIR,chosenDir), 'a+') #adds meta info to periodinfo.txt
        now = datetime.now(); dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        openFile.write("inventory_{} created:: {}\n".format(num,dt_string) )
        openFile.flush()
        openFile.close()


        for item in itemList:
            output.write("{},{},{}\n".format(item.name,item.qty,item.uid))

    print("inventory_{}.csv successfully created".format(num))
    time.sleep(1.5)
    sumFolder(chosenDir)


def updateFolder(chosenDir): #unused for now, may impliment later onced fixed but for now its redundatn
    '''
    updates folder with LAST ACCESSED. This will be called in the scanItems() function
    '''
    with open("{}/{}/FOLDER_INFO.txt".format(INVENTORY_DIR,chosenDir),'r') as contents:
        save = contents.read()[1:]

    with open("{}/{}/FOLDER_INFO.txt".format(INVENTORY_DIR,chosenDir),'w') as contents:
        contents.write("Last Inventory Scanned: {}\n".format(date.today()))

    with open("{}/{}/FOLDER_INFO.txt".format(INVENTORY_DIR,chosenDir),'a') as contents:
        contents.write(save)


def sumFolder(chosenDir):
    '''
    Takes all of the inventory files in a chosen directory and creates a main file with the sum of all inventory quantities. Will be called in scanItems() function
    '''
    directoryList = []
    for r,d,f in walk("{}/{}".format(INVENTORY_DIR,chosenDir)):
        for files in f:
            if files != "FOLDER_INFO.txt" and files !="sum_of_inventories.csv": #exclusing period info
                directoryList.append(files)


    listofItems=[] #list of Item objects
    for files in directoryList:
        itemList = []
        with open('{}/{}/{}'.format(INVENTORY_DIR,chosenDir, files)) as csv_file:
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


    outFile = open('./{}/{}/sum_of_inventories.csv'.format(INVENTORY_DIR,chosenDir),'w')
    outFile.write('name,qty,uid\n')
    for items in sumItem:
        outFile.write('{},{},{}\n'.format(items.name,items.qty,items.uid))
    outFile.close()



while True:
    os.system('clear') 
    print(Fore.GREEN + "  \n-= Inventory Barcode Scanner v2.3 =- \n" + Style.RESET_ALL)
    if settings.currentDatabase == "":
        print(Fore.RED + "WARNING:" + Style.RESET_ALL+" No database detected, please run database_creator.py")

    if not os.listdir(INVENTORY_DIR):
        print(Fore.RED + "WARNING:" + Style.RESET_ALL + " No folders detected, select option 2 to create a new folder\n")

    #put error handlign for no folder
    option = input("1. Start Scanning 2. Create new folder 3. settings 4. Help 5. Exit\n Choose an option and press ENTER: ")
    if option == "1":
        os.system('clear')
        if not os.listdir(INVENTORY_DIR):
            print(Fore.RED + "ERROR:"+ Style.RESET_ALL + " no new folder created, select option 2 to create a new folder")
        else:
            scanItems()
    elif option == "2":
        os.system('clear')
        createFolder()
    elif option == "3":
        os.system('clear') 
        changeDatabase()

    elif option == "4":
        print("HELP PAGE:\n To start scanning, type 1 and press enter\n\n To create a new folder type 2 and press enter.\n")

        contin = input("Press ENTER to continue")
    elif option == "5":
        exit()
    else:
        print("Invalid option, try again")



