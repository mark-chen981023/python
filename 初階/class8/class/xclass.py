#  num = input('輸入2以上得整數')
#  i = 2
#  x = 0
#  while x != 0 and i != num:
#      x = num % i
#      i + 1
# if i == num:
#     print('是質數')
# else:
#     print('不是質數')
x = int(input('輸入2以上得整數'))
i = 2
while x % i != x and i != x:
    i += 1
if i == x:
    print("yes")
else:
    print("no")