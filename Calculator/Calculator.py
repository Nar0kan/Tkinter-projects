from tkinter import *
import os

root = Tk()
root.title("Calculator v0.9")
root.geometry(f"264x272")
root.iconbitmap("LogoCalculator.ico")

#ebox configurations
ebox = Entry(root, width = 40, borderwidth = 6)
ebox.grid(column = 0, row = 0, columnspan = 4, padx = 6, pady = 2)
ebox.insert(0, "")

operator = '0'
#Function to define a number in ebox and save it, for operations
def nums(number):
    value = ebox.get()
    ebox.delete(0, END)
    global num
    num = value + str(number)
    ebox.insert(0, num)
def add():
    first_num = ebox.get()
    global num1
    global operator
    try:
        num1 = float(first_num)
    except: ValueError("")
    ebox.delete(0, END)
    operator = '+'
def substract():
    first_num = ebox.get()
    global num1
    global operator
    try:
        num1 = float(first_num)
    except: ValueError("")
    ebox.delete(0, END)
    operator = '-'
def divide():
    first_num = ebox.get()
    global num1
    global operator
    try:
        num1 = float(first_num)
    except: ValueError("")
    ebox.delete(0, END)
    operator = '/'
def multiply():
    first_num = ebox.get()
    global num1
    global operator
    try:
        num1 = float(first_num)
    except: ValueError("")
    ebox.delete(0, END)
    operator = '*'
def clear():
    ebox.delete(0, END)

#Main result function
def equals():
    second_num = ebox.get()
    ebox.delete(0, END)
    try:
        num2 = float(second_num)
    except: ValueError("")
    if operator == '+':
        try:
            ebox.insert(0, num1 + num2)
        except:
            UnboundLocalError("")
    elif operator == '-':
        try:
            ebox.insert(0, num1 - num2)
        except:
            UnboundLocalError("")
    elif operator == '/':
        try:
            ebox.insert(0, num1 / num2)
        except:
            UnboundLocalError("")
    elif operator == '*':
        try:
            ebox.insert(0, num1 * num2)
        except: UnboundLocalError("")
    else:
        pass

#Number buttons
Button1 = Button(root, text = "1", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(1))
Button2 = Button(root, text = "2", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(2))
Button3 = Button(root, text = "3", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(3))
Button4 = Button(root, text = "4", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(4))
Button5 = Button(root, text = "5", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(5))
Button6 = Button(root, text = "6", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(6))
Button7 = Button(root, text = "7", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(7))
Button8 = Button(root, text = "8", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(8))
Button9 = Button(root, text = "9", bd = 5, bg = '#72C493', padx = 15, pady = 15, command = lambda: nums(9))
Button0 = Button(root, text = "0", bd = 5, bg = '#72C493', padx = 10, pady = 10, command = lambda: nums(0))
Button1.grid(column = 0, row = 3, stick = 'wens')
Button2.grid(column = 1, row = 3, stick = 'wens')
Button3.grid(column = 2, row = 3, stick = 'wens')
Button4.grid(column = 0, row = 2, stick = 'wens')
Button5.grid(column = 1, row = 2, stick = 'wens')
Button6.grid(column = 2, row = 2, stick = 'wens')
Button7.grid(column = 0, row = 1, stick = 'wens')
Button8.grid(column = 1, row = 1, stick = 'wens')
Button9.grid(column = 2, row = 1, stick = 'wens')
Button0.grid(column = 0, row = 4, stick = 'wens')

#Operators buttons
Buttona = Button(root, text = "+", padx = 15, pady = 15, bd = 5, bg = '#52A133', fg = 'black', font = ('Arial', 8), command = add)
Buttons = Button(root, text = "-", padx = 15, pady = 15, bd = 5, bg = '#52A133', fg = 'black', font = ('Arial', 8), command = substract)
Buttonm = Button(root, text = "*", padx = 15, pady = 15, bd = 5, bg = '#52A133', fg = 'black', font = ('Arial', 8), command = multiply)
Buttond = Button(root, text = "/", padx = 15, pady = 15, bd = 5, bg = '#52A133', fg = 'black', font = ('Arial', 8), command = divide)
Buttone = Button(root, text = "=", padx = 10, pady = 10, bd = 5, command = equals)
Buttonc = Button(root, text = "C", padx = 10, pady = 10, bd = 5, bg = 'white', fg = 'red', font = ('Arial', 12), command = clear)
Buttone.grid(column = 1, row = 4, stick = 'wens')
Buttonc.grid(column = 2, row = 4, stick = 'wens')
Buttond.grid(column = 3, row = 1, stick = 'wens')
Buttons.grid(column = 3, row = 2, stick = 'wens')
Buttonm.grid(column = 3, row = 3, stick = 'wens')
Buttona.grid(column = 3, row = 4, stick = 'wens')

root.mainloop()