from turtle import Turtle

#Using inheritance
class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.pu()
        self.shape("square")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.color("white")
        self.goto(x=pos[0], y=pos[1])

    def up(self):
        """
        Move paddle up
        """
        y = self.ycor() + 20
        self.sety(y)

    def down(self):
        """
        Move paddle down
        """
        y = self.ycor() - 20
        self.sety(y)


# Not using inheritance
# class Paddle:

#     def __init__(self, pos):
#         self.start(pos)
#         self.paddle.speed("fastest")
        

#     def start(self, pos):
#         self.paddle = Turtle()
#         self.paddle.pu()
#         self.paddle.shape("square")
#         self.paddle.shapesize(stretch_wid=5.0, stretch_len=1.0)
#         self.paddle.color("white")
#         self.paddle.speed("fastest")
#         self.paddle.goto(x=pos[0], y=pos[1])

#     def up(self):
#         """
#         Move paddle up
#         """
#         y = self.paddle.ycor() + 20
#         self.paddle.sety(y)

#     def down(self):
#         """
#         Move paddle down
#         """
#         y = self.paddle.ycor() - 20
#         self.paddle.sety(y)
