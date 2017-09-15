from room import Room

# instantiate the object
kitchen = Room("Kitchen")

# print out properties right after the instantion
print("The room name is " + kitchen.name)
print("The room description is " + str(kitchen.description))

# assign and print the descrption
kitchen.set_description("A dank and dirty room buzzing with flies.")

kitchen.get_description()
kitchen.describe()

# Python does not need setters and getters, can call the properties directly
kitchen.description = "This is a new room description."
print(kitchen.description)

# essentially how Python saves this object with properties
print(kitchen.__dict__)
print(kitchen.__dict__['description'])

# more about @property, read https://www.programiz.com/python-programming/property