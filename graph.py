# drawing a bar graph with the Tkinter canvas and
# canvas.create_rectangle(x0, y0, x1, y1, option, ...)
# note: coordinates are relative to the top left corner of the canvas
# used a more modern import to give Tkinter items a namespace
# tested with Python24  by    vegaseat    01nov2006

from re import L
import tkinter as tk  # gives tk namespace
import random
import mainprocess

data = []

class GraphRec():
    Y0 = 0
    Y1 = 1
    X0 = 0
    X1 = 1
    Color = 'green'


def GraphCalc():
    OutputData = []
    tempOutput = GraphRec()

    data.clear()
    OutputData.clear()
    

    # for x in range(300):
    #     if x < 100:
    #         data.append(random.randint(-20,50))
    #     elif x >= 100 and x <= 200:
    #         data.append(random.randint(0,60))
    #     else: 
    #         data.append(random.randint(20,75))

    tempload = mainprocess.Line()

    for i in range(80):
        tempload = tempload.load(i)
        data.append(tempload.y)

    summa = 0
    for i in range(70, 80):
        summa += data[i]
    yGap = summa//10

    for i in range(80):
        data[i] -= yGap


    # root = tk.Tk()
    # root.geometry("1300x500")
    # root.configure(bg='blue')
    # root.title("Finance Graph")
    # c_width = 1300
    c_height = 500
    # c = tk.Canvas(root, width=c_width, height=c_height, bg= 'grey23')
    # #BG = tk.PhotoImage(file=r'ProjectFinance\pics\BG.png')

    # c.pack(fill='both', expand = True)
    #c.create_image(0, 0, image=BG, anchor='nw')
    # the variables below size the bar graph
    # experiment with them to fit your needs
    # highest y = max_data_value * y_stretch
    y_stretch = 5
    # gap between lower canvas edge and x axis
    y_gap = 0 
    # stretch enough to get all data items in
    x_stretch = 3
    x_width = 10
    # gap between left canvas edge and y axis
    x_gap = 10

    temp = 0
    temp1 = 0

    for x, y in enumerate(data):
        # calculate reactangle coordinates (integers) for each bar
        x0 = x * x_stretch + x * x_width + x_gap
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1=  c_height -  (y * y_stretch + y_gap)
        if x == 0:
           y0= c_height -  (y * y_stretch + y_gap)
        else:
            if c_height -  (y * y_stretch + y_gap) < temp1 and c_height -  (y * y_stretch + y_gap) < temp:
                y0 = c_height -  (y * y_stretch + y_gap)
                y1 = temp1
            elif c_height -  (y * y_stretch + y_gap) > temp1 and c_height -  (y * y_stretch + y_gap) < temp and data[x - 1] > data[x]:
                y0 = temp1
                y1 = c_height -  (y * y_stretch + y_gap)
            elif c_height -  (y * y_stretch + y_gap) > temp1 and c_height -  (y * y_stretch + y_gap) < temp and data[x - 1] < data[x]:
                y0 = c_height -  (y * y_stretch + y_gap)
                y1 = temp
            elif c_height -  (y * y_stretch + y_gap) > temp1 and c_height -  (y * y_stretch + y_gap) > temp:
                y0 = temp
                y1 = c_height -  (y * y_stretch + y_gap)

        # draw the bar
        tempOutput = GraphRec()
        tempOutput.X0 = x0
        tempOutput.Y0 = y0
        tempOutput.X1 = x1
        tempOutput.Y1 = y1
        if data[x - 1] < data[x]:
            tempOutput.Color = 'green'
            #c.create_rectangle(x0, y0, x1, y1, fill="green")

        elif data[x - 1] > data[x]:
            tempOutput.Color = 'red'
            #c.create_rectangle(x0, y0, x1, y1, fill="red")
        OutputData.append(tempOutput)
        temp = y1
        temp1 = y0

        # put the y value above each bar
        #c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))
    

    return OutputData
    #root.mainloop()
