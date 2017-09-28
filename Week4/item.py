# This class is created by pythonic @property style

class Item():

    def __init__(self, item_name, item_description):
        self._name = item_name
        self._description = item_description
    
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
        self._description = item_description

    # Describe this item
    def describe(self):
        print( self._name + " is found in this room!" )
        print( self._description )
