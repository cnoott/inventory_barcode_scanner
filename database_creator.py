#Written by Liam Amadio
import time


while True:
    fileName = input("Enter name of database to create: ")
    if fileName != "":
        break
    else:
        print("Enter a valid name")

newFile = open('./databases/{}.csv'.format(fileName), 'w+')
newFile.write('name,uid\n')
while True:
    uid = input('Scan barcode (press enter when done): ')
    time.sleep(0.15)
    if uid == '':
        break
    name = input('Enter name of item and press enter: ')
    newFile.write('{},{}\n'.format(name,uid))

newFile.close()
