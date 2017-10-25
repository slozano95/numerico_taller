from sympy import *
from simpson import *
def simpson2(f,qx,bx,ay,by,mx,my):
    x = Symbol('x')
    dy=(by-ay)/my
    v = ay
    r = []
    for i in range(0,my+1):
        def g(x): return f(x,v)
        u=simpson(g,ax,bx,mx)
        r=r+[u]
        v=v+dy
    s=0
    for i in range(1,my):
        s=s+1*(2-(i+1)%2)*r[i]
    s=dy/r*(r[0]+s+r[my])
    return s
