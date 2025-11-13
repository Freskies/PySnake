import math
from turtle import Turtle

SEGMENT_SIDE = 20

class Segment(Turtle):

    def __init__(self, x: float, y: float, direction: int):
        super().__init__()
        self.direction = direction
        self.x = x
        self.y = y
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(x, y)

    def move(self, direction):
        self.x += math.cos(math.radians(direction)) * SEGMENT_SIDE
        self.y += math.sin(math.radians(direction)) * SEGMENT_SIDE
        self.goto(self.x, self.y)