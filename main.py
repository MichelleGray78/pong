from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")
screen.onkey(paddle_two.up, "w")
screen.onkey(paddle_two.down, "s")

game_is_on = True   

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
    # Detect wall collision and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect paddle collision and bounce
    if ball.distance(paddle_one) < 50 and ball.xcor() > 320 or ball.distance(paddle_two) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
        
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()