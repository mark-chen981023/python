b = {}
v = 0
while True:
    for key, value in b.items():
        print(key + ':' + value)
    print('1.新增科目與成績')
    print('2.刪除科目成績')
    print('3.關閉系統')
    ans = input("請輸入編號:")

    if ans == "3":
        for key, value in b.items():
            v = v + int(value)
        print(v / len(b))
        break
    elif ans == '1':
        key = input('請輸入科目名稱:')
        value = input('請輸入資料:')
        b[key] = value
    elif ans == '2':
        r = input('請輸入想刪除的key')
        b.pop(r, '')
    else:
        print("請輸入數字編號")