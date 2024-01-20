import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from database_driver import read_txt

#################################################################
class Display():  
    def __init__(self):
        self.title = "Auto Bot"
        self.screen = Tk()
        self.screen.title(self.title)
        self.screen.configure(bg="#222")
        self.screen.geometry("700x250")

    def Notify(self, tit, mess):
        messagebox.showinfo(tit, mess)

    def Find_File(self, types):
        Tk().withdraw() 
        file_name = askopenfilename()

        if types == "com": 
            self.textcom.delete(1.0, END)
            self.textcom.insert(INSERT, file_name)
            self.filecom = read_txt(file_name)

        elif types == "link": 
            self.textlink.delete(1.0, END)
            self.textlink.insert(INSERT, file_name)
            self.filelink = read_txt(file_name)

        elif types == "acc": 
            self.textacc.delete(1.0, END)
            self.textacc.insert(INSERT, file_name)
            self.fileacc = read_txt(file_name)

    def Show_Output(self, ouput):
        output_window = tk.Toplevel()
        label = tk.Label(output_window, text=ouput)
        label.pack()

    def Create_Label(self, text, xy):
        var = Label(self.screen, text = text, fg="#fff", bg="#222")
        var.place(x = xy[0], y = xy[1])
        return var

    def Create_Entry(self, width, xy):
        var = Entry(width = width, font = ("Times New Roman",16))
        var.place(x = xy[0], y = xy[1])
        return var

    def Create_Button(self, text, command, wh, xy):
        var = Button(text = text, width = wh[0], height = wh[1], command = command)
        var.place(x = xy[0], y = xy[1])
        return var

    def Create_TextBox(self, wh, xy):
        var = Text(self.screen, width = wh[0], height = wh[1], font=("Times New Roman",16))
        var.place(x = xy[0], y = xy[1])
        return var