import numpy as np
#(((x,y), (connections)),((x,y), (connections)))
class obj():
    def __init__(self, array, pos = np.array([0,0])) -> None:
        self.array = array
        self.pos = pos
    def Loadobj(self, dir):
        data = np.load(dir)
        return obj(data)
    def Saveobj(self, dir) -> None:
        np.save(dir, self.array)