import Canvas, Obj, Draw, time

import numpy as np
from timeit import timeit


x = Canvas.canvas((31,31))
y = Obj.obj((([0,0],[1,2]),([29,0],[0,2]),([0,10],[0,1])),[0,0])


while 1:
    x.checkerboard(0,size="big")
    Draw.DrawObject(y,x,1)
    x.render()
    time.sleep(.3)
    y.pos[1] += .1
