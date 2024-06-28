import math

from playarea import PlayArea
from player import Player
from scoremanager import ScoreManager
from car import Car, FastCar, SlowCar
import random

screen = PlayArea()
turtle = Player()
score_manager = ScoreManager()

turtle.move_to_bottom()
screen.bind_press_action("Up", turtle.move_forward)
screen.bind_release_action("Up", turtle.move_null)

slow_cars = []
medium_cars = []
fast_cars = []
cars = [slow_cars, medium_cars, fast_cars]


def initialize_level():
    for Array in cars:
        Array.clear()
    car_count = 10 + score_manager.score
    for _ in range(car_count):
        if len(slow_cars) < math.floor(car_count/3):
            new_car = SlowCar()
            slow_cars.append(new_car)
        elif len(medium_cars) < math.floor(car_count/3):
            new_car = Car()
            medium_cars.append(new_car)
        else:
            new_car = FastCar()
            fast_cars.append(new_car)


initialize_level()

run_game = True
while run_game:
    for carArray in cars:
        for car in carArray:
            car.forward(score_manager.score + 1 * car.speed)
            if car.check_collision(turtle):
                screen.window.bye()
    if turtle.pos()[1] > 300:
        score_manager.increment_score()
        initialize_level()
        turtle = Player()
        turtle.move_to_bottom()
        screen.bind_press_action("Up", turtle.move_forward)
        screen.bind_release_action("Up", turtle.move_null)
    turtle.apply_velocity()
