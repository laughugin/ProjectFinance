import random

global Time
Time = 0


class Line():
    A_y = 0
    B_y = 0

    def save(self):
        GraphData = open('ProjectFinance\Data\GraphData.txt','r')
        temp = GraphData.read()
        Data = temp.split('/')
        GraphData = open('ProjectFinance\Data\GraphData.txt','w')
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
        GraphData.write(temp)
        GraphData.close()
    
    def load(self, time_x):
        GraphData = open('ProjectFinance\Data\GraphData.txt','r')
        temp = GraphData.read()
        Data = temp.split('/')
        self.A_y = int(Data[2*time_x])
        self.B_y = int(Data[2*time_x + 1])
        GraphData.close()
        return self


    
class ProcessData():
    GraphChange = Line()


def MainProcess():
    DirectionData = open('ProjectFinance\Data\GraphDirectionData.txt', 'r')
    temp = DirectionData.read()
    Direction = temp.split('/')
    StepsToNextPoint = int(Direction[0])
    NextPoint_y = int(Direction[1])
    LastLine = Line()
    LastLine = LastLine.load(19)
    if int(Direction[0]) == 0:
        MaxChange = int(LastLine.B_y/100*20)
        NextPoint_y = LastLine.B_y + random.randrange(-MaxChange, MaxChange)
        StepsToNextPoint = random.randrange(1, 4)
    NextLine = Line()
    NextLine.A_y = LastLine.B_y
    NextLine.B_y = LastLine.B_y + int((NextPoint_y - LastLine.B_y)/StepsToNextPoint)
    NextLine.save()
    DirectionData = open('ProjectFinance\Data\GraphDirectionData.txt', 'w')
    temp = str(StepsToNextPoint - 1) + '/' + str(NextPoint_y) + '/'
    DirectionData.write(temp)
    DirectionData.close()



    

