from item import Item

my_item = Item()

print("The item name is " + str(my_item.name))
print("The item desciprtion is " + str(my_item.description))
print("The item color is " + str(my_item.color))

my_item.name = "Apple"
my_item.description = "It's a tasty fruit."
my_item.color = "Red"

print("The item name is " + str(my_item.name))
print("The item desciprtion is " + str(my_item.description))
print("The item color is " + str(my_item.color))

my_item.name = "Banana"
my_item.description = "It's a fruit."
my_item.color = "Yellow"

print("The item name is " + str(my_item.name))
print("The item desciprtion is " + str(my_item.description))
print("The item color is " + str(my_item.color))
