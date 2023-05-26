import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name, price = 0, quantity = 0):
        # Run validations to the received arguments
        #assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        #assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'
        
        # Atributes
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_disccount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        #return self.name, self.price, self.quantity

    @classmethod
    def instantiate_from_csv(cls): # cls = class method
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f) # DictReader = dictionary reader
            items = list(reader) # list = convert reader to list

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    
    @staticmethod        
    def is_integer(num):
        # we will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
                

class Phone(Item):
    def __init__(self, name, price = 0, quantity = 0, broken_phones = 0):
        # call to super fucntion to have access to all attributes / methods
        super().__init__(
            name, price, quantity
            )





        
phone1 = Phone('iPhone', 1000, 5, 1)

print(Item.all)
print(Phone.all)
















#print(Item.is_integer(7.0))
#print(Item.is_integer(7.5))

#Item.instantiate_from_csv()
# print name of the object in all instances
#print([(instance.name, instance.price, instance.quantity) for instance in Item.all])

#print(Item.all)

# print name of the object in all instances
#for instance in Item.all:
#    print(f"'{instance.name}', {instance.price}, {instance.quantity}")
    


# why I'm getting no such file or directory error?

