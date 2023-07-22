from turtle import Turtle

ALIGNMENT='center'
FONT='Courier'
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.LeftScore = 0
        self.RightScore = 0
        self.color('#fff')
        self.goto(0,270)
        self.write(f"Left:{self.LeftScore}| Right:{self.RightScore}",align=ALIGNMENT,font=(FONT,17,'normal'))
    
    def UpdateScore(self):
        self.clear()
        self.write(f"Left:{self.LeftScore}| Right:{self.RightScore}",align=ALIGNMENT,font=(FONT,17,'normal'))

    
    def RectifyScore(self,winnerSide):
        if(winnerSide=='left'):
            self.LeftScore +=1
        elif(winnerSide=='right'):
            self.RightScore +=1