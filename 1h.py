import math

def dxdt(f):
    def dfdt(x, h=0.1e-5):
        return ( f(x+h/2) - f(x-h/2) )/h
    return dfdt

def funcion(x): return math.log(x)

y1era = dxdt(funcion)
y2da = dxdt(y1era)

print "f''(1.8) = ",y2da( 1.8 )
