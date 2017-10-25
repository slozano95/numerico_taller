import scipy.integrate
import math
def cuadratura():
    ret = scipy.integrate.quad(lambda x: x*math.exp(x),2,1)
    print "CUADRATURA ",ret[0]," ERROR ",ret[1]
cuadratura()
