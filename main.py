from item import Item
#from phone import Phone
#Item.instantiate_from_csv()
#print(Item.all)


item1 = Item("MyItem", 750)

item1.apply_increment(0.2)
item1.apply_disccount()

print(item1.price)

#item1.read_only_name = "OtherItem"

