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
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    @property
    def price(self):
        return self.__price
    
    def apply_disccount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
        
    @property
    # Property Decorator = Read-Only Attribute '__atribute'
    def name(self):
        print('Your are trying to access the name')
        return self.__name
    
    #@name.setter
    ## Setter Decorator = Write-Only Attribute '__atribute'
    #def name(self, value):
    #    self.__name = value
    
    
    
    
        
    def calculate_total_price(self):
        return self.__price * self.quantity


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
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
        

        
        