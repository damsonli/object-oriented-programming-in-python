# This class is created by pythonic @property style

class Item():

    def __init__(self):
        self._name = None
        self._description = None
        self._color = None
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, item_name):
        self._name = item_name
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, item_description):
        if len(item_description) >= 20:
            print("The description cannot be more than 20 characters")
        else:
            self._description = item_description

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, item_color):
        self._color = item_color