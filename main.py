import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
screen.listen()
screen.onkey(fun=player.up,key="Up")
car_manager=CarManager()
scoreboard=Scoreboard()
game_is_on = True
a=1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.list__of_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
    if player.player_at_finish_line():
        scoreboard.level+=1
        scoreboard.update_level()
        player.refresh()
        car_manager.level_up()

screen.exitonclick()