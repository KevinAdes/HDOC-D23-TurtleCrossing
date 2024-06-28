from turtle import Turtle, clearscreen


class ScoreDisplay(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setposition(-380, -280)
        self.update_score(0)

    def update_score(self, new_score):
        self.clear()
        self.write(new_score, False, "left", ("arial", 20, "normal"))


class ScoreManager:
    score = 0
    display = ScoreDisplay()

    def increment_score(self):
        self.score += 1
        clearscreen()
        self.display.update_score(self.score)
