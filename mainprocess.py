import random

class Point():
    x = 0
    y = 0

class Line():
    A = Point()
    B = Point()
    
class ProcessData():
    GraphChange = Line()


def MainProcess():
    Data = ProcessData()
    Data.GraphChange.A.x = i