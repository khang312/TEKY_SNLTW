import turtle

# Set up the screen
window = turtle.Screen()
window.title("Pong Game")
window.bgpic("/Users/mac/Desktop/TEKY_SNLTW/Day2/1.gif")
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0",
          align="center",
          font=("Courier", 24, "normal"))
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball_dx = 0.15
ball_dy = -0.15


# Paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)


# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx = -0.15
        ball_dy = 0.15
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "normal"))
        if score_a == 100:
            turtle.done()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx = 0.15
        ball_dy = 0.15
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "normal"))
        if score_b == 100:
            turtle.done()

    # Paddle and ball collision
    if (ball_dx > 0) and (350 > ball.xcor() > 340) and (
            paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball_dx *= -1.3
        ball_dy *= 1.3

    if (ball_dx < 0) and (-350 < ball.xcor() < -340) and (
            paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball_dx *= -1.3
        ball_dy *= 1.3