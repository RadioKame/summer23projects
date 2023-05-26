from item import Item


class Phone(Item):
    def __init__(self, name, price = 0, quantity = 0, broken_phones = 0):
        # call to super fucntion to have access to all attributes / methods
        super().__init__(
            name, price, quantity
            )