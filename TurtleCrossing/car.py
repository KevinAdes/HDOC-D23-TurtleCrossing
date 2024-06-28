from turtle import Turtle
import random


class Car(Turtle):
    height = 1
    width = 2
    speed = 5

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(self.height, self.width)
        self.color("yellow")
        direction = random.randint(0, 1)
        if direction == 0:
            self.spawn_left()
        else:
            self.spawn_right()

    def spawn_left(self):
        vertical_spawn_lane = random.randint(0, 29)
        vertical_spawn_point = (vertical_spawn_lane * 20) - 290
        self.teleport(-350, vertical_spawn_point)
        self.setheading(0)

    def spawn_right(self):
        vertical_spawn_lane = random.randint(0, 29)
        vertical_spawn_point = (vertical_spawn_lane * 20) - 290
        self.teleport(350, vertical_spawn_point)
        self.setheading(180)

    def check_collision(self, turtle):
        if abs(self.pos()[0] - turtle.pos()[0]) < 30 and abs(self.pos()[1] - turtle.pos()[1]) < 20:
            return True
        else:
            if self.pos()[0] < -400:
                self.spawn_right()
            elif self.pos()[0] > 400:
                self.spawn_left()

class SlowCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 3
        self.color("green")


class FastCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 7
        self.color("red")