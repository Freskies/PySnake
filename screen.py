from turtle import Screen, Turtle
from snake import Snake


def draw_border():
    border = Turtle()
    border.speed("fastest")
    border.hideturtle()
    border.penup()
    border.goto(-280, -280)
    border.pendown()
    border.pensize(3)
    border.color("white")
    for _ in range(4):
        border.forward(560)
        border.left(90)


class SnakeScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(620, 620)
        self.screen.bgcolor("#006600")
        self.screen.title("PySnake")
        self.screen.tracer(0)
        self.can_snake_turn = True
        self.buffered_turn = None
        draw_border()

    def reset_turn(self):
        def enable_and_apply():
            self.can_snake_turn = True
            if self.buffered_turn:
                self.buffered_turn()
                self.buffered_turn = None
                self.reset_turn()

        self.can_snake_turn = False
        self.screen.ontimer(enable_and_apply, 100)

    def listen_snake(self, snake: Snake):
        def wrap_turn(turn):
            def handler():
                if self.can_snake_turn:
                    turn()
                    self.reset_turn()
                else:
                    self.buffered_turn = turn
            return handler

        self.screen.listen()
        self.screen.onkey(wrap_turn(snake.go_up), "Up")
        self.screen.onkey(wrap_turn(snake.go_down), "Down")
        self.screen.onkey(wrap_turn(snake.go_left), "Left")
        self.screen.onkey(wrap_turn(snake.go_right), "Right")

    def update(self):
        self.screen.update()

    def exitonclick(self):
        self.screen.exitonclick()

