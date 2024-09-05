from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=self.score, align="center", font=("Courier", 80, "normal"))

    def point(self):
        self.score += 4
        self.update_scoreboard()

