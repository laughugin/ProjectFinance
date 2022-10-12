import mainprocess
import graph
import tkinter as tk
import time

class Window(tk.Tk):  
    
    
    global complexity
    complexity = 1

    global Pause
    Pause = 0

    global Speed
    Speed = 1

    global amount
    amount  = '100'

    global Rate
    Rate = 0

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
            #configuring buttons
            self.button0.configure(state='active', command=self.Start, text='Start')
            self.button1.configure(state='active', command=self.Settings, text='Settings')
            self.button2.configure(state='active', command=self.Exit, text='Exit')
            self.button3.configure(state='disabled', command=None, text='')
            self.button4.configure(state='disabled', command=None, text='')

            #moving buttons to center
            self.button0.place(x = 760, y = 300, anchor='center')
            self.button1.place(x = 760, y = 400, anchor='center')
            self.button2.place(x = 760, y = 500, anchor='center')
            self.button3.place(x = 760, y = 600, anchor='center')
            self.button4.place(x = 760, y = 700, anchor='center')

        #configuration of window
        self.title("Finance Pro")
        self.iconbitmap(r"ProjectFinance\pics\taskbaricon.ico")
        self.BG = tk.PhotoImage(file=r'ProjectFinance\pics\BG.png')
        self.geometry('1520x780+0+0')
        self.resizable(width=False, height=False)

        #creating canvas where all items is
        self.canvasBG.pack(fill='both', expand = True)
        self.canvasBG.create_image(0, 0, image=self.BG, anchor='nw') #setteing up background
        global LabelAtTop
        LabelAtTop = self.canvasBG.create_text(760, 100, text='F.I.N.A.N.C.E.', font=("Console",36,"bold")) 
        
        #creating buttons
        self.canvasBG.create_window(760, 300, window=self.button0)
        self.canvasBG.create_window(760, 400, window=self.button1)
        self.canvasBG.create_window(760, 500, window=self.button2)
        self.canvasBG.create_window(760, 600, window=self.button3)
        self.canvasBG.create_window(760, 700, window=self.button4)

        #New variable to store 
        global rec
        rec = []
        for i in range(80):
            rec.append(self.canvasBG.create_rectangle(0, 0, 0, 0, fill = None))

        MainMenu()


    

    def Start(self):
        self.button0.configure(state='active', command=self.Google, text='Google')
        self.button2.configure(state='disabled', command=None, text='Coming soon!')
        self.button1.configure(state='disabled', command=self.AskBuy, text=None)
        self.button3.configure(state='disabled', command=self.AskSell, text=None)
        self.button4.configure(state='active', command=self.Back, text='Back')

    def Google(self):
        global Speed
        self.button0.configure(state='active', command=self.pause, text='Step')
        self.button2.configure(state='active', command=self.AskBuy, text='Buy Share')
        self.button1.configure(state='active', command=self.AskSell, text= 'Sell Share')
        self.button3.configure(state='active', command=self.ChangeSpeed, text='Speed: ' + str(1//Speed))
        self.button4.configure(state='active', command=self.Back, text='Main Menu')
        self.button0.place(x = 1300, y = 300, anchor='nw')
        self.button1.place(x = 1300, y = 400, anchor='nw')
        self.button2.place(x = 1300, y = 500, anchor='nw')
        self.button3.place(x = 1300, y = 600, anchor='nw')
        self.button4.place(x = 1300, y = 700, anchor='nw')
        self.loop()
            
        

    def pause(self):
        global Pause
        Pause = not Pause

    def ChangeSpeed(self):
        global Speed
        if Speed == 1:
            Speed = 2
        elif Speed == 2:
            Speed = 0.1
        elif Speed == 0.1:
            Speed = 0.5
        elif Speed == 0.5:
            Speed = 1

    def loop(self):
        global Speed
        global Pause
        global Rate
        self.button3.configure(state='active', command=self.ChangeSpeed, text='Speed: ' + str(100//Speed))
        if not Pause:
            global rec
            mainprocess.MainProcess()
            for i in range(80):
                self.canvasBG.delete(rec[i])
            self.canvasBG.delete(Rate)
            rec = []
            GraphData = graph.GraphCalc()
            Account = mainprocess.AccountData()
            Account.load()
            global LabelAtTop
            self.canvasBG.itemconfig(LabelAtTop, text = str(Account.Money) + '$     Share avaliable: ' + str(Account.Share), font=("Console",24,"bold"), fill = 'white')
            for i in range(80):
                rec.append(self.canvasBG.create_rectangle(GraphData[i].X0, GraphData[i].Y0, GraphData[i].X1, GraphData[i].Y1, fill=GraphData[i].Color))
                if i == 79:
                    Rate = self.canvasBG.create_text(GraphData[i].X0 + 15, GraphData[i].Y0, anchor=tk.SW, text=str(mainprocess.CurrentExchange()), fill = 'white', font=("Console",24,"bold"))
        self.after(int(Speed*1000), self.loop)

    def AskBuy(self):
        self.AskAmount(1)
        Account = mainprocess.AccountData()
        Account.load()
        global LabelAtTop
        self.canvasBG.itemconfig(LabelAtTop, text = str(Account.Money) + '$     Share avaliable: ' + str(Account.Share))
        
        
    def AskSell(self):
        self.AskAmount(0)
        Account = mainprocess.AccountData()
        Account.load()
        global LabelAtTop
        self.canvasBG.itemconfig(LabelAtTop, text = str(Account.Money) + '$     Share avaliable: ' + str(Account.Share))


    def AskAmount(self, BuyOrSell):   # True if buy, False if sell

        AmountWindow = tk.Tk()

        #Setting up the window
        AmountWindow.geometry('150x100+770+390') #Size and position: "(Size_X)x(Size_Y)+(Pos_X)+(Pos_Y)"
        #AmountWindow.resizable(width=False, height=False)
        AmountWindow.configure(bg='grey23')

        def GetNumber():   #function that read number when button is pressed
            global amount
            amount = int(NumberInput.get(1.0, "end-1c") or '100')  #Reads text data or if it's empty returns '100'

            AmountWindow.destroy()  #closes window

            if BuyOrSell:
                mainprocess.Buy(amount)  #calls buy function
            else:
                mainprocess.Sell(amount) #calls sell function
        
        #Text
        TextLabel = tk.Label(AmountWindow, text='Enter requested amount:', fg='white', bg='grey33')
        TextLabel.pack()

        #Input field
        NumberInput = tk.Text(AmountWindow, height = 2, width = 10, bg='grey23')
        NumberInput.pack()

        #Button OK
        button0 = tk.Button(AmountWindow, state='active', activebackground='grey23', activeforeground='white', fg='white', bd=0, text='OK', command=GetNumber, font=("Helvetica",20,"bold"), bg='grey23', relief='flat')
        button0.pack()
        
        AmountWindow.mainloop()   #Starting window
        

        
            
        


    def Settings(self):
        self.button1.configure(state='disabled', command=None, text='')
        self.button2.configure(state='active', command=self.Back, text='Back')
        self.button0.configure(state='active', command=self.ChangeComplexity)
        if complexity == 0:
            self.button0.configure(text='Easy')
        elif complexity == 1:                   
            self.button0.configure(text='Medium')
        else:                                    
            self.button0.configure(text='Hard')
            
    def ChangeComplexity(self):
        global complexity
        if complexity < 2:
            complexity += 1
        else:
            complexity = 0

        if complexity == 0:
            self.button0.configure(text='Easy')
        elif complexity == 1:                   
            self.button0.configure(text='Medium')
        else:                                    
            self.button0.configure(text='Hard')

    def Back(self):
        MainMenu()

    def Exit(self):

        global complexity

        Data = open('ProjectFinance\Data\Settings.txt', 'w')
        Data.write(str(complexity))
        Data.close()

        self.quit()





    




    