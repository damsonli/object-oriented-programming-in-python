from room import Room

# instantiate the object
kitchen = Room("Kitchen")
dining_hall = Room("Dining Hall")
ballroom = Room("Ballroom")

# assign and print the descrption
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# link rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
