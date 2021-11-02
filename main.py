from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

screen.onkey(fun=r_paddle.move_up, key='Up')
screen.onkey(fun=r_paddle.move_down, key='Down')
screen.onkey(fun=l_paddle.move_up, key='e')
screen.onkey(fun=l_paddle.move_down, key='s')

is_on = True
while is_on:
    screen.update()
    screen.tracer(0)
    time.sleep(random.uniform(0.0001, 0.1))

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bound_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bound_x()

    # detect l paddle missed
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()
    # detect r paddle missed
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

screen.exitonclick()
