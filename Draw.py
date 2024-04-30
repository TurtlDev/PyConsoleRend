import numpy as np

def DrawObject(obj, canvas, color):
    for i in obj.array:
        pos1 = np.array(i[0])
        for y in i[1]:
            pos2 = np.array(obj.array[y][0])
            pointer = np.array([float(pos1[0]), float(pos1[1])])
            dir = np.array(pos2-pos1)
            temp = (dir[0]**2+dir[1]**2)**.5
            dir = (dir/temp)
            dist = 10
            while dist>1:
                pointer += dir
                canvas.setcord(round(pointer[0]),round(pointer[1]),color)
                dist = (pointer-pos2)
                dist = (dist[0]**2+dist[1]**2)**.5