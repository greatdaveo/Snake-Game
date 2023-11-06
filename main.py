import time
from snake import  Snake
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()






screen.exitonclick()
