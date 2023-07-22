from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,xcoord,ycoord):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(xcoord,ycoord)
        self.left(90)
        self.speed(0)

    def move_up(self):
        self.forward(20)
    
    def move_down(self):
        self.backward(20)