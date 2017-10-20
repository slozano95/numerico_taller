import math
import numpy as np
def f(x):
    return math.sin(x)
    
a = 0
b = 2

integ=(-math.cos(2))-(-math.cos(0))
print integ
#rango = np.arange(0.6,0.7,0.00001)
#for j in range(1,len(rango)):
#    n = rango[j]
#    h = (b-a)/n
#    suma = 0
#
#    for i in range(1,int(n-1)):
#        x = a+h*i
#        suma += 2 * f(x)
#    suma = suma + f(a) +f(b)
#    ans = suma*h/2
#    dif = integ-ans
#    print "N: ",n," ANS: ",ans," DIF: ",dif
#    if(dif<0.0002):
#        print "ENCONTRADO"
#        break
n = 0.64214
h = (b-a)/n
suma = 0

for i in range(1,int(n-1)):
    x = a+h*i
    suma += 2 * f(x)
suma = suma + f(a) +f(b)
ans = suma*h/2
dif = integ-ans
print "N: ",n," ANS: ",ans," DIF: ",dif

