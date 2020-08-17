import turtle
from functools import partial


def initPlayer(posX, posY):
    player = turtle.Turtle()
    player.speed(0)
    player.shape("square")
    player.color("white")
    player.penup()
    player.goto(posX, posY)
    player.shapesize(stretch_wid=5, stretch_len=1)
    return player


def initBall():
    ball = turtle.Turtle()
    ball.speed(-1)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = -1
    ball.dy = -1
    return ball


def initScore(player, points):
    score = turtle.Turtle()
    score.color("green")
    score.penup()
    score.goto(player.xcor(), 270)
    score.write(str(points), font=("Arial", 20, "normal"))
    return score


def playerDown(player):
    player.sety(player.ycor() - 30)


def playerUp(player):
    player.sety(player.ycor() + 30)

def updateScore(score, scoreToPrint):
    score._clear()
    score.write(str(scoreToPrint), font=("Arial", 20, "normal"))

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

playerA = initPlayer(-350, 0)
playerB = initPlayer(350, 0)
ball01 = initBall()
scorePlayerA = initScore(playerA, 0)
scorePlayerB = initScore(playerB, 0)
scoreStored = {"playerA" : 0, 
                "playerB" : 0}

wn.listen()
wn.onkeypress(partial(playerUp, playerA), "a")
wn.onkeypress(partial(playerDown, playerA), "d")
wn.onkeypress(partial(playerUp, playerB), "k")
wn.onkeypress(partial(playerDown, playerB), "l")

while True:
    wn.update()
    ball01.setx(ball01.xcor() + ball01.dx)
    ball01.sety(ball01.ycor() + ball01.dy)

    if ball01.ycor() > 290 or ball01.ycor() < -290:
        ball01.dy *= -1

    if ball01.xcor() > 390:
        ball01.goto(0, 0)
        ball01.dx *= -1
        scoreStored['playerB'] = scoreStored.get("playerB") + 1
        print(scoreStored)
        print(scoreStored.get("playerB"))
        updateScore(scorePlayerA, scoreStored.get("playerB"))

    if ball01.xcor() < -390:
        ball01.goto(0, 0)
        ball01.dx *= -1
        scoreStored['playerA'] = scoreStored.get("playerA") + 1
        print(scoreStored.get("playerA"))
        updateScore(scorePlayerB, scoreStored.get("playerA"))
