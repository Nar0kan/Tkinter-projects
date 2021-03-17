from tkinter import *

root = Tk()
root.title("Tic Tac Toe v.0.3")
root.geometry(f"400x480")

#Functions:
t = 0
def x1(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=0, row=0)
    t += 1
    return button
def x2(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=1, row=0)
    t+=1
    return button
def x3(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=2, row=0)
    t+=1
    return button
def x4(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=0, row=1)
    t+=1
    return button
def x5(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=1, row=1)
    t+=1
    return button
def x6(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=2, row=1)
    t+=1
    return button
def x7(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=0, row=2)
    t+=1
    return button
def x8(button):
    global t
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
    else:
        button = Button(text="0", padx=60, pady=50)
    button.grid(column=1, row=2)
    t+=1
    return button
def x9(button):
    global t
    if t % 2 == 0:
        button = Button(text = "X", padx = 60, pady = 50)
    else:
        button = Button(text = "0", padx = 60, pady = 50)
    button.grid(column = 2, row = 2)
    t+=1
    return button

def clear():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9
    button_1 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x1(button_1))
    button_2 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x2(button_2))
    button_3 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x3(button_3))
    button_4 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x4(button_4))
    button_5 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x5(button_5))
    button_6 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x6(button_6))
    button_7 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x7(button_7))
    button_8 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x8(button_8))
    button_9 = Button(text=" ", padx=60, pady=50, bd=2, command=lambda: x9(button_9))
    button_1.grid(column=0, row=0)
    button_2.grid(column=1, row=0)
    button_3.grid(column=2, row=0)
    button_4.grid(column=0, row=1)
    button_5.grid(column=1, row=1)
    button_6.grid(column=2, row=1)
    button_7.grid(column=0, row=2)
    button_8.grid(column=1, row=2)
    button_9.grid(column=2, row=2)

button_1 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x1(button_1))
button_2 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x2(button_2))
button_3 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x3(button_3))
button_4 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x4(button_4))
button_5 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x5(button_5))
button_6 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x6(button_6))
button_7 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x7(button_7))
button_8 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x8(button_8))
button_9 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: x9(button_9))
button_refresh = Button(text = "Try again!", padx = 100, pady = 40, command = lambda: clear())
button_refresh.grid(column = 0, row = 3, columnspan = 3)
button_1.grid(column = 0, row = 0)
button_2.grid(column = 1, row = 0)
button_3.grid(column = 2, row = 0)
button_4.grid(column = 0, row = 1)
button_5.grid(column = 1, row = 1)
button_6.grid(column = 2, row = 1)
button_7.grid(column = 0, row = 2)
button_8.grid(column = 1, row = 2)
button_9.grid(column = 2, row = 2)

root.mainloop()