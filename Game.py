# Starten
import turtle as t

wn = t.Screen()
wn.title("First Try")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
sc_a = 0
sc_b = 0
# Paddle 1
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("grey")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360,0)

# Paddle 2
paddle_b = t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("grey")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(360,0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Grey")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = t.Turtle()
pen.speed(0)
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Spieler_A: {} Spieler_B: {}".format(sc_a, sc_b), align="center", font=("Arial", 20, "normal"))


#Funktionen
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)


#Tastatur_Bedienung
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
#main loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        sc_a+=1
        pen.clear()
        pen.write("Spieler_A: {} Spieler_B: {}".format(sc_a, sc_b), align="center", font=("Arial", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        sc_b += 1
        pen.clear()
        pen.write("Spieler_A: {} Spieler_B: {}".format(sc_a, sc_b), align="center", font=("Arial", 20, "normal"))

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
# Paddle und Ball
    if (ball.xcor() > 350 and ball.xcor() < 370 ) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(350)
        ball.dx *= -1

    if (ball.xcor() < -350 and ball.xcor() > -370 ) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-350)
        ball.dx *= -1
