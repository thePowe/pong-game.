from turtle import Turtle, Screen

from game_speed import Speed
from paddle import Paddle
from ball import Ball
import time

from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

r_score = ScoreBoard((50 * 2, 200))
l_score = ScoreBoard((-50 * 2, 200))

# screen.update()
ball = Ball()
game_speed = Speed()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "x")


def pong():
    game_is_on = True
    while game_is_on:
        # ball.goto(350, 100)
        time.sleep(game_speed.speed)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < - 280:
            ball.bounce_y()
            # game_speed.increase_game_speed()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            game_speed.increase_game_speed()

        #  Check left paddle misses the ball
        if ball.xcor() > 380:
            ball.reset_position()
            l_score.increase_score()
            game_speed.restart_speed()

        #  Check left paddle misses the ball
        if ball.xcor() < - 380:
            ball.reset_position()
            r_score.increase_score()
            game_speed.restart_speed()






if __name__ == "__main__":
    pong()

screen.exitonclick()
