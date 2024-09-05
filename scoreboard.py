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
        self.goto(100, 225)
        display_score = "Score: " + str(self.score)
        self.write(arg=display_score, align="center", font=("Courier", 30, "normal"))

    def message(self, display_text):
        self.clear()
        self.goto(0, 0)
        self.write(arg=display_text, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 225)
        display_score = "Score: " + str(self.score)
        self.write(arg=display_score, align="center", font=("Courier", 30, "normal"))

    def point(self):
        self.score += 4
        self.update_scoreboard()

