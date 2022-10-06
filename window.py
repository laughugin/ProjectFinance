from turtle import back
import mainprocess
import tkinter as tk

class Window(tk.Tk):  
    
    
    global complexity
    complexity = 1

    def __init__(self):
        super().__init__()

        global complexity

        Data = open('ProjectFinance\Data\Settings.txt', 'r')
        complexity = int(Data.read())
        Data.close()
        
        self.canvasBG = tk.Canvas(self, width = 400, height=780, bd=0, relief='flat')
        self.button0 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button1 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button2 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button3 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        self.button4 = tk.Button(self, state='disabled', activebackground='grey23', activeforeground='white', fg='white', bd=0, text=None, command=None, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')

        global MainMenu
        def MainMenu():
            self.button0.config(state='active', command=self.Start, text='Start')
            self.button1.config(state='active', command=self.Settings, text='Settings')
            self.button2.config(state='active', command=self.Exit, text='Exit')
            self.button3.config(state='disabled', command=None, text='')
            self.button4.config(state='disabled', command=None, text='')

        #configuration
        self.title("Finance Pro")
        self.iconbitmap(r"ProjectFinance\pics\taskbaricon.ico")
        self.BG = tk.PhotoImage(file=r'ProjectFinance\pics\BG.png')
        self.geometry('1520x780+0+0')
        self.resizable(width=False, height=False)
        self.configure(bg='grey23')

        self.canvasBG.pack(fill='both', expand = True)
        self.canvasBG.create_image(0, 0, image=self.BG, anchor='nw')
        self.canvasBG.create_text(760, 100, text='F.I.N.A.N.C.E.', font=("Console",36,"bold"))
        
        self.button0_canvas = self.canvasBG.create_window(760, 300, window=self.button0)
        self.button1_canvas = self.canvasBG.create_window(760, 350, window=self.button1)
        self.button2_canvas = self.canvasBG.create_window(760, 400, window=self.button2)
        self.button3_canvas = self.canvasBG.create_window(760, 450, window=self.button3)
        self.button4_canvas = self.canvasBG.create_window(760, 500, window=self.button4)


        MainMenu()


    

    def Start(self):
        # self.Image = tk.PhotoImage(file=r"ProjectFinance\pics\Soon.png")
        # self.Label.config(image=self.Image)
        self.button0.config(state='active', command=mainprocess.MainProcess, text='Google')
        self.button1.config(state='disabled', command=None, text='Coming soon!')
        self.button2.config(state='disabled', command=None, text='')
        self.button4.config(state='active', command=self.Back, text='Back')

    
    

    def Settings(self):
        self.button1.config(state='disabled', command=None, text='')
        self.button2.config(state='active', command=self.Back, text='Back')
        self.button0.config(state='active', command=self.ChangeComplexity)
        if complexity == 0:
            self.button0.config(text='Easy')
        elif complexity == 1:                   
            self.button0.config(text='Medium')
        else:                                    
            self.button0.config(text='Hard')
            
    def ChangeComplexity(self):
        global complexity
        if complexity < 2:
            complexity += 1
        else:
            complexity = 0

        if complexity == 0:
            self.button0.config(text='Easy')
        elif complexity == 1:                   
            self.button0.config(text='Medium')
        else:                                    
            self.button0.config(text='Hard')

    def Back(self):
        MainMenu()

    def Exit(self):

        global complexity

        Data = open('ProjectFinance\Data\Settings.txt', 'w')
        Data.write(str(complexity))
        Data.close()

        self.quit()




    




    