from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("coral")
        self.speed("fastest")
        self.goto_random()

    def goto_random(self):
        x = random.randint(0, 14) * 20 - 280
        y = random.randint(0, 14) * 20 - 280
        self.goto(x, y)