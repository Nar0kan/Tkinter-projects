from random import choice, shuffle                                  # Build-in random lib
#from pyperclip import copy, paste                                  # External copy to clipboard lib
import customtkinter as ctk                                         # External GUI lib
import json                                                         # For operations with settings.json file
from tkinter import filedialog as fd, Toplevel
from tkinter.messagebox import showinfo


class Menu():
    programStatusInfo = {
        0: "Everything is up-to date", 
        1: "New changes to update", 
        2: "Unexpected bug found"
        }


    def __init__(self) -> None:
        self.PASSWORD = PasswordGenerator()
        self.passwordHistory = []

        with open('settings.json', 'r') as f:
            self.settings = json.load(f)

        # self.controlSum can be taken from checkControlSum method, which will
        # add one 0 or not to each next settings parameter and then combine it all
        # to the controlSum parameter, saved in settings.json probably.
        self.checkControlSum()
        print(f"Control sum: {self.controlSum}")

        # self.programStatus will look at the settings.json to find out the
        # version of the program that is used. If not the latest - new window
        # with such a message will apear, together with link on the latest build.
        self.programStatus = 0

        self.PASSWORD.generatePassword()


    def runProgram(self) -> bool:
        """Use this method to build up program."""
        self.checkControlSum()
        self.buildMainMenu()
    

    """Select settings to load"""

    def checkControlSum(self) -> bool:
        if self.settings['controlSum'] == 0:
            self.controlSum = 0
            self.loadDefaultSettings()
        else:
            self.controlSum = self.settings['controlSum']
            self.loadUserSettings()
    

    def loadDefaultSettings(self):
        self.writeHistoryOption = True
        self.PASSWORD.writeHistory(self.writeHistoryOption)

        self.PASSWORD.setLength(12)

        self.addSymbols = str("")
        self.PASSWORD.addSymbols(self.addSymbols)

        self.delSymbols = str("")
        self.PASSWORD.delSymbols(self.delSymbols)

        self.useDigitsOption = True
        self.PASSWORD.useDigits(self.useDigitsOption)
    
    
    def loadUserSettings(self):
        self.writeHistoryOption = bool(self.settings['writeHistoryOption'])
        self.PASSWORD.writeHistory(self.writeHistoryOption)

        self.PASSWORD.setLength(self.settings['passwordLength'])

        self.addSymbols = str(self.settings['addSymbols'])
        self.PASSWORD.addSymbols(self.addSymbols)

        self.delSymbols = str(self.settings['delSymbols'])
        self.PASSWORD.delSymbols(self.delSymbols)

        self.useDigitsOption = bool(self.settings['useDigits'])
        self.PASSWORD.useDigits(self.useDigitsOption)

    
    """Main window elements"""

    def loadSettingsButton(self) -> None:
        self.settingsButton = ctk.CTkButton(self.root, text="Settings", command=self.openSettingsWindow, border_width=2, bg_color="#ddf4ff",\
            fg_color="#2a2a2c")

        self.settingsButton.grid(row=0, column=1, padx=5, pady=5, sticky=ctk.E)
    
    
    def loadRetryButton(self) -> None:
        self.retryButton = ctk.CTkButton(self.root, text="Generate new", command=self.retry, border_width=2, bg_color='#ddf4ff',\
            fg_color="#2a2a2c", border_color="blue")
        
        self.retryButton.grid(row=2, column=1, padx=5, pady=5)
    

    def loadPasswordEntry(self) -> None:
        self.passwordEntry = ctk.CTkEntry(self.root, width=600, textvariable=self.PASSWORD.password,\
            text_font='arial', placeholder_text="center", border_width=2, border_color="pink")
        
        self.passwordEntry.grid(row=1, column=1, padx=10, pady=5, sticky=ctk.N)
        self.passwordEntry.insert(0, self.PASSWORD.password)

    """Settings buttons methods"""
    
    def exportPasswordHistory(self) -> None:
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))

        self.messageFilename = fd.asksaveasfilename(
            confirmoverwrite=True,
            initialfile='Passwords.txt',
            title='Saving passwords history file',
            initialdir='/',
            filetypes=filetypes)
        
        try:
            with open(self.messageFilename, 'a') as f:
                for pswd in self.PASSWORD.passwordHistory:
                    f.writelines(pswd)

            showinfo(title='Success!', message=f'File have been successfully saved as a {self.messageFilename}')
        except FileNotFoundError:
            showinfo(title='Error!', message=f'File "{self.messageFilename}" has not been found. Please try again!')
    

    def useDigits(self):
        if self.useDigitsCheckbox.get() == 0:
            self.PASSWORD.useDigits(False)
            self.useDigitsOption = False
        elif self.useDigitsCheckbox.get() == 1:
            self.PASSWORD.useDigits(True)
            self.useDigitsOption = True
    

    def writeHistory(self):
        if self.writeHistoryCheckbox.get() == 0:
            self.PASSWORD.writeHistory(False)
            self.writeHistoryOption = False
        else:
            self.PASSWORD.writeHistory(True)
            self.writeHistoryOption = True
    

    def setLength(self, value: int):
        self.passwordLengthProgressbar.set(value)
        self.PASSWORD.setLength(value)

    
    """Settings Buttons"""
    
    def saveBUFFERSettings(self):
        self.BUFFERwriteHistoryOption = self.writeHistoryOption
        self.BUFFERpasswordLength = self.PASSWORD.length
        self.BUFFERaddSymbols = self.addSymbols
        self.BUFFERdelSymbols = self.delSymbols
        self.BUFFERuseDigitsOption = self.useDigitsOption

        self.BUFFERsettings = (self.BUFFERwriteHistoryOption, self.BUFFERpasswordLength,\
            self.BUFFERaddSymbols, self.BUFFERdelSymbols, self.BUFFERuseDigitsOption)


    def exportHistoryButton(self):
        self.historyButton = ctk.CTkButton(self.settingsWindow, text='Export Password History', command=self.exportPasswordHistory)
        self.historyButton.pack()
    

    def loadPasswordLengthSlider(self):
        self.passwordLengthSlider = ctk.CTkSlider(self.settingsWindow, from_=4, to=26, number_of_steps=24, command=self.PASSWORD.setLength)
        self.passwordLengthSlider.place(relx=0.5, rely=0.5)

        self.passwordLengthSlider.set(self.PASSWORD.length)
        self.passwordLengthProgressbar = ctk.CTkProgressBar(master=self.settingsWindow, width=160, height=20, border_width=5)
        self.passwordLengthProgressbar.place(relx=0.5, rely=0.5)


    def loadCheckboxes(self):
        self.useDigitsCheckbox = ctk.CTkCheckBox(self.settingsWindow, text='Use digits', command=self.useDigits)
        self.useDigitsCheckbox.place(relx=0.5, rely=0.5)
        if "0123456789" in self.PASSWORD.alphabet:
            self.useDigitsCheckbox.select()
        
        self.writeHistoryCheckbox = ctk.CTkCheckBox(self.settingsWindow, text='Write password history', command=self.writeHistory)
        self.writeHistoryCheckbox.place(relx=0.5, rely=0.5)
        self.writeHistoryCheckbox.select(self.PASSWORD.history)
    

    def saveSettings(self):
        self.settings['writeHistoryOption'] = bool(self.writeHistoryOption)
        self.settings['passwordLength'] = int(self.PASSWORD.length)
        self.settings['addSymbols'] = str(self.addSymbols)
        self.settings['delSymbols'] = str(self.delSymbols)
        self.settings['useDigits'] = bool(self.useDigitsOption)

        self.controlSum = 1
        self.settings['controlSum'] = self.controlSum

        cfg = json.dumps(self.settings)
        with open('settings.json', 'w') as f:
            f.write(cfg)
        
        self.refresh()
    

    def abortSettings(self):
        self.settings['writeHistoryOption'] = bool(self.BUFFERwriteHistoryOption)
        self.settings['passwordLength'] = int(self.BUFFERpasswordLength)
        self.settings['addSymbols'] = str(self.BUFFERaddSymbols)
        self.settings['delSymbols'] = str(self.BUFFERdelSymbols)
        self.settings['useDigits'] = bool(self.BUFFERuseDigitsOption)

        cfg = json.dumps(self.settings)

        with open('settings.json', 'w') as f:
            f.write(cfg)

        self.refresh()


    def useDefaultSettings(self):
        self.loadDefaultSettings()
        self.settings = {
            'controlSum': 0,
            'writeHistory': True,
            'passwordLength': 12,
            'addSymbols': '',
            'delSymbols': '',
            'useDigits': True,
            'build': "0.2.1",
        }
        self.controlSum = 0

        cfg = json.dumps(self.settings)
        with open('settings.json', 'w') as f:
            f.write(cfg)
        
        self.refresh()
    

    """Main menu buttons methods"""

    def openSettingsWindow(self):
        self.saveBUFFERSettings()
        self.settingsWindow = Toplevel(self.root)
        self.settingsWindow.geometry("620x300")
        self.settingsWindow.title("Settings")
        
        self.loadPasswordLengthSlider()
        self.exportHistoryButton()
        self.loadCheckboxes()
        self.saveChangedButton = ctk.CTkButton(self.settingsWindow, text='Save changes', command=self.saveSettings)
        self.saveChangedButton.pack()
        self.abortChangedButton = ctk.CTkButton(self.settingsWindow, text='Abort changes', command=self.abortSettings)
        self.abortChangedButton.pack()
        self.useDefaultButton = ctk.CTkButton(self.settingsWindow, text='Default', command=self.useDefaultSettings)
        self.useDefaultButton.pack()

        self.settingsWindow.resizable(False, False)
        self.settingsWindow.mainloop()

    
    def retry(self) -> None:
        self.passwordHistory.append(self.PASSWORD.password)
        self.PASSWORD.generatePassword()
        self.loadPasswordEntry()


    """Function to display everything"""
    def refresh(self) -> None:
        self.settingsWindow.destroy()
        self.root.destroy()

        with open('settings.json', 'r') as f:
            self.settings = json.load(f)
        
        self.checkControlSum()
        self.buildMainMenu()


    def buildMainMenu(self) -> None:
        ctk.set_appearance_mode("Dark")

        self.root = ctk.CTk()
        self.root.title("PassGen 0.3")
        self.root.geometry("620x180")
        self.root.iconbitmap("pglogo2.png")

        self.loadSettingsButton()
        self.loadRetryButton()
        self.loadPasswordEntry()

        self.root.resizable(False, False)
        self.root.mainloop()


class PasswordGenerator:
    def __init__(self, length: int=12, alphabet: str="", addDigits: bool=True, otherSymbols: str="") -> None:
        self.length = length

        if not alphabet:
            self.alphabet = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
        else:
            self.alphabet = alphabet
        
        if addDigits:
            self.alphabet += "0123456789"
        
        self.alphabet += otherSymbols
        self.passwordHistory = []
        self.writeHistory()


    def generatePassword(self) -> str:
        self.password = ''
        for i in range(self.length):
            self.password += choice(self.alphabet)
        
        if self.history:
            self.passwordHistory.append(self.password)
        
        return self.password


    def setLength(self, newLength: int) -> None:
        self.length = newLength
    

    def addSymbols(self, symbols) -> None:
        for symbol in symbols:
            if symbol not in self.alphabet:
                self.alphabet += symbols
    

    def delSymbols(self, symbols) -> None:
        for symbol in symbols:
            if symbol in self.alphabet:
                self.alphabet = self.alphabet[0:self.alphabet.find(symbol)] + self.alphabet[self.alphabet.find(symbol)+1:]

    
    def useDigits(self, option: bool=True) -> None:
        if option and "0123456789" not in self.alphabet:
            self.alphabet += "0123456789"
        elif not option and "0123456789" in self.alphabet:
            self.alphabet = self.alphabet[0:self.alphabet.find("0123456789")] + self.alphabet[self.alphabet.find("0123456789")+10:]

    
    def writeHistory(self, option: bool=True) -> None:
        self.history = option


def main() -> None:
    OBJ = Menu()
    OBJ.runProgram()
    return OBJ.programStatus


if __name__=='__main__':
    main()