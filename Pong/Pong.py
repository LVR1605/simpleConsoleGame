import turtle as t

player1score = 0
player2score = 0
ball_speed_increase = 0.001

window = t.Screen()
window.title("Pong Games")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Left paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("red")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("blue")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Score display
pen = t.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Devil: 0                           God: 0", align="center", font=("Arial", 24, "normal"))

# Draw the center line
center_line = t.Turtle()
center_line.speed(0)
center_line.color("white")
center_line.penup()
center_line.goto(0, 300)
center_line.setheading(270)
while center_line.ycor() > -300:
    center_line.pendown()
    center_line.forward(20)
    center_line.penup()
    center_line.forward(20)

# Functions to move paddles
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 20
        left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -250:
        y -= 20
        left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 20
        right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -250:
        y -= 20
        right_paddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx += ball_speed_increase  # Increase ball speed
        player1score += 1
        pen.clear()
        pen.write("Devil: {}                           God: {}".format(player1score, player2score), align="center",
                  font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx -= ball_speed_increase  # Increase ball speed
        player2score += 1
        pen.clear()
        pen.write("Devil: {}                           God: {}".format(player1score, player2score), align="center",
                  font=("Arial", 24, "normal"))

    # Paddle and ball collisions
    if (340 > ball.xcor() > 330) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        if ball.dx > 0:
            ball.dx += ball_speed_increase  # Increase ball speed if moving right
        else:
            ball.dx -= ball_speed_increase  # Decrease ball speed if moving left

    if (-340 < ball.xcor() < -330) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        if ball.dx > 0:
            ball.dx += ball_speed_increase  # Increase ball speed if moving right
        else:
            ball.dx -= ball_speed_increase  # Decrease ball speed if moving left
