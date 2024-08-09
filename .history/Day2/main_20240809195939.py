import turtle
class Bong:
    ball = turtle.Turtle()
    dx = 0.15
    dy = -0.15

    def __init__(self, shape, color):
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.goto(0, 0)
    def move_ball(self):

        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)
    def ball_collision(self):
        if self.ball.ycor() > 290:
            self.ball.sety(290)
        self.dy *= -1

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.dy *= -1

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.dx = -0.15
            self.dy = 0.15
            # score_a += 1
            # pen.clear()
            # pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
            #         align="center",
            #         font=("Courier", 24, "normal"))
            # if score_a == 100:
            #     turtle.done()
        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.dx = 0.15
            self.dy = 0.15
            # score_b += 1
            # pen.clear()
            # pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
            #         align="center",
            #         font=("Courier", 24, "normal"))
            # if score_b == 100:
            #     turtle.done()

    

class Paddle:
   
    def __init__(self, color, x, y):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color(color)
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.goto(x, y)
        self.score = 0

        # Paddle movement
        def paddle_up(self):
            y = self.paddle.ycor()
            if y < 250:
                y += 20
            self.paddle.sety(y)


        def paddle_down(self):
            y = self.paddle.ycor()
            if y > -240:
                y -= 20
            self.paddle.sety(y)

    
    pass
# Set up the screen
window = turtle.Screen()
window.title("Pong Game")
window.bgpic("/Users/mac/Desktop/TEKY_SNLTW/Day2/1.gif")
window.setup(width=800, height=600)
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0",
          align="center",
          font=("Courier", 24, "normal"))

paddleA = Paddle()






# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    window.update()


    # Border checking
    
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