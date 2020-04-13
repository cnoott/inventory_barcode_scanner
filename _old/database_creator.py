#!/usr/bin/env python3
#Written by Liam Amadio
#09/19/2020
import time

newFile = open('database_reference.py','w+')
newFile.write('database = {')

while True:
    uid = input('Scan barcode (press enter when done): ')
    time.sleep(0.25)
    if uid == '':
        break
    name = input('Enter name of item and press enter: ')

    newFile.write('"{}":"{}",'.format(uid,name))

newFile.write('}')
