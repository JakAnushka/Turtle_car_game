from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.update_level()


    def update_level(self):
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level+=1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center",font=FONT)
