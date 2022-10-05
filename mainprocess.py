from tkinter import *

#class MainWindow:
    

def WindowStart():
    window = Tk()

    window.title("Python GUI App")
    window.configure(width=500, height=300)
    window.configure(bg='darkgrey')

    # move window center
    winWidth = window.winfo_reqwidth()
    winwHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))

    window.mainloop()


    