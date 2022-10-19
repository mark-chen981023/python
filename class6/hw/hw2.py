"""
請使用turtle模組、for、time模組來印出時鐘的秒針
基本功能參考影片t1_turtle_time.mp4
提示：
turtle.clear() # 清空畫面指令
​
import time  # 匯入time模組
time.sleep(1) # 延遲1秒
"""
import time
import turtle as t

t.speed(0)
for i in range(0, 360, 6):
    t.right(i)
    t.forward(100)
    t.stamp()
    t.home()
    time.sleep(1)
    t.clear()
t.done()