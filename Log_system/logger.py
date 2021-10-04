from tkinter import *
from tkinter import messagebox
import sqlite3 as sq

class CreateDB:
    def __init__(self, path):
        with sq.connect(path + "logins.db") as con:
            cur = con.cursor()      # Cursor
    
            cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                name TEXT NOT NULL PRIMARY KEY,
                password TEXT NOT NULL
            )
            """)


# class for login/sign up
class Verification:
    def __init__(self, user_info, option):
        # user_info should be tuple, that contains nickname and password info
        # option can be 'sign_up' or "log_in"
        self._user_info = user_info
        self.log_window(option)

    # build geometry for new window
    def log_window(self, option):
        global top
        top = Toplevel()
        top.title('Login window')
        top.geometry(f"470x130")
        self.set_buttons_state_disabled()
        log_label = Label(top, text = '\n\nNickname \n \n \n \nPassword ', fg = 'pink',
                         bg = 'black', height = 220, width = 300)
        log_label.grid(columnspan = 3, rowspan = 3)

        nickname = Text(log_label, width = 25, height = 1, pady = 5)
        password = Text(log_label, width = 25, height = 1, pady = 5)
        nickname.grid(row = 2, column = 2, pady = 13, padx = 5)
        password.grid(row = 4, column = 2, pady = 13, padx = 5)

        if option == 'log_in':
            confirm_button = Button(log_label, width = 15, height = 2, text = "Confirm",
                                command = lambda: self.log_in_user(self, (nickname.get(1.0, 16.0)[:-1], password.get(1.0, 20.0)[:-1])))
        elif option == 'sign_up':
            confirm_button = Button(log_label, width = 15, height = 2, text = "Confirm",
                                command = lambda: self.sign_up_user(self, (nickname.get(1.0, 16.0)[:-1], password.get(1.0, 20.0)[:-1])))
        
        confirm_button.grid(row = 4, column = 1, pady = 15, padx = 5)

        cancel_button = Button(log_label, width=15, height=2, text="Cancel", command=lambda: self.on_cancel(self))
        cancel_button.grid(row=4, column=3, pady=15, padx=5)
        

    # METHOD TO CHECK IF USERS ARE IN DATABASE AND VALIDATE THE DATA WAS GIVEN
    @staticmethod
    def check_user(user_info, option = 'log_in'):
        with sq.connect("logins.db") as con:
            cur = con.cursor()
            
            if option == 'log_in':
                cur.execute("SELECT * FROM users WHERE name = ? AND password = ?", (user_info[0], user_info[1]))
                
            elif option == 'sign_up':
                cur.execute("SELECT * FROM users WHERE name LIKE ?", (user_info[0], ))
                #sq.ProgrammingError()
                #return True
            result = cur.fetchall()
            if option == 'log_in' and not result:
                return False
            elif option == 'sign_up' and not result:
                return False
            return True
        

    def log_in_user(self, user_info):
        global top
        self._user_info = user_info
        if self.check_user(self._user_info):
            messagebox.showinfo(title = 'Success', message = 'You are logged in as ' + self._user_info[0])
            self.on_cancel(self, "Logged in")
            # here implement function to show that user is logged in and load logged menu
        else:
            messagebox.showinfo(title = 'Problem', message = 'You have entered wrong password or login!')
            self.on_cancel(self)

    
    def sign_up_user(self, user_info):
        # check if user exist
        self._user_info = user_info
        if self.check_user(self._user_info, "sign_up"):
            messagebox.showerror(message = 'This user already exist.')
            self.on_cancel(self)
            return None
        else:
            # and now we can add new user in our file
            with sq.connect('logins.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (name, password) VALUES (?, ?)", (self._user_info[0], self._user_info[1])) 

        self.on_cancel(self)

    
    # def for cancel button and for other class functions exit
    def on_cancel(self, status = "Not logged in"):
        global top, log_button, sign_up_button
        if status == "Not logged in":
            top.destroy()
            log_button['state'] = NORMAL
            sign_up_button['state'] = NORMAL
        elif status == "Logged in":
            top.destroy()
            log_button.destroy()
            sign_up_button.destroy()
            menu = Logged_Menu(self._user_info)
    
    @staticmethod
    def set_buttons_state_disabled():
        global log_button, sign_up_button
        log_button['state'] = DISABLED
        sign_up_button['state'] = DISABLED


# WHY DID I DO THAT?
class Not_Logged_Menu:
    def __init__(self, option):
        if option == "log_in":
            Verification
        else:
            Verification.sign_up(self)


class Logged_Menu:
    def __init__(self, user_info):
        self._user_info = user_info
        self._visual()

    def _visual(self):
        # here i wanna add text label which will show us that user is
        # logged in and button to unlogin out of program
        global my_label
        my_label['text'] = 'Hello, ' + self._user_info[0]
        
        unlog_button = Button(my_label, text = 'Exit account', width = 15, height = 2, command = lambda: self.unlogin())
        unlog_button.grid(row = 10, column = 10, pady = 13, padx = 5)

    def unlogin(self):
        global root
        self._user_info = (None, None)
        root.destroy()
        menu = Main()


# MAIN PROGRAM CLASS THAT YOU SEE WHEN LAUNCH THE CODE
class Main:
    @staticmethod
    def option(opt):
        menu = Not_Logged_Menu(opt)

    def __init__(self):
        #self.create_db()    \\ Creating DB file if not exists in current folder
        global root, my_label
        root = Tk()
        root.title('Main program')
        root.geometry(f'400x200')
        root.config(bg = 'grey')
    
        my_label = Label(root, text = " Hello, user!", font = 24, bg = 'gray', fg = 'purple')
        my_label.grid(row = 2, column = 0, rowspan = 5)

        global log_button, sign_up_button
        log_button = Button(root, text = " Log in ", padx = 20, pady = 10, fg = 'pink', 
                bg = 'black', command = lambda: Verification.log_window(Verification, 'log_in'))
        sign_up_button = Button(root, text = " Sign up ", padx = 20, pady = 10, fg = 'pink', 
                bg = 'black', command = lambda: Verification.log_window(Verification, 'sign_up'))
        log_button.grid(row = 1, column = 5, padx = 200, pady = 5)
        sign_up_button.grid(row = 0, column = 5, padx = 200, pady = 10)
        root.mainloop()


if __name__ == '__main__':
    program = Main()