from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]


# tim1 = Turtle(shape = "turtle")
# tim1.color(colors[0])
# tim1.penup()
# tim1.goto(x=-230,y=-100)
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=-150+i*50)
    all_turtles.append(new_turtle)

import random
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner!")
            else:
                print("you've lost")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()