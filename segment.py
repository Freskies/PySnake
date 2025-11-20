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
        self.color("#00cc00")
        self.goto(x, y)

    def move(self, direction):
        self.x += math.cos(math.radians(direction)) * SEGMENT_SIDE
        self.y += math.sin(math.radians(direction)) * SEGMENT_SIDE
        self.goto(self.x, self.y)


class HeadSegment(Segment):

    def __init__(self, x: float, y: float, direction: int):
        super().__init__(x, y, direction)
        self.eyes = (Turtle(), Turtle())
        for eye in self.eyes:
            eye.hideturtle()
            eye.penup()
            eye.shape("circle")
            eye.color("black")
            eye.shapesize(0.2, 0.2)
            eye.showturtle()
        self.move(direction)


    def move(self, direction):
        super().move(direction)
        facing = math.radians(direction)
        eye_offset_x = math.cos(facing) * 5
        eye_offset_y = math.sin(facing) * 5
        angle_perpendicular_line = facing + math.pi / 2
        eye_separation = 6
        eyes_pos = (
            (
                self.x + eye_offset_x + math.cos(angle_perpendicular_line) * (eye_separation / 2), # left eye X
                self.y + eye_offset_y + math.sin(angle_perpendicular_line) * (eye_separation / 2) # left eye Y
            ),
            (
                self.x + eye_offset_x - math.cos(angle_perpendicular_line) * (eye_separation / 2), # right eye X
                self.y + eye_offset_y - math.sin(angle_perpendicular_line) * (eye_separation / 2) # right eye Y
            )
        )
        for eye, pos in zip(self.eyes, eyes_pos):
            eye.goto(pos)

    def hideturtle(self):
        super().hideturtle()
        for eye in self.eyes:
            eye.hideturtle()