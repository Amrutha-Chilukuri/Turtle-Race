import turtle
import random
my_screen = turtle.Screen()
my_screen.setup(500, 400)
user_bet = my_screen.textinput("What's your bet?", "Which turtle among red, blue, yellow, green would win?").lower()


def defining(obj, color, y):
    obj.shape("turtle")
    obj.color(color)
    obj.penup()
    obj.setposition(-230, y)
    obj.speed("fastest")


red = turtle.Turtle()
defining(red, 'red', 150)
blue = turtle.Turtle()
defining(blue, 'blue', 50)
green = turtle.Turtle()
defining(green, 'green', -50)
yellow = turtle.Turtle()
defining(yellow, 'yellow', -150)
colors = ["red", "blue", 'green', "yellow"]
pen = turtle.Turtle()
pen.ht()


def start(obj1, obj2, obj3, obj4, point):
    while obj1.xcor() <= point and obj2.xcor() <= point and obj3.xcor() <= point and obj4.xcor() <= point:
        obj1.fd(random.randint(0, 20))
        obj2.fd(random.randint(0, 20))
        obj3.fd(random.randint(0, 20))
        obj4.fd(random.randint(0, 20))
    turtles = [obj1.xcor(), obj2.xcor(), obj3.xcor(), obj4.xcor()]
    winner_index = turtles.index(max(turtles))
    if colors[winner_index] == user_bet:
        pen.write('You Won!', font=("arial", 25, "normal"))
    else:
        pen.write('You Lost.', font=("arial", 25, "normal"))


line = turtle.Turtle()
line.ht()
line.penup()
line.setposition(220, 150)
line.pensize(5)
line.pendown()
line.sety(-150)
start(red, blue, green, yellow, 220)

my_screen.exitonclick()