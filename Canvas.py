import itertools

from typing import Literal
#add ascii support (text in image)

class canvas:
    exsist = False
    def __new__(cls,*args,**kwargs):
        if canvas.exsist:
            raise SystemError(
                "\033[38;2;255;0;0mmultiple instances of canvas cannot exsist"
                )
        canvas.exsist = True
        return super().__new__(cls)
    def __init__(self,dims: tuple[int,int],*, 
                color_mode: Literal['bw','rgb','ansi256'] = "ansi256"):
        self.width = dims[0]
        self.height = dims[1]
        self.dims = dims
        self.color_mode = color_mode
        #constants
        self.END ='\033[F'*(self.width*self.height)+'\033[0'
        self.COLORMODES = {'bw', 'rgb', 'ansi256'}
        self.BOTH = {"Both", "both", "B", "b"}
        self.RIGHTLEFT = {"Right":1,"right":1,"R":1,"r":1,
                          "Left":0,"left":0,"L":0,"l":0}#cant believe bro hard coded this shit
        #yes, you can color half pixel
        #sadly, you cant color a quarter of a pixel

        
        self.grid = [
            [
                [(0,0,0),(0,0,0)] for x in range(self.width)] if color_mode == 'rgb' 
            else [
                [0,0] for x in range(self.width)] for y in range(self.height)
            ]


    def __getitem__(self,y:int):
        print(y)
        return self.grid[y]

    def __setitem__(self,y,x=0):
        print("dont.")

    def __call__(self,**cnf):
        """config:
        color_mode -> default: rgb, acceptable params: bw, rgb"""
        if 'color_mode' in cnf:
            if cnf['color_mode'] not in self.COLORMODES:
                raise ValueError("invalid color option")
            self.color_mode=cnf['color_mode']
            self.grid = [
            [
                [(0,0,0),(0,0,0)] for x in range(self.width)
            ]  for y in range(self.height)] if self.color_mode == "rgb" else [[[0,0] for x in range(self.width)] for y in range(self.height)]

            
    def setcord(self,x,y,color: tuple[int, int, int] | int, 
                side: Literal["Left","left","L","l",
                "Right","right","R","r", "Both", "both", "B", "b"] = "b"):
            if self.color_mode == "rgb" and not isinstance(color,tuple):
                raise ValueError("rgb must take rgb value in form of tuple")
            if side in self.BOTH:
                self.grid[y][x][0] = self.grid[y][x][1] = ((color[0],color[1],color[2]) 
                                                           if self.color_mode == "rgb" else color)
                return
            self.grid[y][x][self.RIGHTLEFT[side]] = ((color[0],color[1],color[2])
                                                    if self.color_mode == "rgb" else color)
            return


    def checkerboard(self,colorA: tuple[int, int, int] | int, colorB: tuple[int, int, int] | int,
                     *,size: Literal["big","little"] = "big"):
        if self.color_mode == "rgb":
            if not isinstance(color,tuple):
                raise ValueError("rgb must take rgb value in form of tuple")
        if size == "big":
                for i in range(round(self.height)):
                    for ii in range(round(self.width)):
                        pass
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

    def render(self):
        screen = '\033[0'
        match self.color_mode:
            case "rgb":
                for y in self.grid:
                    for x in y:
                        if -1 in x[0]:
                            screen+='\033[0m '
                        if -1 in x[1]:
                            screen+='\033[0m '
                        screen += (
                        f"\033[48;2;{x[0][0]};{x[0][1]};{x[0][2]}m "
                        +f"\033[48;2;{x[1][0]};{x[1][1]};{x[1][2]}m ")
                    screen += '\033[0m\n'
            case "ansi256":
                for y in self.grid:
                    for x in y:
                        if x[0] == -1:
                            screen+='\033[0m '
                        else:
                            screen+=f"\033[48;5;{x[0]}m "
                        if x[1] == -1:
                            screen+='\033[0m '
                            continue
                        screen+=f"\033[48;5;{x[1]}m "
                    screen += '\033[0m\n'
            case "bw":
                col = {0:0,1:15}
                for y in self.grid:
                    for x in y:
                        screen += f"\033[48;5;{col[x[0]]}m \033[48;5;{col[x[1]]}m "
                    screen += '\033[0m\n'
        print(screen,end=self.END)
    @staticmethod
    def kill(*msg):
        print("\033[0m",*msg)
        quit()
        