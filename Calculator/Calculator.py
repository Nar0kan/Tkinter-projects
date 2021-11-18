from tkinter import *

class Interface():


    def nums(self, number):
        digit = self.ebox.get()
        self.ebox.delete(0, END)
        num = digit + str(number)
        self.ebox.insert(0, num)


    def clear(self):
        self.ebox.delete(0, END)


    def first_num(self, operator):
        self.operator = operator
        first_num = self.ebox.get()
        try:
            self.num1 = float(first_num)
        except: ValueError("Wrong value!")
        self.ebox.delete(0, END)


    def second_num(self):
        second_num = self.ebox.get()
        self.ebox.delete(0, END)
        try:
            self.num2 = float(second_num)
        except: ValueError("Wrong value!")
        self.operation()


    def operation(self):
        if self.operator == '+':
            try:
                self.ebox.insert(0, self.num1 + self.num2)
            except: UnboundLocalError("Some error was made during calculations.")
        elif self.operator == '-':
            try:
                self.ebox.insert(0, self.num1 - self.num2)
            except: UnboundLocalError("Some error was made during calculations.")
        elif self.operator == '/':
            try:
                self.ebox.insert(0, self.num1 / self.num2)
            except: UnboundLocalError("Some error was made during calculations.")
        elif self.operator == '*':
            try:
                self.ebox.insert(0, self.num1 * self.num2)
            except: UnboundLocalError("Some error was made during calculations.")


    # initialization of virtual elements
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator v0.9.1")
        self.root.geometry(f"264x272")
        self.root.iconbitmap("LogoCalculator.ico")

        self.ebox = Entry(self.root, width = 40, borderwidth = 6)
        self.ebox.grid(column = 0, row = 0, columnspan = 4, padx = 6, pady = 2)
        self.ebox.insert(0, "")
        
        self.button_init()


    def button_init(self, color_bg_nums = '#72C493', color_fg_nums = 'black', color_bg_adbut = '#52A133', color_fg_adbut = 'black'):
        self.Button1 = Button(self.root, text = "1", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 1))   # nums will call the output on ebox
        self.Button2 = Button(self.root, text = "2", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 2))
        self.Button3 = Button(self.root, text = "3", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 3))
        self.Button4 = Button(self.root, text = "4", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 4))
        self.Button5 = Button(self.root, text = "5", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 5))
        self.Button6 = Button(self.root, text = "6", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 6))
        self.Button7 = Button(self.root, text = "7", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 7))
        self.Button8 = Button(self.root, text = "8", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 8))
        self.Button9 = Button(self.root, text = "9", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 15, pady = 15, command = lambda: Interface.nums(self, 9))
        self.Button0 = Button(self.root, text = "0", bd = 5, bg = color_bg_nums, fg = color_fg_nums, padx = 10, pady = 10, command = lambda: Interface.nums(self, 0))
        self.Button1.grid(column = 0, row = 3, stick = 'wens')
        self.Button2.grid(column = 1, row = 3, stick = 'wens')
        self.Button3.grid(column = 2, row = 3, stick = 'wens')
        self.Button4.grid(column = 0, row = 2, stick = 'wens')
        self.Button5.grid(column = 1, row = 2, stick = 'wens')
        self.Button6.grid(column = 2, row = 2, stick = 'wens')
        self.Button7.grid(column = 0, row = 1, stick = 'wens')
        self.Button8.grid(column = 1, row = 1, stick = 'wens')
        self.Button9.grid(column = 2, row = 1, stick = 'wens')
        self.Button0.grid(column = 0, row = 4, stick = 'wens')

        self.Buttona = Button(self.root, text = "+", padx = 15, pady = 15, bd = 5, bg = color_bg_adbut, fg = color_fg_adbut, font = ('Arial', 8), command = lambda: self.first_num('+'))
        self.Buttons = Button(self.root, text = "-", padx = 15, pady = 15, bd = 5, bg = color_bg_adbut, fg = color_fg_adbut, font = ('Arial', 8), command = lambda: self.first_num('-'))
        self.Buttonm = Button(self.root, text = "*", padx = 15, pady = 15, bd = 5, bg = color_bg_adbut, fg = color_fg_adbut, font = ('Arial', 8), command = lambda: self.first_num('*'))
        self.Buttond = Button(self.root, text = "/", padx = 15, pady = 15, bd = 5, bg = color_bg_adbut, fg = color_fg_adbut, font = ('Arial', 8), command = lambda: self.first_num('/'))
        self.Buttone = Button(self.root, text = "=", padx = 10, pady = 10, bd = 5, command = lambda: self.second_num())
        self.Buttonc = Button(self.root, text = "C", padx = 10, pady = 10, bd = 5, bg = 'white', fg = 'red', font = ('Arial', 12), command = lambda: self.clear())
        self.Buttone.grid(column = 1, row = 4, stick = 'wens')
        self.Buttonc.grid(column = 2, row = 4, stick = 'wens')
        self.Buttond.grid(column = 3, row = 1, stick = 'wens')
        self.Buttons.grid(column = 3, row = 2, stick = 'wens')
        self.Buttonm.grid(column = 3, row = 3, stick = 'wens')
        self.Buttona.grid(column = 3, row = 4, stick = 'wens')


calculator = Interface()
calculator.button_init('white', 'red', 'black', 'yellow')
calculator.root.mainloop()