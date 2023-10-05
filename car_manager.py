import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.speed_of_car=STARTING_MOVE_DISTANCE


    def car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            random_colors = random.choices(COLORS)
            new_car.color(random_colors)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-200, 200)
            x_pos =300
            new_car.goto(x=x_pos,y=y_pos)
            self.all_cars.append(new_car)


    def move_car(self):
        for i in self.all_cars:
            i.setheading(180)
            i.forward(self.speed_of_car)

    def speed_car(self):
        self.speed_of_car=+MOVE_INCREMENT




