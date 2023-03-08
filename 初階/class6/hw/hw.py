"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""
import turtle as t

t.penup()
t.speed(0)

for i in range(0, 360, 45):
    t.right(i)
    t.forward(100)
    t.stamp()
    t.home()
t.done()