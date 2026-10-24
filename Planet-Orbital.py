import math
import numpy
import matplotlib.pyplot
from scipy.integrate import solve_ivp

mu = 4*math.pi**2
timesteps = numpy.linspace(0, 2, 1000)

def twobody(t, state):
    r = numpy.sqrt(x**2 + y**2)
    x, y, vs, vy = state
    d2x = -mu * x / r**3
    d2y = -mu * y / r**3
    return [vs, vy, d2x, d2y]

state0 = [1, 0, 0, 2*math.pi]

orbital = solve_ivp(twobody,(0, 2), state0, t_eval=timesteps)