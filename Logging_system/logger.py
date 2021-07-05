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
                            command = lambda: login_user([nickname.get(1.0, 16.0), password.get(1.0, 20.0)], top))
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
                            command=lambda: create_user([nickname.get(1.0, 16.0), password.get(1.0, 20.0)], top))
    confirm_button.grid(row=4, column=1, pady=15, padx=5)

    cancel_button = Button(su_label, width=15, height=2, text="Cancel", command=lambda: on_cancel(top))
    cancel_button.grid(row=4, column=3, pady=15, padx=5)

# here we check from out txt file if user is already registered\ for login
def login_user(user_info, top):
    loggins = open('loggins.txt', 'r')
    k = list(loggins.readlines())
    
    if user_info == k:
        messagebox.showinfo(title='Success', message='You are logged in as ' + user_info[0])

        # feature to show result on Main program window
        My_label['text'] = " Hello, " + user_info[0]
        My_label.grid(row = 2, column = 0, rowspan = 5)
    else:
        messagebox.showinfo(title = 'Problem', message = 'Your input isn\'t correct!')
        on_cancel(top)
    
    loggins.close()
    top.destroy()

# here we will write a new user after we check if he is not existing\ for sign up
def create_user(user_info, top):
    global My_label

    # check if user exist
    loggins = open('loggins.txt', 'r')
    k = list(loggins.readlines())
    
    if user_info == k:
        messagebox.showerror(message = 'This user already exist.')
        on_cancel(top)

    loggins.close()

    # and now we can add new user in our file
    loggins = open('loggins.txt', 'w')
    line = str(user_info[0]) + str(user_info[1])
    loggins.writelines(line)

    # end process
    loggins.close()
    on_cancel(top)

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
