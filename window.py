
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from turtle import position

class Window(tk.Tk):    

    def __init__(self):
        super().__init__()

        #configuration
        self.title("Finance Pro")
        self.iconbitmap(r"ProjectFinance\pics\taskbaricon.ico")
        self.geometry('200x200')
        self.configure(bg='black')

        # move self center
        winWidth = self.winfo_reqwidth()
        winwHeight = self.winfo_reqheight()
        posRight = int(self.winfo_screenwidth() / 2 - winWidth / 2 - 10)
        posDown = int(self.winfo_screenheight() / 2 - winwHeight / 2 - 40)
        self.geometry("+{}+{}".format(posRight, posDown))

        self.button = ttk.Button(self, text='Press me', height=5, weight=30)
        self.button['command'] = self.button_clicked
        self.button
        self.button.pack()

    def button_clicked(self):
        showinfo(title = 'Test completed', message='You are gay')




    




    