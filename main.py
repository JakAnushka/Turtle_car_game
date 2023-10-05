import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager=CarManager()
player=Player()

scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car()
    car_manager.move_car()
    if player.ycor()>280:
        player.move_from_start()
        scoreboard.level_up()
        car_manager.speed_car()
    for cars in car_manager.all_cars:
        if player.distance(cars)<25:
            scoreboard.game_over()
            game_is_on=False

screen.exitonclick()
