from turtle import Turtle,Screen
from Paddle import Paddle
from Ball import Ball
from Score import Score
s  = Screen()
s.setup(width=800,height=600)
s.bgcolor('#000')
s.title("Pong 2D")
s.tracer(0)

PaddleRight = Paddle(350,0)
PaddleLeft = Paddle(-350,0)
ball = Ball()
s.update()
s.listen()

scoreboard = Score()

s.onkey(PaddleRight.move_up,"Up")
s.onkey(PaddleRight.move_down,"Down")
s.onkey(PaddleLeft.move_up,"w")
s.onkey(PaddleLeft.move_down,"s")

game_is_on = True
while game_is_on:
    s.update()
    ball.move()

    print(ball.distance(PaddleRight))
    if(ball.ycor()>=260):
        ball.CollisionOnTopWall()

    elif(ball.ycor()<=-280 ):
        ball.CollisionOnBottomWall()

    elif(ball.distance(PaddleRight) < 50.99 and ball.xcor() > 320):
        print('Collide')
        ball.Rebound()

    elif(ball.distance(PaddleLeft) < 50.99 and ball.xcor() < -320):
        print('Collide')
        ball.Rebound()
    elif(ball.xcor()>390 or ball.xcor() <-390):
        scoreboard.RectifyScore(ball.checkWinner())
        scoreboard.UpdateScore()
        ball.Restart()
s.exitonclick()