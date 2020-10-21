#Pong
#By @TWHO
#part 1 getting started

import turtle


win = turtle.Screen()
win.title("pong by @TWHO")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#score
score_a = 0
score_b = 0

#paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350,0)


#paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350,0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3.5
ball.dy = -3.5

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center",font=("Courier",24,"normal"))

#Function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


#keyboard binding
win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")


# main game loop
while True:
    win.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1



    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",font=("Courier",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",font=("Courier",24,"normal"))


    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_2.ycor()+ 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
       


    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_1.ycor()+ 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

