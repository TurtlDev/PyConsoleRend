from typing import Literal


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
                color_mode: Literal['bw','rgb'] = "bw"):
        self.width = dims[0]
        self.height = dims[1]
        self.dims = dims
        if color_mode != "bw":
            raise NotImplementedError("""
            *ring ring*
            ben
            ho ho ho 
            nno""")
        #yes, you can color half pixel
        #sadly, you cant color a quarter of a pixel
        self.grid:dict = {
            y:[
                [0,0] for x in range(self.width)
            ]  for y in range(self.height)
        }
    def __getitem__(self,y:int | float):
        print(y)
        return self.grid[y]

    def __setitem__(self,y,x=0):
        print("dont.")

    def __invert__(self):
        for y in enumerate(self.grid.values()):#a
            print(y)
            for x in enumerate(y[1]):
                self.grid[y[0]][x[0]][0] = 1 if x[1][0] == 0 else 0
    def render(self):
        col = [0,15]
        screen = '\033[0'
        for y in tuple(self.grid.values()):
            for x in y:
                screen += f"\033[48;5;{col[x[0]]}m \033[48;5;{col[x[1]]}m "
            screen += '\033[0m\n'
        print(screen,end='\n\033[0')