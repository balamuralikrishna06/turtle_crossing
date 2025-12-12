FONT = ("Courier", 20, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-230,230)
        self.write(f"Level: {self.level}",font=FONT,align="center")

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",font=FONT,align="center")
