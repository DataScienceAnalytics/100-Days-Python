import random
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score is: {str(self.score)}",False,"center",("Arial","12","normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score is: {str(self.score)}",False,"center",("Arial","12","normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER","center","center",("Arial","12","normal"))