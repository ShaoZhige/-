import random
import tkinter as tk
window=tk.Tk()
window.title("猜数游戏")
window_width=253
window_height=237
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x_coordinate=int((screen_width / 2) - (window_width / 2))
y_coordinate=int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
window.resizable(False, False)
bg_image=tk.PhotoImage(file="images/bg_image.png")
bg_label=tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
a=int(random.randint(1, 100))
b=10
label=tk.Label(window, text="猜整数，范围在1-100内。你一共有10次机会。", font=("Helvetica", 9))
label.place(relx=0.52, rely=0.4, anchor=tk.CENTER)
def guess_number():
    global b
    c=int(entry.get())
    if a==c:
        label.config(text="宾果！答对了！")
        entry.config(state=tk.DISABLED)
        button.config(state=tk.DISABLED)
    elif a<c:
        b=b - 1
        label.config(text="大了，宝。还有{}次机会。".format(b))
    else:
        b=b - 1
        label.config(text="小了，宝。还有{}次机会。".format(b))
    if b==0:
        label.config(text="笨比，你没机会了。答案是:{}！".format(a))
        entry.config(state=tk.DISABLED)
        button.config(state=tk.DISABLED)
entry=tk.Entry(window, font=("Helvetica", 12))
entry.place(relx=0.51, rely=0.48, anchor=tk.CENTER)
button=tk.Button(window, text="确定", font=("Helvetica", 9), command=guess_number)
button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
window.mainloop()