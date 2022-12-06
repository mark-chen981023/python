# x = []
# num = int(input('請輸入清單長度'))

# for i in range(num):
#     d = input('請輸入資料')
#     x.append(d)
#     print(x)

# # c = input("請輸入請輸入想計算的資料")
# # print(f"{c}有{x.count(c)}個")
# for i in x:
#     print(f"{i}有{x.count(i)}個")
x = []
z = []
num = int(input('請輸入清單長度'))

for i in range(num):
    d = input('請輸入資料')
    x.append(d)
    print(x)

for i in x:
    if not (i) in z:
        z.append(i)
        print(f"{i}有{x.count(i)}個")
