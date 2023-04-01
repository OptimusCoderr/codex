# Simple pong in Python

#Part 1: Getting Started

import turtle
import winsound

wn= turtle.Screen()
wn.title('PONG') #title name
wn.bgcolor("blue") #background_colour
wn.setup(width=900, height=600) # pixles
wn.tracer(0) # for the game to run smoother

#SCORE
score_a=0
score_b=0

#PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)# speed of animation (max)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=7, stretch_len=1)# wid is the same as height
paddle_a.penup()
paddle_a.goto(-400,0)# starting position of the turtle



#PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)# speed of animation (max)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)# wid is the same as height
paddle_b.penup()
paddle_b.goto(400,0)# starting position of the turtle




#BALL
ball = turtle.Turtle()
ball.speed(0)# speed of animation (max)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)# starting position of the turtle

ball.dx= 0.05 # ball movement by 2 pixles
ball.dy= 0.05

#SCOR BOARD #PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",20,"normal"))


#FUNCTION
def paddle_a_up() : #define a function
    y=paddle_a.ycor() #recalling previous y cordinate
    y+=20
    paddle_a.sety(y)

def paddle_a_down() : #define a function
    y=paddle_a.ycor() #recalling previous y cordinate
    y-=20
    paddle_a.sety(y)

def paddle_b_up() : #define a function
    y=paddle_b.ycor() #recalling previous y cordinate
    y+=20
    paddle_b.sety(y)

def paddle_b_down() : #define a function
    y=paddle_b.ycor() #recalling previous y cordinate
    y-=20
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290) #it means set it back to 290
        ball.dy *= -1 #this reverses the direction
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) #FOR PLAYING A SOUND

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 440:
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        score_a +=1
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",20,"normal"))

    if ball.xcor() < -440:
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        score_b += 1
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

# PADDLE AND BALL COLLISIONS
    if (ball.xcor() > 380 and ball.xcor()<390) and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor()>paddle_b.ycor() - 40):
        ball.setx(380)
        ball.dx*=-1

    if (ball.xcor() < -380 and ball.xcor()>-390) and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor()>paddle_a.ycor() - 40):
        ball.setx(-380)
        ball.dx*=-1



