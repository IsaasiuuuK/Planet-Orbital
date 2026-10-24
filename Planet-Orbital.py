import math
import numpy
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot
from scipy.integrate import solve_ivp

# Constants
mu = 4*math.pi**2
timesteps = numpy.linspace(0, 2, 1000)

# Velocity multiplier
velocity_multiplier = [0.8, 1, 1.2, 1.5]
colours = ["red", "blue", "green", "purple"]

# Two body problem function
def twobody(t, state):
    x, y, vs, vy = state
    r = numpy.sqrt(x**2 + y**2)
    d2x = -mu * x / r**3
    d2y = -mu * y / r**3
    return [vs, vy, d2x, d2y]

# Create Graph
fig, (orbit, energy) = matplotlib.pyplot.subplots(1,2, figsize=(12, 6))

# Stores solution
solutions = []

# Loop for every velocity multiplier
for x in velocity_multiplier:

    # Define initial conditions
    state_0 = [1, 0, 0, x*2*math.pi]

    # Solve IVP
    orbital = solve_ivp(twobody,(0, 2), state_0, t_eval=timesteps)

    # Positions and velocities
    x_pos = orbital.y[0]
    y_pos = orbital.y[1]
    vx = orbital.y[2]
    vy = orbital.y[3]

    # Specific energy
    energy_data = 0.5 * (vx**2 + vy**2) - mu / numpy.sqrt(x_pos**2 + y_pos**2)

    # Save solution
    solutions.append({"x_pos": x_pos, "y_pos": y_pos, "energy_data": energy_data})

# Orbit Graph
orbit.set_xlim(-3, 3)
orbit.set_ylim(-5, 5)
orbit.set_aspect('equal')
orbit.grid(True)

# Energy Graph
energy.set_xlabel('Time (years)')
energy.set_ylabel('Specific Energy')
energy.set_title('Specific Energy vs Time')
energy.set_xlim(timesteps[0], timesteps[-1])
energy_values = numpy.concatenate([solution["energy_data"] for solution in solutions])
energy.set_ylim(energy_values.min() - 0.1, energy_values.max() + 0.1)
energy.grid(True)

# Star on graph
orbit.plot(0, 0, marker = 'o', markersize = 10, color = 'yellow', label = 'Star') # Star

# Planet path and Planet
pathlist = []
planetlist = []
energylist = []

# Plot path and planet for each velocity multiplier
for y in range(len(velocity_multiplier)):
    path, = orbit.plot([], [], linestyle = '-', color = colours[y], label = f'vy = {velocity_multiplier[y]} × 2π') # Planet path
    Planet, = orbit.plot([], [], marker = 'o', markersize = 4, color = colours[y], label = 'Planet') # Planet 
    energy_path, = energy.plot([], [], linestyle = '-', color = colours[y], label = f'vy = {velocity_multiplier[y]} × 2π')
    pathlist.append(path)
    planetlist.append(Planet)
    energylist.append(energy_path)

# Label 
orbit.legend()

# Animation function
def animate(tick):
    for i in range(len(velocity_multiplier)):
        x_pos = solutions[i]["x_pos"]
        y_pos = solutions[i]["y_pos"]
        energy_data = solutions[i]["energy_data"]
        pathlist[i].set_data(x_pos[:tick + 1], y_pos[:tick + 1])
        planetlist[i].set_data([x_pos[tick]], [y_pos[tick]])
        energylist[i].set_data(timesteps[:tick + 1], energy_data[:tick + 1])
    return pathlist + planetlist + energylist

# Animate
frame_step = 5
animation_frames = list(range(0, len(x_pos), frame_step))
if animation_frames[-1] != len(x_pos) - 1:
    animation_frames.append(len(x_pos) - 1)
animation = FuncAnimation(fig, animate, frames=animation_frames, interval=1, repeat=False)

# Energy graph legend
energy.legend()

# Show graph
matplotlib.pyplot.show()