import math
import numpy
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot
from scipy.integrate import solve_ivp

# Constants
mu = 4*math.pi**2
timesteps = numpy.linspace(0, 2, 1000)

# Two body problem function
def twobody(t, state):
    x, y, vs, vy = state
    r = numpy.sqrt(x**2 + y**2)
    d2x = -mu * x / r**3
    d2y = -mu * y / r**3
    return [vs, vy, d2x, d2y]

# Define initial conditions
state0 = [1, 0, 0, 2*math.pi]

# Solve IVP
orbital = solve_ivp(twobody,(0, 2), state0, t_eval=timesteps)

# Positions
x_pos = orbital.y[0]
y_pos = orbital.y[1]

# Graph
fig, ax = matplotlib.pyplot.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)

# Objects on graph
ax.plot(0, 0, marker = 'o', markersize = 10, color = 'yellow', label = 'Star') # Star
path, = ax.plot([], [], marker = '_', color = 'blue', label = 'Planet Path')[0] # Planet path
Planet, = ax.plot([], [], marker = 'o', markersize = 4, color = 'blue', label = 'Planet')[0] # Planet 

# Show graph
matplotlib.pyplot.show()