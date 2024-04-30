import numpy as np

def DrawObject(obj, canvas):
    for i in obj.array:
        for y in i[1]:
            pointer = np.array((i[0][0]+obj.pos[0],i[0][1]+obj.pos[1]))
            dir = (np.linalg.norm(np.array((i[0][0]+obj.array[y][0][0],i[0][1]+obj.array[y][0][1]))))/((((i[0][0]-obj.array[y][0][0])**2)+((i[0][1]-obj.array[y][0][1])**2))**.5)
            