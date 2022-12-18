from string import ascii_letters, digits                            # Letters and digits that are used in the alphabet
from secrets import choice as secchoice                             # This is the one that provide generator with safe sequences
from random import choice as randchoice                             # This is for not secured password
from datetime import datetime                                       # Used in export password history and generate passwords
from pyperclip import copy                                          # External copy to clipboard lib for passwords
import customtkinter as ctk                                         # External GUI lib
import json                                                         # Lib for operations with settings.json file
from tkinter import filedialog as fd, Toplevel, PhotoImage          # Additional Tkinter classes that missing in ctk
from tkinter.messagebox import showinfo                             # Class to show messagebox after file opened


class Menu():
    """Menu class to implement GUI with PasswordGenerator class object"""


    def __init__(self) -> None:
        self.PASSWORD = PasswordGenerator()
        self.passwordHistory = []

        with open('settings.json', 'r') as f:
            self.settings = json.load(f)

        self.PASSWORD.generatePassword()


    def runProgram(self) -> None:
        """The method to build up program"""
        self.checkControlSum()
        self.buildMainMenu()
    

    """_________________________--------------------|Check settings and load methods|--------------------_________________________"""

    def checkControlSum(self) -> None:
        if self.settings['controlSum'] == 0:
            self.controlSum = 0
            self.useDefaultSettings()
        else:
            self.controlSum = self.settings['controlSum']
            self.useUserSettings()
    

    def useDefaultSettings(self) -> None:
        self.writeHistoryOption = True
        self.PASSWORD.writeHistory(self.writeHistoryOption)
        
        self.useClipboard = True
        self.PASSWORD.useClipboard(self.useClipboard)

        self.PASSWORD.setLength(12)

        self.addSymbols = str("")
        self.PASSWORD.addSymbols(self.addSymbols)

        self.delSymbols = str("")
        self.PASSWORD.delSymbols(self.delSymbols)

        self.useDigitsOption = True
        self.PASSWORD.useDigits(self.useDigitsOption)
    
    
    def useUserSettings(self) -> None:
        self.writeHistoryOption = bool(self.settings['writeHistoryOption'])
        self.PASSWORD.writeHistory(self.writeHistoryOption)

        self.useClipboard = bool(self.settings['useClipboard'])
        self.PASSWORD.useClipboard(self.useClipboard)

        self.PASSWORD.setLength(self.settings['passwordLength'])

        self.addSymbols = str(self.settings['addSymbols'])
        self.PASSWORD.addSymbols(self.addSymbols)

        self.delSymbols = str(self.settings['delSymbols'])
        self.PASSWORD.delSymbols(self.delSymbols)

        self.useDigitsOption = bool(self.settings['useDigits'])
        self.PASSWORD.useDigits(self.useDigitsOption)
    
    
    def saveBUFFERSettings(self) -> None:
        self.BUFFERwriteHistoryOption = self.writeHistoryOption
        self.BUFFERuseClipboard = self.useClipboard
        self.BUFFERpasswordLength = self.PASSWORD.length
        self.BUFFERaddSymbols = self.addSymbols
        self.BUFFERdelSymbols = self.delSymbols
        self.BUFFERuseDigitsOption = self.useDigitsOption


    """_________________________--------------------|Settings window element methods|--------------------_________________________"""
    
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
                f.writelines(self.PASSWORD.getHistory())

            showinfo(title='Success!', message=f'File have been successfully saved as a {self.messageFilename}')
        except FileNotFoundError:
            showinfo(title='Error!', message=f'File "{self.messageFilename}" has not been saved. Please try again!')
    

    def useDigits(self) -> None:
        if self.useDigitsCheckbox.get() == 0:
            self.PASSWORD.useDigits(False)
            self.useDigitsOption = False
        elif self.useDigitsCheckbox.get() == 1:
            self.PASSWORD.useDigits(True)
            self.useDigitsOption = True
        else:
            raise AttributeError('self.useDigitsCheckbox.get() \
                method in Menu class must return integers (0 or 1)!')
    

    def writeHistory(self) -> None:
        if self.writeHistoryCheckbox.get() == 0:
            self.PASSWORD.writeHistory(False)
            self.writeHistoryOption = False
        elif self.writeHistoryCheckbox.get() == 1:
            self.PASSWORD.writeHistory(True)
            self.writeHistoryOption = True
        else:
            raise AttributeError('self.writeHistoryCheckbox.get() \
                method in Menu class must return integers (0 or 1)!')
        
    
    def copyToClipboard(self) -> None:
        if self.clipboardCheckbox.get() == 0:
            self.PASSWORD.useClipboard(False)
            self.useClipboard = False
        elif self.clipboardCheckbox.get() == 1:
            self.PASSWORD.useClipboard(True)
            self.useClipboard = True
        else:
            raise AttributeError('self.useClipboardCheckbox.get() \
                method in Menu class must return integers (0 or 1)!')
    

    def setLength(self, val: int) -> None:
        self.passwordLengthProgressbar.set(val/50)
        self.PASSWORD.setLength(val)
    
    
    def checkEntryValues(self) -> None:
        symbols = self.addSymbolsEntry.get()
        if symbols:
            self.addSymbols = symbols
            self.PASSWORD.addSymbols(symbols)

        symbols = self.delSymbolsEntry.get()
        if symbols:
            self.delSymbols = symbols
            self.PASSWORD.delSymbols(symbols)

    
    """_________________________--------------------|Settings window buttons|--------------------_________________________"""

    def loadExportHistoryButton(self) -> None:
        self.historyButton = ctk.CTkButton(self.settingsFrame, text='Export password history', command=self.exportPasswordHistory)
        self.historyButton.pack()
    

    def loadPasswordLengthSlider(self) -> None:
        self.passwordLengthSlider = ctk.CTkSlider(self.settingsFrame, from_=1, to=50, number_of_steps=50, command=self.setLength)
        self.passwordLengthSlider.pack(pady=10, padx=10)
        self.passwordLengthSlider.set(self.PASSWORD.length)

        self.passwordLengthProgressbar = ctk.CTkProgressBar(master=self.settingsFrame, width=160, height=20, border_width=5)
        self.passwordLengthProgressbar.set(self.PASSWORD.length/50)
        self.passwordLengthProgressbar.pack(pady=10, padx=10)


    def loadCheckboxes(self) -> None:
        self.useDigitsCheckbox = ctk.CTkCheckBox(self.settingsFrame, text='Use digits', text_color="black", command=self.useDigits)
        self.useDigitsCheckbox.pack(pady=10, padx=10)
        if digits in self.PASSWORD.alphabet:
            self.useDigitsCheckbox.select()
        
        self.writeHistoryCheckbox = ctk.CTkCheckBox(self.settingsFrame, text='Write password history', command=self.writeHistory)
        self.writeHistoryCheckbox.pack(pady=10, padx=10)
        if self.PASSWORD.history:
            self.writeHistoryCheckbox.select()
        
        self.clipboardCheckbox = ctk.CTkCheckBox(self.settingsFrame, text='Copy to clipboard', command=self.copyToClipboard)
        self.clipboardCheckbox.pack(pady=10, padx=10)
        if self.useClipboard:
            self.clipboardCheckbox.select()

    
    def loadEntries(self) -> None:
        self.addSymbolsEntry = ctk.CTkEntry(self.settingsFrame, placeholder_text="type symbols to add")
        self.addSymbolsEntry.pack(pady=5, padx=2)
        self.delSymbolsEntry = ctk.CTkEntry(self.settingsFrame, placeholder_text="type symbols to delete")
        self.delSymbolsEntry.pack(pady=5, padx=2)
    

    def loadOptionsButton(self) -> None:
        self.saveChangedButton = ctk.CTkButton(master=self.backFrame, text='Save', command=self.saveSettings)
        self.saveChangedButton.pack(padx=10, pady=5)
        self.abortChangedButton = ctk.CTkButton(master=self.backFrame, text='Cancel', command=self.abortSettings)
        self.abortChangedButton.pack(padx=10, pady=5)
        self.useDefaultButton = ctk.CTkButton(master=self.backFrame, text='Default', command=self.useDefault)
        self.useDefaultButton.pack(padx=10, pady=5)


    """_________________________--------------------|Settings overall methods|--------------------_________________________"""

    def loadValues(self, wHO: bool, uC: bool, pL: int, aS: str, dS: str, uDO: bool) -> None:
        self.settings['writeHistoryOption'] = bool(wHO)
        self.settings['useClipboard'] = bool(uC)
        self.settings['passwordLength'] = int(pL)
        self.settings['addSymbols'] = str(aS)
        self.settings['delSymbols'] = str(dS)
        self.settings['useDigits'] = bool(uDO)

    def saveSettings(self) -> None:
        self.checkEntryValues()
        self.loadValues(self.writeHistoryOption, self.useClipboard, self.PASSWORD.length,\
            self.addSymbols, self.delSymbols, self.useDigitsOption)

        self.controlSum = 1
        self.settings['controlSum'] = self.controlSum

        cfg = json.dumps(self.settings)
        with open('settings.json', 'w') as f:
            f.write(cfg)
        
        self.refresh()
    

    def abortSettings(self) -> None:
        self.loadValues(self.BUFFERwriteHistoryOption, self.BUFFERuseClipboard, self.BUFFERpasswordLength,\
            self.BUFFERaddSymbols, self.BUFFERdelSymbols, self.BUFFERuseDigitsOption)

        cfg = json.dumps(self.settings)

        with open('settings.json', 'w') as f:
            f.write(cfg)

        self.refresh()


    def useDefault(self) -> None:
        self.useDefaultSettings()
        self.PASSWORD.useDefaultAlphabet()
        self.settings = {
            'controlSum': 0,
            'writeHistory': True,
            'useClipboard': True,
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
    

    """_________________________--------------------|Main menu elements methods|--------------------_________________________"""

    def openSettingsWindow(self):
        self.saveBUFFERSettings()
        self.settingsWindow = Toplevel()
        self.settingsWindow.geometry("520x450")
        self.settingsWindow.title("Settings")

        self.nonUseFrame = ctk.CTkFrame(self.settingsWindow, bg_color="black", width=150, height=150)
        self.nonUseFrame.pack(anchor=ctk.N, fill=ctk.BOTH, expand=True, side=ctk.TOP)
        self.backFrame = ctk.CTkFrame(self.nonUseFrame, bg_color="gray", width=60, height=150)
        self.backFrame.pack(anchor=ctk.S, fill=ctk.Y, expand=True, side=ctk.BOTTOM)
        self.settingsFrame = ctk.CTkFrame(self.backFrame, bg_color="yellow", width=200, height=280, border_width=2)
        self.settingsFrame.pack(pady=10, anchor=ctk.N, fill=ctk.BOTH, expand=False, side=ctk.TOP)
        
        self.loadPasswordLengthSlider()
        self.loadExportHistoryButton()
        self.loadCheckboxes()
        self.loadEntries()
        self.loadOptionsButton()

        self.settingsWindow.resizable(False, False)
        self.settingsWindow.mainloop()

    
    def retry(self) -> None:
        self.passwordHistory.append(self.PASSWORD.password)
        self.PASSWORD.generatePassword()
        self.loadPasswordEntry()
    

    def changePasswordType(self) -> None:
        newType = self.PASSWORD.genTypes[self.PASSWORD.genTypes.index(self.PASSWORD.genType)-1]
        self.PASSWORD.setGenType(newType=newType)

        self.typeButton.destroy()
        self.typeButton = ctk.CTkButton(self.root, text=self.PASSWORD.genType, command=self.changePasswordType, border_width=2)
        self.typeButton.grid(row=3, column=1, padx=5, pady=5)
    
    
    """_________________________--------------------|Main window elements|--------------------_________________________"""

    def loadSettingsButton(self) -> None:
        settingsImage = PhotoImage(file='settingsImage.png')
        self.settingsButton = ctk.CTkButton(self.root, text="Settings", command=self.openSettingsWindow,\
            border_width=2, image=settingsImage)

        self.settingsButton.grid(row=0, column=1, padx=5, pady=5, sticky=ctk.E)
    
    
    def loadRetryButton(self) -> None:
        self.retryButton = ctk.CTkButton(self.root, text="Generate new", command=self.retry, border_width=2, bg_color='#ddf4ff',\
            fg_color="#2a2a2c", border_color="blue")
        
        self.retryButton.grid(row=2, column=1, padx=5, pady=5)
    

    def loadPasswordEntry(self) -> None:
        self.passwordEntry = ctk.CTkEntry(self.root, width=600, textvariable=self.PASSWORD.password,\
            text_font='arial', placeholder_text="Password", border_width=2, border_color="pink")
        
        self.passwordEntry.grid(row=1, column=1, padx=10, pady=5, sticky=ctk.N)
        self.passwordEntry.insert(0, self.PASSWORD.password)
    

    def loadPasswordType(self) -> None:
        self.typeButton = ctk.CTkButton(self.root, text=self.PASSWORD.genType, command=self.changePasswordType, border_width=2)
        self.typeButton.grid(row=3, column=1, padx=5, pady=5)


    """_________________________--------------------|Menu display|--------------------_________________________"""

    def buildMainMenu(self) -> None:
        ctk.set_appearance_mode("Dark")

        self.root = ctk.CTk()
        self.root.title("PassGen 0.3")
        self.root.geometry("620x200")
        
        pglogo = PhotoImage(file='pglogo2.png')
        self.root.iconphoto(False, pglogo)
        
        self.loadSettingsButton()
        self.loadRetryButton()
        self.loadPasswordEntry()
        self.loadPasswordType()

        self.root.resizable(False, False)
        self.root.mainloop()
    

    def refresh(self) -> None:
        self.settingsWindow.destroy()
        self.root.destroy()

        with open('settings.json', 'r') as f:
            self.settings = json.load(f)
        
        self.checkControlSum()
        self.buildMainMenu()


class PasswordGenerator:
    """Specific class to be called methods from for password specification changes and operations with it"""
    def __init__(self, length: int=16, alphabet: str="", addDigits: bool=True) -> None:
        self.length = length

        if not alphabet:
            self.alphabet = ascii_letters
        else:
            self.alphabet = alphabet
        
        if addDigits:
            self.alphabet += digits
        
        self.passwordHistory = []
        self.time = []

        self.genTypes = ['secured', 'unsecured']
        self.genType = 'secured'

        self.writeHistory()
        self.useClipboard()
    

    def useDefaultAlphabet(self) -> None:
        self.length = 16
        self.alphabet = ascii_letters
        self.alphabet += digits


    def generatePassword(self,) -> str:
        self.password = ''

        if self.genType == 'secured':
            for i in range(self.length):
                self.password += secchoice(self.alphabet)    
        elif self.genType == 'unsecured':
            for i in range(self.length):
                self.password += randchoice(self.alphabet)
        else:
            raise ValueError(f"!!! type argument must be in {self.genTypes}")

        if self.history:
                self.passwordHistory.append(self.password)
            
        if self.clipboard:
            copy(self.password)
        
        self.time.append(str(datetime.now()))
        return self.password
    

    def setLength(self, newLength: int) -> None:
        self.length = newLength
    

    def addSymbols(self, symbols: str) -> None:
        for symbol in symbols:
            if symbol not in self.alphabet:
                self.alphabet += symbols
    

    def delSymbols(self, symbols: str) -> None:
        for symbol in symbols:
            if symbol in self.alphabet:
                self.alphabet = self.alphabet[0:self.alphabet.find(symbol)] + self.alphabet[self.alphabet.find(symbol)+1:]

    
    def useDigits(self, option: bool=True) -> None:
        if option and digits not in self.alphabet:
            self.alphabet += digits
        elif not option and digits in self.alphabet:
            self.alphabet = self.alphabet[0:self.alphabet.find(digits)] + self.alphabet[self.alphabet.find(digits)+len(digits):]
    
    
    def setGenType(self, newType: str='secure') -> None:
            self.genType = newType
    
    def writeHistory(self, option: bool=True) -> None:
        self.history = option
    

    def getHistory(self) -> str:
        return '\n'.join([self.passwordHistory[i] + '\t' + self.time[i] for i in range(len(self.passwordHistory))])
    

    def useClipboard(self, option: bool=True) -> None:
        self.clipboard = option


def main() -> None:
    OBJ = Menu()
    OBJ.runProgram()


if __name__=='__main__':
    main()