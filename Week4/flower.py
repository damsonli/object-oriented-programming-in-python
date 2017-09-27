class Flower():

    # This is a class variable - it is shared between all objects of the class Flower
    picked = 0

    def __init__(self):
        # This is an instance variable, a different copy is stored once per object
        self.color = "red"

    def pick(self):
        # This is how we refer to a class variable - classname.varname
        Flower.picked += 1
    
    def get_status(self):
        print( str(Flower.picked) + " flowers have been picked")