"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
​
hint:可以使用%取餘數進行判斷
​
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
s = int(input('number'))
f = 0
g = 0
for i in range(0, s + 1, 3):
    print(i)
for i in range(0, s + 1, 7):
    print(i)