from turtle import Turtle
MOVE = False
ALIGN = "left"
FONT = ('courier', 80, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.refresh_score_board()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score_board()

    def refresh_score_board(self):
        self.write(f"{self.score}", move=MOVE, align=ALIGN, font=FONT)
