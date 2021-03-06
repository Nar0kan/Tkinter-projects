from tkinter import *

root = Tk()
root.title("Tic Tac Toe v.0.6")
root.geometry(f"400x480")

#Functions // t == turn for o's and x's // lst for overwriting this x's and o's inside
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

    # k_list stores inside all possible pos for buttons.grid(column , row) func
    k_list = [[0, 0], [1, 0], [2, 0], [0, 1],
              [1, 1], [2,1], [0,2], [1,2], [2,2]]

    button.grid(column = k_list[k-1][0], row = k_list[k-1][1])

    t+=1
    print(check())
    return button

def clear():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9
    global t, lst
    # init buttons to clear them with text == " " and bd == 3
    buttons_init(" ", 3)
    # update variables data to default
    t = 0
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def check():
    global lst, t
    # check if 3 x's or o's are in one row to stop game | last digit in change_color is h - case of lst[] equality
    if lst[0] == lst[1] == lst[2]:
        change_color(0, 1, 2, 1)
        return "Game over!"
    elif lst[3] == lst[4] == lst[5]:
        change_color(3, 4, 5, 2)
        return "Game over!"
    elif lst[6] == lst[7] == lst[8]:
        change_color(6, 7, 8, 3)
        return "Game over!"
    elif lst[0] == lst[3] == lst[6]:
        change_color(0, 3, 6, 4)
        return "Game over!"
    elif lst[1] == lst[4] == lst[7]:
        change_color(1, 4, 7, 5)
        return "Game over!"
    elif lst[2] == lst[5] == lst[8]:
        change_color(2, 5, 8, 6)
        return "Game over!"
    elif lst[0] == lst[4] == lst[8]:
        change_color(0, 4, 8, 7)
        return "Game over!"
    elif lst[2] == lst[4] == lst[6]:
        change_color(2, 4, 6, 8)
        return "Game over!"
    elif t >= 9:
        clear()
        return "Friendship won!"

def change_color(k, l, m, h):
    global lst

    def btngrid(h_list):
        btn1 = Button(text=lst[k], padx=60, pady=50, bd=1, bg="yellow").grid(column= h_list[0], row= h_list[3])
        btn2 = Button(text=lst[l], padx=60, pady=50, bd=1, bg="yellow").grid(column= h_list[1], row= h_list[4])
        btn3 = Button(text=lst[m], padx=60, pady=50, bd=1, bg="yellow").grid(column= h_list[2], row= h_list[5])

    # here is used h_list to collect each of possible btngrid(c1 , c2, c3, r1, r2, r3) pos for buttons to highlight
    h_list = [[0, 1, 2, 0, 0, 0], [0, 1, 2, 1, 1, 1], [0, 1, 2, 2, 2, 2], [0, 0, 0, 0, 1, 2],
              [1, 1, 1, 0, 1, 2], [2, 2, 2, 0, 1, 2], [0, 1, 2, 0, 1, 2], [0, 1, 2, 2, 1, 0]]

    btngrid(h_list[h-1])

# Buttons initialization for main menu// here is functions bcs we need to call clear() func with the same commands
def buttons_init(text, bd):
    button_1 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(1)).grid(column = 0, row = 0)
    button_2 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(2)).grid(column = 1, row = 0)
    button_3 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(3)).grid(column = 2, row = 0)
    button_4 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(4)).grid(column = 0, row = 1)
    button_5 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(5)).grid(column = 1, row = 1)
    button_6 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(6)).grid(column = 2, row = 1)
    button_7 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(7)).grid(column = 0, row = 2)
    button_8 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(8)).grid(column = 1, row = 2)
    button_9 = Button(text = text, padx = 60, pady = 50, bd = bd, command = lambda: sign(9)).grid(column = 2, row = 2)

buttons_init(" ", 2)
button_refresh = Button(text = "Try again!", padx = 100, pady = 40, command = lambda: clear()).grid(column = 0, row = 3, columnspan = 3)

root.mainloop()