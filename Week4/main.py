from room import Room
from character import Enemy, Friend
from item import Item

# creat rooms
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

# create characters
dave = Enemy("Dave", "A smelly zobmie")
dave.conversation = "Brrlgrh... rhrhl... brains..."
dave.weakness = "cheese"

ava = Enemy("Ava", "A beautilful fox")
ava.conversation = "Hello..."
ava.weakness = "sword"

catrina = Friend("Catrina", "A friendly skeleton")
catrina.conversation = "Why hello there."

# create item
cheese = Item("cheese", "A big smelly block of cheese")
sword = Item("sword", "A good-decarated sword")

# start the game
backpack = []
current_room = kitchen

kitchen.character = ava
dining_hall.character = dave
ballroom.character = catrina
kitchen.item = cheese
ballroom.item = sword

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.character
    item = current_room.item

    # check if there is character and item in current room
    # if yes, print description
    # if no, do nothing
    if inhabitant is not None:
        inhabitant.describe()
    
    if item is not None:
        item.describe()

    command = input("> ").lower()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "list":
        if len(backpack) == 0:
            print("You have nothing now. Explorer rooms and take some items.")
        else:
            print("Here what you have: ")
            for each in backpack[:-1]:
                print(each, end=", ")
            print(backpack[-1])
    elif command == "take":
        backpack.append(current_room.item.name)
        print("You just put " + current_room.item.name + " in your backpack. Use <list> command to see what you have.")
        current_room.item = None
        #print(current_room.item)
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
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == False:
                        print("You lose...")
                        print("Try again")
                    else:
                        backpack.remove(fight_with)
                        current_room.character = None
                        Enemy.num_defeated_enemy += 1
                        print("The number of enemies you fent off: " + Enemy.num_defeated_enemy)
                        if Enemy.num_defeated_enemy == 2:
                            print("Congratulations!! You won!!! Thanks for playing.")
                            break
                else:
                    print("You don't have it. Stop the fight.")
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
        print("Valid options: ")
        for key in current_room.linked_rooms:
            print(key, end = ", ")
        print("list, take, talk, fight, hug, exit, or quit")
