from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)
game_on = True

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
score = Scoreboard()

screen.listen()

screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    #Detect ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect a miss
    if ball.xcor() > 365: 
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -365:
        ball.reset_pos()
        score.r_point()




screen.exitonclick()