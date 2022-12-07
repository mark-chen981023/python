z = []
p = []
juices = ['新增餐點', '移除餐點', '提交菜單']
n = ['頻果汁', '柳橙汁', '葡萄汁']
while True:
    for index in range(len(juices)):
        print(f'{(index+1)}. {juices[index]}')
    # print("1. 蘋果汁")
    # print("2. 柳橙汁")
    # print("3. 葡萄汁")
    # print("4. 系統關閉")
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("請輸入數字編號")
    else:
        if ans > len(juices) or ans == 0:
            print("請輸入數字編號")
        elif ans == 3:
            for i in z:
                if not (i) in p:
                    p.append(i)
                    print(f"{i}有{z.count(i)}個")
            break
        elif ans == 1:
            for i in range(len(n)):
                print(f'{(i+1)}. {n[i]}')
            a = input('請輸入資料')
            print(f'{n[ans-1]}')
            z.append(n[int(a) - 1])
            print(z)
        else:
            r = input('請輸入你想刪掉的資料')
            while r in z:
                z.remove(r)
            print(z)