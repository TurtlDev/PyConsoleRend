import numpy as np
import time
#(((x,y), (connections)),((x,y), (connections)))
class obj():
    def __init__(self, array, pos = np.array([0,0])) -> None:
        self.array = array
        self.pos = pos
    def Saveobj(self, dir) -> None:
        np.save(dir, self.array)
    def Draw(self, canvas, color = (0,0,0)):
        DrawObject(self, canvas, color)

def DrawObject(obj, canvas, color):
    
    for i in obj.array:
        pos1 = np.array(i[0]) + obj.pos
        for y in i[1]:
            pos2 = np.array(obj.array[y][0]) + obj.pos
            pointer = pos1.astype(float).copy()
            dir = np.array(pos2-pos1)
            dir = dir/np.linalg.norm(dir)
            dist = 10
            while dist>=1:
                canvas.setcord(round(pointer[0]),round(pointer[1]),color)
                pointer += dir
                dist = np.linalg.norm(pointer - pos2)
def Loadobj(dir):
    data = np.load(dir)
    return obj(data)