import Canvas, Obj, Draw, time

import numpy as np
from timeit import timeit


x = Canvas.canvas((20,20))
y = Obj.obj((([0,0],[]),([10,0],[0]),([10,10],[0,1])),[-2,2])
Draw.DrawObject(y, x, color)

while 1:
    x.render()
    time.sleep(.3)