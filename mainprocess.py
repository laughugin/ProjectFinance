import random
import tkinter
import tkinter.messagebox as huila

class Point():
    x = 0
    y = 0

class Line():
    y = 0

    def save(self):
        GraphData = open('ProjectFinance\Data\GraphData.txt','r')
        temp = GraphData.read()
        Data = temp.split('/')
        GraphData = open('ProjectFinance\Data\GraphData.txt','w')
        for i in range(0, 79):
            Data[i] = Data[i+1]
        Data[79] = str(self.y)
        temp = Data[0] + '/'
        for i in range(1,80):
            temp += Data[i] + '/'
        GraphData.write(temp)
        GraphData.close()
    
    def load(self, time_x):
        GraphData = open('ProjectFinance\Data\GraphData.txt','r')
        temp = GraphData.read()
        Data = temp.split('/')
        self.y = int(Data[time_x])
        GraphData.close()
        return self


    
class AccountData():
    Money = 0
    Share = 0

    def load(self):
        Data = open('ProjectFinance\Data\AccountData.txt', 'r')
        temp = Data.read()
        inpt = temp.split('/')
        self.Money = int(inpt[0])
        self.Share = int(inpt[1])
        Data.close()

    def save(self):
        Data = open('ProjectFinance\Data\AccountData.txt', 'w')
        temp = str(self.Money) + '/' + str(self.Share) + '/'
        Data.write(temp)
        Data.close()

    
        


def MainProcess():
    DirectionData = open('ProjectFinance\Data\GraphDirectionData.txt', 'r')
    temp = DirectionData.read()
    Direction = temp.split('/')
    StepsToNextPoint = int(Direction[0])
    NextPoint_y = int(Direction[1])
    LastLine = Line()
    LastLine = LastLine.load(79)
    if int(Direction[0]) == 0:
        NextPoint_y = LastLine.y + random.randrange(-30, 30)
        if NextPoint_y < 30:
            NextPoint_y = LastLine.y + random.randrange(30, 40)
        StepsToNextPoint = random.randrange(1, 4)
    NextLine = Line()
    NextLine.y = LastLine.y
    NextLine.y = LastLine.y + int((NextPoint_y - LastLine.y)/StepsToNextPoint)
    NextLine.save()
    DirectionData = open('ProjectFinance\Data\GraphDirectionData.txt', 'w')
    temp = str(StepsToNextPoint - 1) + '/' + str(NextPoint_y) + '/'
    DirectionData.write(temp)
    DirectionData.close()

def CurrentExchange():
    GraphData = open('ProjectFinance\Data\GraphData.txt', 'r')
    temp = GraphData.read()
    Data = temp.split('/')
    return int(Data[79])


def Buy(Amount):
    Account = AccountData()
    Account.load()
    GraphData = open('ProjectFinance\Data\GraphData.txt', 'r')
    temp = GraphData.read()
    Data = temp.split('/')
    ChangeRate = int(Data[79])
    Price = ChangeRate * int(Amount)
    if Price > Account.Money:
        huila.showerror(title="Not enough money", message="Not enough money")
    else:
        Account.Money -= Price
        Account.Share += int(Amount)
        Account.save()
        GraphData.close()
    

def Sell(Amount):
    Account = AccountData()
    Account.load()
    GraphData = open('ProjectFinance\Data\GraphData.txt', 'r')
    temp = GraphData.read()
    Data = temp.split('/')
    ChangeRate = int(Data[79])
    Price = ChangeRate * int(Amount)
    if int(Amount) > Account.Share:
        huila.showerror(title="Not enough share", message="Not enough share")
    else:
        Account.Money += Price
        Account.Share -= int(Amount)
        Account.save()
        GraphData.close()
