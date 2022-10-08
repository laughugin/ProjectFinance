# drawing a bar graph with the Tkinter canvas and
# canvas.create_rectangle(x0, y0, x1, y1, option, ...)
# note: coordinates are relative to the top left corner of the canvas
# used a more modern import to give Tkinter items a namespace
# tested with Python24  by    vegaseat    01nov2006

import tkinter as tk  # gives tk namespace
import random 

data = [30,20,15,23,26,12,42,21,13,32,18,21,34,43,23,14,32,33,31,32,36,30,20,15,23,26,12,42,
21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,26,21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,26,21,13,32,18,21,34
,21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,26,21,13,32,18,21,21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,26,21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,2621,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,26,34,43,23,14,32,33,31,32,30,20,15,23,26,21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,2643,23,14,32,33,31,32,30,20,15,23,26,21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,26,12,42,21,13,32,18,21,34,43,23,14,32,33,31,32,30,20,15,23,26,12,42,21,13,32,18,21,34,43,23,14,32,33,31,32,36]

root = tk.Tk()
root.geometry("1300x500")
root.configure(bg='blue')
root.title("Finance Graph")
c_width = 1300
c_height = 500
c = tk.Canvas(root, width=c_width, height=c_height, bg= 'black')
BG = tk.PhotoImage(file=r'ProjectFinance\pics\BG.png')

c.pack(fill='both', expand = True)
c.create_image(0, 0, image=BG, anchor='nw')
# the variables below size the bar graph
# experiment with them to fit your needs
# highest y = max_data_value * y_stretch
y_stretch = 5
# gap between lower canvas edge and x axis
y_gap = 0
# stretch enough to get all data items in
x_stretch = 3
x_width = 3
# gap between left canvas edge and y axis
x_gap = 5

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
        if temp < c_height -  (y * y_stretch + y_gap):
            y0 = c_height -  (y * y_stretch + y_gap)
            y1 = temp1
        else:
            y1 =  c_height -  (y * y_stretch + y_gap)
            y0 = temp

    print(x0, y0, x1, y1)
    # draw the bar
    if y1 < temp1:
        c.create_rectangle(x0, y0, x1, y1, fill="green")
    else:
        c.create_rectangle(x0, y0, x1, y1, fill="red")
    temp = y1
    temp1 = y0
    
    # put the y value above each bar
    c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))

root.mainloop()
