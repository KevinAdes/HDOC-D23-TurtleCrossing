from turtle import Turtle


class Player(Turtle):
    velocity = 0
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()

    def move_to_bottom(self):
        self.teleport(0, -280)

    def move_forward(self):
        self.velocity = 10

    def move_null(self):
        self.velocity = 0

    def apply_velocity(self):
        current_pos = self.pos()
        self.goto(current_pos[0], current_pos[1] + self.velocity)
