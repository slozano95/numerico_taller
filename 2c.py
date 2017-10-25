import math
import numpy as np
import scipy.integrate as integrate
import scipy.special as special
from numpy import sqrt, sin, cos, pi
def f(x):
    result = integrate.quad(lambda x: sqrt(x)*sin(x), 0, 2)
    print result
def trapecios(a,b,m):
    h=(b-a)/m
    s=0
    for i in range(1,m):
        s = s+f(a+1*h)
    r=h/2*(f(a)+2*s+f(b))
    return r
f(1)
