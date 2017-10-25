import numpy as np
from scipy.integrate import simps
def curva1(x):
    return x**2
def curva2(x):
    return x**3
#puntos
x = np.array([1,3,4])
y1 = curva1(x)
rta = simps(y1, x)
print(rta)
