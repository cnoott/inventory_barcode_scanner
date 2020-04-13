#item class

class Item:
    def __init__(self, name='no name', qty = 0, uid = 'no barcode'):
        self.name = name
        self.qty = qty
        self.uid = uid

    def incrimentQty(self):
        self.qty += 1
