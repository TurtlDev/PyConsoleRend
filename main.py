import Canvas, Obj, Draw, time

import numpy as np
from timeit import timeit


x = Canvas.canvas((10,10))
y = Obj.obj((([2,2],[1]),([6,7],[])),[-2,2])
Draw.DrawObject(y, x)
while 1:
    x.render()