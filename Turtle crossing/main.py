from turtle import Turtle,Screen
from squares import Square
from car import Car
from scoreboard import Scoreboard
import time




screen=Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
car=Car()
square = Square()
scoreboard=Scoreboard()






screen.listen()
screen.onkey(car.go_up, "Up")
screen.onkey(car.go_down, "Down")

game_on=True

while game_on:
    scoreboard.update_scoreboard()
    time.sleep(0.1)
    screen.update()
    square.create_car()
    square.move_cars()
    if car.ycor() > 280:
        car.goto(0, -270)
        scoreboard.increase_score()
        square.speed_increase()
    for cars in square.all_squares:
        if cars.distance(car)<20:
            scoreboard.game_over()
            game_on=False
        



















screen.exitonclick()