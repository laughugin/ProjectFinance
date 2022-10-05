from tkinter import *

#class MainWindow:
    

def WindowStart():
    window = Tk()

    window.title("Finance Pro")
    window.iconbitmap(r"ProjectFinance\pics\taskbaricon.ico")
    window.configure(width = window.winfo_screenwidth()-10, height = window.winfo_screenheight()-80)
    window.configure(bg='black')

    # move window center
    winWidth = window.winfo_reqwidth()
    winwHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2 - 10)
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2 - 40)
    window.geometry("+{}+{}".format(posRight, posDown))

    window.mainloop()


    