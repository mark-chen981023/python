from tkinter import *

change = False


def hifun():
    global change
    print("hello")
    if change == False:
        display.config(text="Hi singular", fg="red",
                       bg="black")  #config=設定,display.config重新設定Label)
    else:
        display.config(text="hi", fg="red", bg="#00BCA2")
    change = not (change)


win = Tk()  #把物件存到變數中
win.title("My first GUI")  #命名標題
display = Label(win, text="hi", fg="red", bg="#00BCA2")  #Label是文字
display.pack()
btn = Button(
    win, text="click me", command=hifun, fg="#0000FA",
    bg="green")  #(fg=frontground=文字,bg=background=按鈕)第一格是想放入的視窗,第二格按鈕,第三格功能
btn.pack()  #(把按鈕打包到視窗上)

win.mainloop()  #維持畫面維持畫面
