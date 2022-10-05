
import tkinter as tk

class Window(tk.Tk):  
      

    

    def __init__(self):
        super().__init__()

        self.Label = tk.Label(self, text='F.I.N.A.N.C.E.', bg='grey23', font=("Helvetica",36,"bold"))
        self.button0 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button1 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button2 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button3 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button4 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')

        #configuration
        self.title("Finance Pro")
        self.iconbitmap(r"ProjectFinance\pics\taskbaricon.ico")
        self.geometry('1000x700')
        self.configure(bg='grey23')

        self.Label.pack(pady=100)

        self.button0.config(state='active', command=self.Start, text='Start')
        self.button1.config(state='active', command=self.Settings, text='Settings')
        self.button2.config(state='active', command=self.Exit, text='Exit')

        self.button0.pack(pady=25)
        self.button1.pack(pady=10)
        self.button2.pack(pady=10)
        self.button3.pack(pady=10)
        self.button4.pack(pady=10)

        

    def Start(self):
        self.Image = tk.PhotoImage(file=r"ProjectFinance\pics\Soon.png")
        self.Label.config(image=self.Image)
    
    def Settings(self):
        return 0




    def Back(self):
        return 0

    def Exit(self):
        self.quit()




    




    