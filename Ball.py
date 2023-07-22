from turtle import Turtle
import time
from Score import Score
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.goto(0,0)
        self.penup()
        self.speed(10)
        self.SPEED_X = 10
        self.SPEED_Y = 10
        
    def move(self):
        self.goto(self.xcor()+self.SPEED_X,self.ycor()+self.SPEED_Y)
        time.sleep(0.1)
    
    def CollisionOnTopWall(self):
        self.SPEED_Y = self.SPEED_Y * (-1)
    
    def CollisionOnBottomWall(self):
        self.SPEED_Y = self.SPEED_Y * (-1)
    
    def Rebound(self):
            self.SPEED_X*=-1

    def checkWinner(self):
         if(self.xcor()>0):
            return 'left'
         else:
            return 'right'


    def Restart(self):
         self.goto(0,0)
         self.SPEED_X*=-1