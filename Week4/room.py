class Room():

    def __init__(self, room_name):
        self._name = room_name
        self._description = None
        self.linked_rooms = {}
        self._character = None
        self._item = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, room_name):
        self._name = room_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, room_description):
        self._description = room_description

    def describe(self):
        print( self._description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        print( "The " + self._name)
        separator = ""
        for i in range (0,20):
            separator += "-"
        print( separator)
        print( self._description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.name + " is " + direction)
        #print( "\n\n")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, room_char):
        self._character = room_char

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, room_item):
        self._item = room_item       