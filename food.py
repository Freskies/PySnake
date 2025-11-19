from turtle import Turtle
import random

from snake import Snake


class Food(Turtle):
    def __init__(self, snake: Snake):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("coral")
        self.speed("fastest")
        self.goto_random(snake)

    def goto_random(self, snake: Snake):
        x = random.randint(0, 26) * 20 - 260
        y = random.randint(0, 26) * 20 - 260
        self.goto(x, y)
        for segment in snake.segment_list:
            if self.distance(segment) < 15:
                self.goto_random(snake)
                break
