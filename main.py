from turtle import Screen
from create_turtle import CreateTurtle
from create_car import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = CreateTurtle()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 26:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() > 275:
        turtle.reset()
        car_manager.increase_speed()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()


screen.exitonclick()
