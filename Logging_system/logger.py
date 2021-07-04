from tkinter import *
from tkinter import messagebox

# main window initialization
root = Tk()
root.title('Main program')
root.geometry(f'400x200')
root.config(bg = 'grey')

# label
My_label = Label(root, text = " Hello, USER!", font = 24, bg = 'gray', fg = 'purple')

# some functions for login/sign up
def login():
    log_button['state'] = DISABLED
    sign_up_button['state'] = DISABLED
    top = Toplevel(root)
    top.title('Login window')
    top.geometry(f"470x130")
    log_label = Label(top, text = '\n\nNickname \n \n \n \nPassword ', fg = 'pink', bg = 'black', height = 220, width = 300)
    log_label.grid(columnspan = 3, rowspan = 3)

    nickname = Text(log_label, width = 25, height = 1, pady = 5)
    password = Text(log_label, width = 25, height = 1, pady = 5)
    nickname.grid(row = 2, column = 2, pady = 13, padx = 5)
    password.grid(row = 4, column = 2, pady = 13, padx = 5)

    confirm_button = Button(log_label, width = 15, height = 2, text = "Confirm",
                            command = lambda: check_user([nickname.get(1.0), password.get(1.0)]))
    confirm_button.grid(row = 4, column = 1, pady = 15, padx = 5)

    cancel_button = Button(log_label, width=15, height=2, text="Cancel", command=lambda: on_cancel(top))
    cancel_button.grid(row=4, column=3, pady=15, padx=5)


def sign_up():
    log_button['state'] = DISABLED
    sign_up_button['state'] = DISABLED
    top = Toplevel(root)
    top.title('Sign-up window')
    top.geometry(f"470x130")
    su_label = Label(top, text='\n\nNickname \n \n \n \nPassword ', fg='pink', bg='black', height=220, width=300)
    su_label.grid(columnspan=3, rowspan=3)

    nickname = Text(su_label, width=25, height=1, pady=5)
    password = Text(su_label, width=25, height=1, pady=5)
    nickname.grid(row=2, column=2, pady=13, padx=5)
    password.grid(row=4, column=2, pady=13, padx=5)

    confirm_button = Button(su_label, width=15, height=2, text="Confirm",
                            command=lambda: check_user([nickname.get(1.0), password.get(1.0)]))
    confirm_button.grid(row=4, column=1, pady=15, padx=5)

    cancel_button = Button(su_label, width=15, height=2, text="Cancel", command=lambda: on_cancel(top))
    cancel_button.grid(row=4, column=3, pady=15, padx=5)

# here we check from out txt file if user is already registered\ for login
def check_user(user_info):
    loggins = open('loggins.txt', 'r')
    k = 0
    if user_info == dict(loggins.readline(0)):
        k = 1
    else:
        k = 0
    loggins.close()

# here we will write a new user after we check if he is not existing\ for sign up
def create_user():
    pass

def clear_bar(bar):
    bar.delete(1.0, END)

# def for cancel button
def on_cancel(top):
    top.destroy()
    log_button['state'] = NORMAL
    sign_up_button['state'] = NORMAL

# some initializations for the elements
My_label.grid(row = 2, column = 0, rowspan = 5)

log_button = Button(root, text = " Login ", padx = 20, pady = 10, fg = 'pink', bg = 'black', command = lambda: login())
sign_up_button = Button(root, text = " Sign up ", padx = 20, pady = 10, fg = 'pink', bg = 'black', command = lambda: sign_up())

log_button.grid(row = 1, column = 5, padx = 200, pady = 5)
sign_up_button.grid(row = 0, column = 5, padx = 200, pady = 10)
root.mainloop()
