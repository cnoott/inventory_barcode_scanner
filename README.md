# Inventory Barcode Scanner v2.3

Inventory Barcode Scanner is command line interface inventory keeping utility that allows the user to:
- Create their own database of barcodes and respective names
- scan items from a HID barcode scanner and store inventory scans in CSV format
- and much more as seen in the "Features" section.

## Installation

Inventory Barcode Scanner requires no additional python packages to operate.
To install, simply open terminal and:

1. Change directory to your prefered folder

```bash
cd ~/user/Desktop/
```

2. Clone the repo (this downloads the program)

```bash
git clone https://github.com/cnoott/inventory_barcode_scanner.git
```

3. Change directory to the program folder

```bash
cd ./inventory_barcode_scanner
```

## Usage

This program is split into two parts: database_creator.py and inventory_scanner.py

1. Run database creator so that your barcodes can be named in the output file. This is stored in the databases folder

```bash
python3 database_creator.py
```

2. Afterwards, run inventory_scanner.py to start scanning barcodes.
```bash
python3 inventory_scanner.py
```

## Features

One of the key features of this program is creating folders that contain meta data of said folder. This data includes:
 - FOLDER_INFO.txt that contains information such as date created,  as well as the time and date at which each inventory was done.
 - sum_of_inventories.csv which contains the sum of the qty of all inventory items scanned in that folder. 


