from turtle import Screen, Turtle
from snake import Snake

BG_COLOR = "#006600"

# message turtle
message_turtle = Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.color("white")


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

def draw_start_message(is_game_over=False):
    message_turtle.goto(0, 20)
    message_turtle.write("Press SPACE to Start", align="center", font=("Courier", 24, "normal"))
    if is_game_over:
        message_turtle.goto(0, 60)
        message_turtle.write("GAME OVER!", align="center", font=("Courier", 30, "normal"))


class SnakeScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(620, 620)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title("PySnake")
        self.screen.tracer(0)
        self.screen.listen()
        self.can_snake_turn = True
        self.buffered_turn = None
        self.waiting_for_start = False
        self.game_on = False
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

        self.screen.onkey(wrap_turn(snake.go_up), "Up")
        self.screen.onkey(wrap_turn(snake.go_down), "Down")
        self.screen.onkey(wrap_turn(snake.go_left), "Left")
        self.screen.onkey(wrap_turn(snake.go_right), "Right")

    def update(self):
        self.screen.update()

    def exitonclick(self):
        self.screen.exitonclick()

    def wait_for_start(self):
        self.waiting_for_start = True
        draw_start_message()
        self.screen.update()

        def start_game():
            message_turtle.clear()
            self.screen.update()
            self.waiting_for_start = False
            self.game_on = True

        self.screen.onkey(start_game, "space")

    def reset_game(self):
        self.game_on = False
        self.waiting_for_start = False
        draw_start_message(is_game_over=True)
        self.screen.update()
