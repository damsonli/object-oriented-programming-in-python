from turtle import Turtle
from random import randint

alice = Turtle()
alice.color('red')
alice.shape('turtle')
alice.penup()
alice.goto(-160, 100)
alice.pendown()

bob = Turtle()
bob.color('yellow')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()

cathy = Turtle()
cathy.color('blue')
cathy.shape('turtle')
cathy.penup()
cathy.goto(-160, 40)
cathy.pendown()

dave = Turtle()
dave.color('green')
dave.shape('turtle')
dave.penup()
dave.goto(-160, 10)
dave.pendown()

for movement in range (100):
    alice.forward(randint(1,5))
    bob.forward(randint(1,5))
    cathy.forward(randint(1,5))
    dave.forward(randint(1,5))

wait = input("PRESS ENTER TO CONTINUE...")