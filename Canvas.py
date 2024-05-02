import itertools
import numpy
import time

from typing import Literal

#add ascii support (text/characters in image)
class canvas:
    exsist = False
    def __new__(cls,*args,**kwargs):
        if canvas.exsist:
            raise SystemError(
                "\x1b[38;2;255;0;0mmultiple instances of canvas cannot exsist"
                )
        canvas.exsist = True
        return super().__new__(cls)
    def __init__(self,dims: tuple[int,int]):
        self.width = dims[0]
        self.height = dims[1]
        self.dims = dims
        #constants
        self.END ='\x1b[F'*(self.width*self.height)+'\x1b[0' 
        self.BOTH = {"Both", "both", "B", "b"}    #We want to do C++ right?
        self.RIGHTLEFT = {"Right":1,"right":1,"R":1,"r":1,
                          "Left":0,"left":0,"L":0,"l":0}#cant believe bro hard coded this shit
                                                        # T-T
        #-----------------------------
        self.grid = [[[0,0] for x in range(dims[0])] for y in range(dims[1])]
        #time complexity:
        #o(dims[0]*dims[1])
        #-----------------------------
    def __getitem__(self,y:int):
        print(y)
        return self.grid[y]

    def __setitem__(self,y,x=0):
        print("dont.")

    def __call__(self,**cnf):
        """config:
        """
        


    def setcord(self,x,y,color: tuple[int, int, int] | int, 
                side: Literal["Left","left","L","l",
                "Right","right","R","r", "Both", "both", "B", "b"] = "b"):
                #instead of using try except IndexError
            if x >= self.width or y >= self.height:
                return
            if isinstance(color,tuple):
                          color = 16+int((color[0]/255*36)+(color[1]/255*6)+b/255)
            if side in self.BOTH:
                self.grid[y][x][0] = self.grid[y][x][1] = color                                     
                return
            self.grid[y][x][self.RIGHTLEFT[side]] = color                             

    #optimize checkerboard func
    def checkerboard(self,colorA: tuple[int, int, int] | int = 0, 
                     colorB: tuple[int, int, int] | int = 0 ,*, size: Literal["big","little"] = "big"):
        if size == "big":
            for y in range(self.height):
                for x in range(self.width):
                    if x % 2 == 0:
                        if y % 2 == 0:
                            self.setcord(x,y,colorA)
                            continue
                        self.setcord(x,y,colorB)
                        continue
                    elif y % 2 == 0:
                            self.setcord(x,y,colorB)
                            continue
                    self.setcord(x,y,colorA)
        else:
            for y in range(self.height):
                for x in range(self.width):
                    try:
                        if y % 2 == 0:
                            self.setcord(x,y,colorA,"l")
                            self.setcord(x,y,colorB,"r")
                        else:
                            self.setcord(x,y,colorA,"r")
                            self.setcord(x,y,colorB,"l")
                    except IndexError:
                        pass
                        
    #optimize render func
    #its really slow
    def render(self):    
        #removed other methods of rendering (rgb will now be converted to a valid color)
         #may be able to have this as empty str
        screen = []
        for y in self.grid:
            for x in y:    
                screen.append(f"\x1b[48;5;{x[1]}m \x1b[48;5;{x[0]}m ")
            screen.append('\n\x1b[0')
        print(''.join(screen),end=self.END) 
    @staticmethod
    def kill(*msg):
        print("\x1b[0m",*msg)
        quit()
