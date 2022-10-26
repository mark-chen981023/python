from re import S
import turtle as t

# t.tracer(0, 0)
# t.pensize(10)
# t.fillcolor('blue')
# t.begin_fill()
# for i in range(5):
#     t.forward(100)
#     t.right(144)
# t.end_fill()
# t.done()
number = input('請輸入整數')
print('整數是' + number)
s = 0
for i in range(0, int(number) + 1):
    s = s + i
print(s)