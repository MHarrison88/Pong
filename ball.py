from turtle import Turtle

class Ball(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.goto(x=pos[0], y=pos[1])
        self.seth(45)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        """
        Moves ball around screen
        """
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x, y)

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= .9

    def bounce_y(self):
        self.move_y *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1