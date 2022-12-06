x = []
num = int(input('請輸入清單長度'))

for i in range(num):
    d = input('請輸入資料')
    x.append(d)
    print(x)

r = input('請輸入你想刪掉的資料')
while r in x:
    x.remove(r)
print(x)
c = input("請輸入請輸入想計算的資料")
print(f"{c}有{x.count(c)}個")