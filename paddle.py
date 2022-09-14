from turtle import Turtle, Screen
PADDLE_STARTING_POINT  = (350, 0)


class Paddle(Turtle):
    def __init__(self, start_position):
        self.starting_position = start_position
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(self.starting_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
