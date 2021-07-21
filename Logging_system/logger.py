from tkinter import *
from tkinter import messagebox

# main window initialization
root = Tk()
root.title('Main program')
root.geometry(f'400x200')
root.config(bg = 'grey')

# label
My_label = Label(root, text = " Hello, user!", font = 24, bg = 'gray', fg = 'purple')

class Verification:
    def __init__(self, user_info, top, option):
        self._user_info = user_info
        self._top = top
        if option == "sign_up":
            self.create_account()
        else:
            self.login_user()

    @staticmethod
    def check_user(user_info):
        # open file
        loggins = open('loggins.txt', 'r')
        k_list = list(loggins.readlines())
        loggins.close()
        print(k_list)
        
        for couple in range(1, len(k_list)):
           # print(k_list[couple])
            print(user_info)
            if str(user_info[0]) == str(k_list[couple-1]) and str(user_info[1]) == str(k_list[couple]):
                return True
        
        return False
        

    def login_user(self):
        
        if self.check_user(self._user_info):
            messagebox.showinfo(title = 'Success', message = 'You are logged in as ' + self._user_info[0])

            # feature to show result on Main program window
            #My_label['text'] = " Hello, " + self._user_info[0]
            #My_label.grid(row = 2, column = 0, rowspan = 5)  
        else:
            messagebox.showinfo(title = 'Problem', message = 'You have entered wrong password or login!')
            self.on_cancel(self._top)
        
        
        return self._top.destroy()

    
    def create_account(self):
        # check if user exist
        if self.check_user(self._user_info):
            messagebox.showerror(message = 'This user already exist.')
            self.on_cancel(self._top)
            return None
        else:
            # and now we can add new user in our file
            loggins = open('loggins.txt', 'a')
            #line = (str(self._user_info[0][:-1]), str(self._user_info[1][:-1]))
            loggins.writelines("".join(self._user_info))
            loggins.close()

        self.on_cancel(self._top)

    # def for cancel button
    @staticmethod
    def on_cancel(top):
        top.destroy()
        log_button['state'] = NORMAL
        sign_up_button['state'] = NORMAL
        


# some functions for login/sign up
class Not_logged_Menu(Verification):
    def __init__(self, option):
        if option == "login":
            self.login()
        else:
            self.sign_up()
        pass

    @staticmethod
    def set_buttons_state_disabled():
        log_button['state'] = DISABLED
        sign_up_button['state'] = DISABLED

    
    def login(self):
        self.set_buttons_state_disabled()
        
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
                                command = lambda: Verification((nickname.get(1.0, 16.0), password.get(1.0, 20.0)), top, 'login'))
        confirm_button.grid(row = 4, column = 1, pady = 15, padx = 5)

        cancel_button = Button(log_label, width=15, height=2, text="Cancel", command=lambda: self.on_cancel(top))
        cancel_button.grid(row=4, column=3, pady=15, padx=5)


    def sign_up(self):
        self.set_buttons_state_disabled()
        
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
                                command=lambda: Verification((nickname.get(1.0, 16.0), password.get(1.0, 20.0)), top, 'sign_up'))
        confirm_button.grid(row=4, column=1, pady=15, padx=5)

        cancel_button = Button(su_label, width=15, height=2, text="Cancel", command=lambda: self.on_cancel(top))
        cancel_button.grid(row=4, column=3, pady=15, padx=5)

#Objects
def option(option):
    menu = Not_logged_Menu(option)

# some initializations for the elements
My_label.grid(row = 2, column = 0, rowspan = 5)

log_button = Button(root, text = " Login ", padx = 20, pady = 10, fg = 'pink',
                    bg = 'black', command = lambda: option('login'))
sign_up_button = Button(root, text = " Sign up ", padx = 20, pady = 10, fg = 'pink',
                        bg = 'black', command = lambda: option('sign_up'))

log_button.grid(row = 1, column = 5, padx = 200, pady = 5)
sign_up_button.grid(row = 0, column = 5, padx = 200, pady = 10)

root.mainloop()
