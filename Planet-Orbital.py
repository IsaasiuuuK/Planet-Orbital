import math
import numpy
import matplotlib.pyplot
from scipy.integrate import solve_ivp

mu = 4*math.pi**2

def twobody(t, state):
    r = numpy.sqrt(x**2 + y**2)
    x, y, vs, vy = state
    d2x = -mu * x / r**3
    d2y = -mu * y / r**3
    return [vs, vy, d2x, d2y]   