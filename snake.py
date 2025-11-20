import math

from segment import Segment, SEGMENT_SIDE, HeadSegment


class Snake:
    def __init__(self):
        self.head_direction = 0
        self.segment_list: list[Segment] = [HeadSegment(0, 0, 0)]
        self.head = self.segment_list[0]
        self.add_segment()
        self.add_segment()

    def add_segment(self):
        tail = self.segment_list[-1]
        x = -math.cos(math.radians(tail.direction)) * SEGMENT_SIDE + tail.x
        y = -math.sin(math.radians(tail.direction)) * SEGMENT_SIDE + tail.y
        self.segment_list.append(Segment(x, y, tail.direction))

    def move(self):
        current_moving = self.head_direction
        for segment in self.segment_list:
            segment.move(current_moving)
            current_moving, segment.direction = segment.direction, current_moving

    def go_up(self):
        if self.head_direction != 270:
            self.head_direction = 90

    def go_down(self):
        if self.head_direction != 90:
            self.head_direction = 270

    def go_left(self):
        if self.head_direction != 0:
            self.head_direction = 180

    def go_right(self):
        if self.head_direction != 180:
            self.head_direction = 0

    def is_game_over(self):
        if (not -280 < self.head.x < 280) or (not -280 < self.head.y < 280):
            return True
        if len(self.segment_list) < 4:
            return False
        for segment in self.segment_list[4:]:
            if self.head.distance(segment) < 15:
                return True
        return False

    def reset(self):
        for segment in self.segment_list:
            segment.hideturtle()
        self.segment_list.clear()
        self.__init__()