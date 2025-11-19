from food import Food
from scoreboard import Scoreboard
from screen import SnakeScreen
from snake import Snake
import time

screen = SnakeScreen()
scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen_snake(snake)
screen.update()

while True:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.goto_random()
        snake.add_segment()
        scoreboard.increase_score()

screen.exitonclick()