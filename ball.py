from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.refresh()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bound_y(self):
        self.y_move *= -1

    def bound_x(self):
        self.speed("fastest")
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.x_move *= -1









