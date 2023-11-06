from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=520, height=520)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# To set the control key
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # To Detect the collision of the snake and food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake_size()
        scoreboard.increase_score()

   # To detect collision with the wall
    if snake.snake_head.xcor() > 250 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 250 or snake.snake_head.ycor() < -240:
        game_is_on = False
        scoreboard.gave_over()

    # To detect the collision with the tail (If the head collides wth any segment in the tail)
    for segment in snake.segments:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gave_over()


screen.exitonclick()
