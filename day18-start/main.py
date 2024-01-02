# from turtle import Turtle, Screen
# tim = Turtle()
# tim.shape("turtle")
# tim.color("blue")
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# import turtle
# tim = turtle.Turtle()
import random
# from (module) import (class from module) vs import (class)

import turtle as t

#import heroes
#you can move your cursor to the module to install a package with something that's not installed!

# Challenge 2 - draw a dashline

# from turtle import Turtle, Screen
# tim = Turtle()
# for _ in range(100):
#     tim.forward(1)
#     tim.up()
#     tim.forward(1)
#     tim.down()
#
#
# screen = Screen()
# screen.exitonclick()

# challenge 3 - Draw different shapes
# from turtle import Turtle, Screen
# tim = Turtle()
#
# for i in range(3,9):
#     for _ in range(i):
#         tim.forward(50)
#         tim.right(360/i)
#
# screen = Screen()
# screen.exitonclick()

# Challenge 4 = random walk
# from turtle import Turtle, Screen
# tim = Turtle()
# colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue"]
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed("fastest")
# for i in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()

# Challenge 5 - Drawing Spirograph
from turtle import Turtle, Screen
tim = Turtle()
colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue"]
tim.speed("fastest")
for i in range(72):
    tim.color(random.choice(colors))
    tim.circle(50)
    tim.setheading(i*360/72)


screen = Screen()
screen.exitonclick()
