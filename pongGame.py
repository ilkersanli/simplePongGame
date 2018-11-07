# Simple Pong game
# https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
# Pong in Python 3 for Beginners by Christian Thompson
"""
1- Empty screen object added. Dimensions and background's been set. Main game loop started.
2- Paddles and ball objects added. Location and color's been set.
3- Function that moves the paddles added. Keyboard listening added.
4- Function that moves the ball added. Border checking added.
5- Collision checking added.
6- Default PEN added. Scores are start counting and PEN updated along.
7- WINSOUND imported. Bounce.wav set in the same dir as py file. winsound.PlaySound added in 4 collisions.
"""
# TODO Make game with accelerating ball and extra creative functions.
# TODO Make game with changing paddle sides depending on creative conditions..
# TODO Make a single player alternative.
# TODO Make a single player alternative towards wall.

import turtle
import winsound

# ----- 1 ----- #
wn = turtle.Screen()
wn.title("Pong by ilker")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
# ----- 6 ----- #
score_a = 0
score_b = 0

# Paddle A
# ----- 2 ----- #
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
# ----- 2 ----- #
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
# ----- 2 ----- #
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# ----- 4 ----- #
ball.dx = 0.25
ball.dy = 0.25

# Pen
# ----- 6 ----- #
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
# ----- 3 ----- #
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# ----- 3 ----- #
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# ----- 3 ----- #
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


# ----- 3 ----- #
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
# ----- 3 ----- #
wn.listen()
wn.onkeypress(paddle_a_up, "w")  # not paddle_a_up()
wn.onkeypress(paddle_a_down, "s")  # not paddle_a_down()
wn.onkeypress(paddle_b_up, "Up")  # not paddle_b_up()
wn.onkeypress(paddle_b_down, "Down")  # not paddle_b_down()

# Main Game loop
# ----- 1 ----- #
while True:
    wn.update()

    # Move the ball
    # ----- 4 ----- #
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # ----- 4 ----- #
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # ----- 7 ----- #
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    # ----- 4 ----- #
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # ----- 7 ----- #
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    # ----- 4 ----- #
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    # ----- 6 ----- #
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # ----- 4 ----- #
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    # ----- 6 ----- #
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # ----- 5 ----- #
    if 350 > ball.xcor() > 340 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    # ----- 7 ----- #
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    # ----- 5 ----- #
    if -350 < ball.xcor() < -340 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    # ----- 7 ----- #
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
