from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")

turtle = Turtle()
turtle.shape("square")
turtle.shapesize(stretch_wid=100, stretch_len=0.25)
turtle.color("white")
screen.tracer(0)

paddle_r = Paddle((390, 0))
paddle_l = Paddle((-390, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 390 or ball.ycor() < -390:
        ball.bounce()

    if ball.xcor() > 370 and ball.distance(paddle_r) < 50:
        ball.bounce_x()

    if ball.xcor() < -370 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()