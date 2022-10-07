import random

global Time
Time = 0


class Line():
    A_y = 0
    B_y = 0

    def save(self):
        file = open('ProjectFinance\Data\MainData.txt','r')
        temp = file.read()
        Data = temp.split('/')
        file = open('ProjectFinance\Data\MainData.txt','w')
        for i in range(0, 19):
            Data[i*2] = Data[(i+1)*2]
            Data[i*2 + 1] = Data[(i+1)*2 + 1]
        Data[38] = str(self.A_y)
        Data[39] = str(self.B_y)
        temp = Data[0] + '/'
        for i in range(0,20):
            if i != 0:
                temp += Data[i*2] + '/'
            temp += Data[i*2 + 1] + '/'
        file.write(temp)
        file.close()
    
    def load(self, time_x):
        file = open('ProjectFinance\Data\MainData.txt','r')
        temp = file.read()
        Data = temp.split('/')
        self.A_y = int(Data[2*time_x])
        self.B_y = int(Data[2*time_x + 1])
        file.close()
        return self


    
class ProcessData():
    GraphChange = Line()


def MainProcess():
    Data = Line()
    Data = Data.load(19)
    temp = Data.A_y
    Data.A_y += random.randrange(-10, 10)
    Data.B_y = temp
    Data.save()
    

