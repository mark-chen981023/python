# import os
# if os.path.isfile("C:\\Users\\markc\\Desktop\\python\\class18\\cls.py"):
#     print("檔案存在")
# else:
#     print("檔案不存在")
# #1. 要開啟的檔名
# fileName = "test.txt"
# #2. 指定w/ r /a mode
# Mode = "a"
# #3. 開啟檔案
# myFile = open(fileName, Mode)
# #4. 寫入檔案 \n 換行符號
# myFile.write("Hi\n")
# myFile.write("How old are you?")
# #5. 關閉檔案
# myFile.close()
# 1. 要開啟的檔名

path = "test.txt"
#2. 指定w/ r /a mode
f = open(path, 'r')
#3. 讀取檔案並顯示
total = f.read()  # 一次讀取檔案所有內容
print(total)
f.close()