import Canvas, Obj, time
from timeit import timeit
lim = time.time()
f = open("demofile2.txt", "a")
x = Canvas.canvas((31,31))
y = Obj.Loadobj("demofile.npy")
while 1:
    lim = time.time()
    x.checkerboard(25,50,size="big")
    y.Draw(x,1)
    x.render()
    y.pos[1] += 1
    f.write(str(time.time()-lim)+ '\n')
    f.flush()
