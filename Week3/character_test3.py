from character import Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.conversation = "Hello there, can I eat you?"

dave.describe()
dave.talk()

dave.weakness = "cheese"
print(dave.weakness)

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)