from room import Room
from character import Enemy, Friend

# instantiate the object
kitchen = Room("Kitchen")
dining_hall = Room("Dining Hall")
ballroom = Room("Ballroom")

# assign and print the descrption
kitchen.description = "A dank and dirty room buzzing with flies."
dining_hall.description = "A large room with ornate golden decorations on each wall."
ballroom.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."

# link rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# create a character
dave = Enemy("Dave", "A smelly zobmie")
dave.conversation = "Brrlgrh... rhrhl... brains..."
dave.weakness = "cheese"

# start the game
current_room = kitchen
dining_hall.character = dave

# Add a new character
catrina = Friend("Catrina", "A friendly skeleton")
catrina.conversation = "Why hello there."
ballroom.character = catrina

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.character
    if inhabitant is not None:
        inhabitant.describe()
    
    command = input("> ").lower()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is nobody here to talk")
    elif command == "fight":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy) == True:
                print("What will you fight with?")
                fight_with = input()
                #dave.fight(fight_with)
                if inhabitant.fight(fight_with) == False:
                    print("You lose...")
                    break
            else:
                print("Why you'd like fight with a friend?")
        else:
            print("There is nobody here to fight")  
    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend) == True:
                inhabitant.hug()
            else:
                print("You cannot hug an enemy")
        else:
            print("There is nobody here to hug")
    elif command in ["exit", "quit"]:
        print("Thanks for playing")
        break
    else:
        print("Valid options: north, south, east, west, talk, fight, hug, exit, or quit")
