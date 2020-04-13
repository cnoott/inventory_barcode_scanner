#item class

class Item:
    def __init__(self, name='no name', uid = 'no_barcode', qty = 0):
        self.name = name
        self.qty = qty
        self.uid = uid

    def incrimentQty(self):
        self.qty += 1
