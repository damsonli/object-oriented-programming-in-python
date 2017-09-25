# This file is to use shapes class and darw shapes

from shapes import Triangle, Oval, Rectangle

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(300)
rect1.set_color("blue")
rect1.draw()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(100)
rect2.set_y(100)
rect2.draw()

oval1 = Oval()
oval1.randomise()
oval1.draw()

