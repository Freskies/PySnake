from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("PySnake")
screen.tracer(0)

snake = Snake()
screen.update()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")


while True:
    snake.move()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()