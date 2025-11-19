from turtle import Screen
from snake import Snake

class SnakeScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.title("PySnake")
        self.screen.tracer(0)
        self.can_snake_turn = True
        self.buffered_turn = None

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