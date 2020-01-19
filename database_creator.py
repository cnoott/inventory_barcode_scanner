#Written by Liam Amadio
#09/19/2020

newFile = open('database_reference.py','w+')
newFile.write('database = {')

while True:
    uid = input('Scan barcode (press enter when done): ')
    if uid == '':
        break
    name = input('Enter name of item and press enter: ')

    newFile.write('"{}":"{}",'.format(uid,name))

newFile.write('}')
