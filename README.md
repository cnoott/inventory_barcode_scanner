<h1 align=center> Inventory barcode scanner v1.0 </h1>
<p align=center> Created by Liam Amadio </p>

### Description
This program is designed to:
- Create a database of UIDs and thier respective names.
- Count the amount of each UID in inventory via barcode scanner
- Output to a excel-readable CSV file with the current date.

### Installation Instructions
Requirements: 
 - Python3
 - git

* Clone the repo

    git clone https://github.com/cnoott/inventory_barcode_scanner.git
* change directory into it

    cd ./inventory_barcode_scanner

### Usage
* Run the database creator so that your barcodes can be named in the output file.

    python3 database_creator.py
* Run the inventory scanner to begin counting inventory.

    python3 inventory_scanner.py

* The program then outputs the inventory CSV to a folder named inventories.
