from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5

from tkinter import Tk, Entry, Button, END, Label, Toplevel, filedialog as fd
from tkinter.messagebox import showinfo

from base64 import b64encode, b64decode
import rsa


class Encryptor:
    def __init__(self, keyLength=1024) -> None:
        self.keyLength = keyLength


    def importKey(externKey):
        return RSA.importKey(externKey)


    def getpublickey(priv_key):
        return priv_key.publickey()


    def encrypt(message, pub_key):
        cipher = PKCS1_OAEP.new(pub_key)
        return cipher.encrypt(message)


    def sign(message, priv_key):
        signer = PKCS1_v1_5.new(priv_key)
        digest = MD5.new()
        digest.update(message)
        return signer.sign(digest)


    def decrypt(ciphertext, priv_key):
        cipher = PKCS1_OAEP.new(priv_key)
        return cipher.decrypt(ciphertext)


    def verify(message, signature, pub_key):
        signer = PKCS1_v1_5.new(pub_key)
        digest = MD5.new()
        digest.update(message)
        return signer.verify(digest, signature)


    def generateKey(self, keys: tuple, messageFilename: str, signatureFilename: str) -> str:
        with open(messageFilename, "r") as f:
            msg = f.read()
        
        msg = msg.encode('utf-8')
        (publicKey, privateKey) = keys
        self.encrypted = b64encode(rsa.encrypt(msg, publicKey))

        with open("input.txt", "w") as f:
            f.write(self.encrypted.decode('ascii'))

        self.signature = b64encode(rsa.sign(msg, privateKey, "MD5"))
        
        with open(signatureFilename, "wb") as f:
            f.write(self.signature)

        return "Файл успішно підписано!"


    def checkKey(self, keys, messageFilename: str, signatureFilename: str) -> str:
        publicKey, privateKey = keys

        with open(messageFilename, "r") as f:
            msg = f.read()
        
        msg = msg.encode('utf-8')
        self.decrypted = rsa.decrypt(b64decode(msg), privateKey)

        with open(signatureFilename, "rb") as f:
            signature = f.read()
        
        self.verified = rsa.verify(self.decrypted, b64decode(signature), publicKey)

        with open(messageFilename, "w") as f:
            f.write(self.decrypted.decode('ascii'))

        return "Підпис успішно верифіковано!"



class Menu:
    def __init__(self) -> None:
        self.keySize = 1024
        (self.publicKey, self.privateKey) = rsa.newkeys(self.keySize)
        self.OBJ = Encryptor(self.keySize)

        self.drawWindow()
        self.loadButtons()
        
    
    def encrypt(self) -> None:
        self.OBJ.generateKey((self.publicKey, self.privateKey), self.messageFilename, self.signatureFilename)
        self.openNewWindow("Підпис створено та накладено на документ.", self.OBJ.encrypted, self.OBJ.signature)
    

    def decrypt(self) -> None:        
        try:
            self.OBJ.checkKey((self.publicKey, self.privateKey), self.messageFilename, self.signatureFilename)
            self.openNewWindow("Підпис верифіковано, повідомлення розшифроване.", self.OBJ.decrypted, self.OBJ.verified)
        except:
            rsa.VerificationError("Перевірка підпису невдала! ЕЦП не верифіковано.")
    

    def drawWindow(self) -> None:
        self.root = Tk('Tk')
        self.root.title('ЕЦП')
        self.root.resizable(False, False)
        self.root.geometry('300x150')

    
    def loadButtons(self) -> None:
        self.openSignButton = Button(
            self.root,
            text='Відкрити файл з повідомленням',
            command=self.selectMsg
        )
        
        self.openMsgButton = Button(
            self.root,
            text='Відкрити файл з підписом',
            command=self.selectSign
        )

        self.encrpyptSignButton = Button(self.root, text='Підписати файл', command=self.encrypt)
        self.decrpyptSignButton = Button(self.root, text='Верифікувати файл', command=self.decrypt)

        self.decrpyptSignButton.pack(expand = True)
        self.encrpyptSignButton.pack(expand = True)
        self.openMsgButton.pack(expand = True)
        self.openSignButton.pack(expand = True)


    def selectMsg(self) -> None:
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))

        self.messageFilename = fd.askopenfilename(
            title='Відкрити файл з повідомленням',
            initialdir='/',
            filetypes=filetypes)

        showinfo(title='Вибрано файл.', message=self.messageFilename)
    

    def selectSign(self) -> None:
        filetypes = (('key files', '*.key'), ('All files', '*.*'))

        self.signatureFilename = fd.askopenfilename(
            title='Відкрити підпис',
            initialdir='/',
            filetypes=filetypes)

        showinfo(title='Відкрито підпис', message=self.signatureFilename)
    

    def openNewWindow(self, option: str, msg1: str, msg2:str) -> None:
        self.newWindow = Toplevel(self.root)
        self.newWindow.title(option)
        self.newWindow.geometry("500x250")

        Label(self.newWindow, text="Текст повідомлення: ").pack(padx=10)
        textbox1 = Entry(self.newWindow, bg="white", width=100, borderwidth=2)
        textbox1.insert(0, msg1)
        textbox1.pack(pady=20)

        Label(self.newWindow, text="Підпис: ").pack(padx=10)
        textbox2 = Entry(self.newWindow, bg="white", width=100, borderwidth=2)
        textbox2.insert(0, msg2)
        textbox2.pack(pady=20)
   
    
def main() -> None:
    MENU = Menu()
    MENU.root.mainloop()
    exit()


if __name__ == "__main__":
    main()