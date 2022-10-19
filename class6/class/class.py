import turtle as t

from pygame import BLEND_MULT

# t.forward(100)
# for i in range(3):
#     t.right(90)
#     t.forward(100)
# t.done()

# t.shape('turtle')
# t.color('blue')
# t.forward(50)
# t.penup()
# t.stamp()
# t.done()
t.shape('circle')
t.penup()
t.color('blue')
for i in range(0, 100, 2):
    t.forward(i)
    t.right(25)
    t.stamp()
t.done()