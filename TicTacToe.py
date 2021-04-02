from tkinter import *

root = Tk()
root.title("Tic Tac Toe v.0.4")
root.geometry(f"400x480")

#Functions:
t = 0
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def sign(k):
    global t, lst
    if t % 2 == 0:
        button = Button(text="X", padx=60, pady=50)
        lst[k-1] = "x"
    else:
        button = Button(text="0", padx=60, pady=50)
        lst[k-1] = "0"
    if k == 1:
        button.grid(column=0, row=0)
    elif k == 2:
        button.grid(column=1, row=0)
    elif k == 3:
        button.grid(column=2, row=0)
    elif k == 4:
        button.grid(column=0, row=1)
    elif k == 5:
        button.grid(column=1, row=1)
    elif k == 6:
        button.grid(column=2, row=1)
    elif k == 7:
        button.grid(column=0, row=2)
    elif k == 8:
        button.grid(column=1, row=2)
    else:
        button.grid(column=2, row=2)
    t+=1
    print(check())
    return button

def clear():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9
    global t, lst
    button_1 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(1))
    button_2 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(2))
    button_3 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(3))
    button_4 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(4))
    button_5 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(5))
    button_6 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(6))
    button_7 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(7))
    button_8 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(8))
    button_9 = Button(text=" ", padx=60, pady=50, bd=3, command=lambda: sign(9))
    button_1.grid(column=0, row=0)
    button_2.grid(column=1, row=0)
    button_3.grid(column=2, row=0)
    button_4.grid(column=0, row=1)
    button_5.grid(column=1, row=1)
    button_6.grid(column=2, row=1)
    button_7.grid(column=0, row=2)
    button_8.grid(column=1, row=2)
    button_9.grid(column=2, row=2)
    t = 0
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def check():
    global lst, t, h
    if lst[0] == lst[1] == lst[2]:
        h = 1
        change_color(0, 1, 2)
        return "Game over!"
    elif lst[3] == lst[4] == lst[5]:
        h = 2
        change_color(3, 4, 5)
        return "Game over!"
    elif lst[6] == lst[7] == lst[8]:
        h = 3
        change_color(6, 7, 8)
        return "Game over!"
    elif lst[0] == lst[3] == lst[6]:
        h = 4
        change_color(0, 3, 6)
        return "Game over!"
    elif lst[1] == lst[4] == lst[7]:
        h = 5
        change_color(1, 4, 7)
        return "Game over!"
    elif lst[2] == lst[5] == lst[8]:
        h = 6
        change_color(2, 5, 8)
        return "Game over!"
    elif lst[0] == lst[4] == lst[8]:
        h = 7
        change_color(0, 4, 8)
        return "Game over!"
    elif lst[2] == lst[4] == lst[6]:
        h = 8
        change_color(2, 4, 6)
        return "Game over!"
    elif t >= 9:
        clear()
        return "Friendship won!"
    else:
        pass

def change_color(k, l, m):
    global lst, h
    btn1 = Button(text = lst[k], padx = 60, pady = 50, bd = 1, bg = "yellow")
    btn2 = Button(text = lst[l], padx = 60, pady = 50, bd = 1, bg = "yellow")
    btn3 = Button(text = lst[m], padx = 60, pady = 50, bd = 1, bg = "yellow")
    def btngrid(c1, c2, c3, r1, r2, r3):
        btn1.grid(column=c1, row=r1)
        btn2.grid(column=c2, row=r2)
        btn3.grid(column=c3, row=r3)
    if h == 1:
        btngrid(0, 1, 2, 0, 0, 0)
    elif h == 2:
        btngrid(0, 1, 2, 1, 1, 1)
    elif h == 3:
        btngrid(0, 1, 2, 2, 2, 2)
    elif h == 4:
        btngrid(0, 0, 0, 0, 1, 2)
    elif h == 5:
        btngrid(1, 1, 1, 0, 1, 2)
    elif h == 6:
        btngrid(2, 2, 2, 0, 1, 2)
    elif h == 7:
        btngrid(0, 1, 2, 0, 1, 2)
    else:
        btngrid(0, 1, 2, 2, 1, 0)

# Buttons
button_1 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(1))
button_2 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(2))
button_3 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(3))
button_4 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(4))
button_5 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(5))
button_6 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(6))
button_7 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(7))
button_8 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(8))
button_9 = Button(text = " ", padx = 60, pady = 50, bd = 2, command = lambda: sign(9))
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