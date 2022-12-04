from tkinter import *
from tkinter import ttk


def main():
    Game_window = Game()


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tic Tac Toe v.0.6")
        self.root.geometry("647x720")

        req_width = self.root.winfo_reqwidth()
        req_height = self.root.winfo_reqheight()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int(screen_width / 2 - req_width / 2)
        y = int(screen_height / 2 - req_height)
        
        self.root.geometry(f"+{x}+{y}")
        self.root.resizable(False, False)
        self.buttons_init()
        self.root.mainloop()
    

    def change_value(self, button):
        button['text']='X'
        self.buttons[]['state']='disabled'
        while self.game_status == True:
            for key in self.buttons:
                print(key)
                if self.buttons[key]['state']!='disabled':
                    return None
                else:
                    self.exit_game()
    
    #bg='blue', bd=2, width=24, height=12, 
    def buttons_init(self) -> None: # Button(text=lst[k], padx=60, pady=50, bd=1, bg="green").grid(column= h_list[0], row= h_list[3])
        self.game_status = True
        self.buttons = {}
        self.buttons_label = Label(self.root, width=0).grid(column=1, row=0, columnspan=2, rowspan=2)

        for col in range(3):
            for row in range(3):
                place = Button(self.buttons_label, text=" ", bg='blue', bd=2, width=24, height=12)
                place.config(command=lambda: self.change_value(place))
                place.grid(column=col, row=row, padx=5, pady=5)
                self.buttons[str(col)+str(row)] = place
        
        self.retry_button = Button(self.buttons_label, text="Try again", bg='yellow', bd=2, width=40, height=8)
        self.retry_button.grid(column=1, row = 4, pady=10)
        
        print(self.buttons)
        

    def exit_game(self) -> None:
        exit()


if __name__== "__main__":
    main()