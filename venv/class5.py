#Simple calculator

from tkinter import *

root = Tk()
root.title("Calculator - By Rahul Soni")
root.geometry("600x600")
root.resizable(0, 0)
root.config(background='black')

a = StringVar()


def add(s):
    b = a.get()
    a.set(b+s)


def evaluate():
    try:
        s = eval(a.get())
        a.set(s)
    except SyntaxError:
        a.set("Syntax Error")


def clear():
    a.set("")


display = Label(root, textvariable=a, font=("", 23), background="grey", fg="white", width=21)
display.grid(row=2, column=1, columnspan=3, padx=(20, 0), pady=(20, 0), sticky="E")

button1 = Button(root, text="1", width=10, font=("", 16), command=lambda: add("1"))
button1.grid(row=3, column=1, padx=(20, 0))

button2 = Button(root, text="2", width=10, font=("", 16), command=lambda: add("2"))
button2.grid(row=3, column=2)

button3 = Button(root, text="3", width=10, font=("", 16), command=lambda: add("3"))
button3.grid(row=3, column=3)

button_plus = Button(root, text="+", width=10, font=("", 16), command=lambda: add("+"))
button_plus.grid(row=3, column=4)

button4 = Button(root, text="4", width=10, font=("", 16), command=lambda: add("4"))
button4.grid(row=4, column=1, padx=(20, 0))

button5 = Button(root, text="5", width=10, font=("", 16), command=lambda: add("5"))
button5.grid(row=4, column=2)

button6 = Button(root, text="6", width=10, font=("", 16), command=lambda: add("6"))
button6.grid(row=4, column=3)

button_minus = Button(root, text="-", width=10, font=("", 16), command=lambda: add("-"))
button_minus.grid(row=4, column=4)

button7 = Button(root, text="7", width=10, font=("", 16), command=lambda: add("7"))
button7.grid(row=5, column=1, padx=(20, 0))

button8 = Button(root, text="8", width=10, font=("", 16), command=lambda: add("8"))
button8.grid(row=5, column=2)

button9 = Button(root, text="9", width=10, font=("", 16), command=lambda: add("9"))
button9.grid(row=5, column=3)

button_divide = Button(root, text="/", width=10, font=("", 16), command=lambda: add("/"))
button_divide.grid(row=5, column=4)

button_dot = Button(root, text=".", width=10, font=("", 16), command=lambda: add("."))
button_dot.grid(row=6, column=1, padx=(20, 0))

button0 = Button(root, text="0", width=10, font=("", 16), command=lambda: add("0"))
button0.grid(row=6, column=2)

button_equal = Button(root, text="=", width=10, font=("", 16), command=evaluate)
button_equal.grid(row=6, column=3)

button_multiply = Button(root, text="*", width=10, font=("", 16), command=lambda: add("*"))
button_multiply.grid(row=6, column=4)

button_clear = Button(root, text="C", width=10, font=("", 16), background="red", fg="white", command=clear)
button_clear.grid(row=2, column=4, pady=(20, 0))

root.mainloop()
