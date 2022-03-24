from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screenwidth, screenheight):
        super().__init__()
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        rand_x = random.randint(-(self.screenwidth // 2) + 20, (self.screenwidth // 2) - 20)
        rand_y = random.randint(-(self.screenheight // 2) + 20, (self.screenheight // 2) - 20)
        self.goto(rand_x, rand_y)

    def reappear(self):
        rand_x = random.randint(-(self.screenwidth // 2) + 20, (self.screenwidth // 2) - 20)
        rand_y = random.randint(-(self.screenheight // 2) + 20, (self.screenheight // 2) - 20)
        self.goto(rand_x, rand_y)

