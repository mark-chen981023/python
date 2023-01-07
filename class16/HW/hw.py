x = int(input('輸入'))
y = int(input('輸入'))
import turtle as t


def tree(x, y):
    t.penup()
    t.pencolor("green")
    t.goto(x, y)
    t.pendown()
    t.left(90)
    t.pensize(100)
    t.forward(50)
    t.left(90)
    t.pensize(100)
    t.forward(50)
    t.right(135)
    t.pensize(100)
    t.forward(70)
    t.right(90)
    t.pensize(100)
    t.forward(70)


tree(x, y)
t.done()