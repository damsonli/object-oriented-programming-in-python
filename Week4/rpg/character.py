class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self._name = char_name
        self._description = char_description
        self._conversation = None

    # Describe this character
    def describe(self):
        print( self._name + " is here!" )
        print( self._description )

    # Set what this character will say when talked to
    @property
    def conversation(self):
        return self._conversation

    @conversation.setter
    def conversation(self, new_conversation):
        self._conversation = new_conversation

    # Talk to this character
    def talk(self):
        if self._conversation is not None:
            print("[" + self._name + " says]: " + self._conversation)
        else:
            print(self._name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self._name + " doesn't want to fight with you")
        return True

# Add a sub class
class Enemy(Character):

    num_defeated_enemy = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._weakness = None

    @property
    def weakness(self):
        return self._weakness

    @weakness.setter
    def weakness(self, char_weakness):
        self._weakness = char_weakness

    # Fight with an enemy
    def fight(self, combat_item):
        if combat_item == self._weakness:
            print("Your fend " + self._name + " off with the " + combat_item)
            return True
        else:
            print(self._name + " crushes you, puny adventurer")
            return False

    def steal(self):
        print("You steal from " + self._name)

class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._feeling = None
    
    def hug(self):
        print(self._name + " hugs you back!")
