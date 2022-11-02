b = int(input('請輸入開始數值'))
c = int(input('請輸入結束數值'))
for a in range(b, c):
    x = "t"
    for i in range(2, a):
        if a % i == 0:
            x = 'f'
    if x == "t":
        print(a)
