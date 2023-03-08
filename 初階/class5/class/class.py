# == 相等 1 == 1 True
# != 不相等 1 != 0 True
# >= 大於等於 1 >= 2 False
# <= 小於等於 1 <= 2 True
# > 大於 1 > 2 False
# < 小於 1 < 2 True
# not邏輯
# •and邏輯
# •or邏輯
# •實驗看看：與比較運算子結合
# 使用時哪一部分會優先執行呢?
# not範例 結果(布林)
# not True False
# not False True
# and範例 結果(布林)
# False and False False
# False and True False
# True and False False
# True and True True
# or範例 結果(布林)
# False or False False
# False or True True
# True or False True
# 運算子優先順序
# 優先順序 運算子
# 1 ()括號
# 2 **次方
# 3 +(正數)、-(負數)
# 4 *(乘法)、/(除法)、%(餘數)、//(取商)
# 5 +(加法)、-(減法)
# 6 ==、!=、>、<、>=、<=
# 7 not、and、or
password = input("請輸入密碼")
if password == "1234":
    print("歡迎光臨")
elif password == "9876":
    print("Hello!")
else:
    print("哈囉!你是小偷嗎?")
# score = float(input("Please input score: "))
# if score >= 90:
# grade = "A"
# if score >= 80 and score < 90:
# grade = "B"
# if score >= 70 and score < 80:
# grade = "C"
# if score >= 60 and score < 70:
# grade = "D"
# else:
# grade = "E"
# print("Your grade is:" + grade)