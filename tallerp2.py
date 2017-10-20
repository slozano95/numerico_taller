import math
import numpy as np

def derivada(a,b):
    return 1

L = 0.098
R = 0.142
t = [1.00,1.01,1.02,1.03,1.04]
i = [3.10,3.12,3.14,3.18,3.24]
#I(t)=V(1-e^(-Rt/L))
for k in range(1,len(t)):
    V = i[k]/(1-math.exp(-R*t[k]/L))
    print "t: ",t[k]," i: ",i[k]," V: ",V
