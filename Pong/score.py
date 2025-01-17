from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore, align="center",font=("Courier", 50,"normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 50, "normal"))