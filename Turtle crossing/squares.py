from turtle import Turtle
from random import randint
import random
colors=["black","yellow","blue","red","green"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10





class Square:
    def __init__(self):
        self.all_squares=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car (self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            new_car=Turtle("square")
            new_car.color(random.choice(colors))
            new_car.shapesize(1,2)
            new_car.penup()
            y = random.randint(-250, 250)
            new_car.goto(300,y)
            self.all_squares.append(new_car)

    def move_cars(self):
        for car in self.all_squares:
            car.backward(self.car_speed)

    def speed_increase (self):
        self.car_speed+=1








