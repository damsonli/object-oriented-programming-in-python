# This file is to create a turtle race game, but concise codes with list

from turtle import Turtle
from random import randint

turtle_colors = ['red', 'yellow', 'blue', 'green']
turtles = []

vPos = 100

for turtlecolor in turtle_colors:
    t = Turtle()
    t.color(turtlecolor)
    t.shape('turtle')
    t.penup()
    t.goto(-160, vPos)
    t.pendown()

    vPos -= 30

    turtles.append(t)

for movement in range (100):
    for turtle in turtles:
        turtle.forward(randint(1,5))

wait = input("PRESS ENTER TO CONTINUE...")