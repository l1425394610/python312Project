import tkinter as tk


def btn_click():
    print("hello")


if __name__ == '__main__':
    window = tk.Tk()
    window.title("demo")
    window.geometry('500x500')
    btn = tk.Button(window, text="上传", width=15, height=2, command=btn_click)
    btn.pack()
    window.mainloop()
