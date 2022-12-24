import numpy
import matplotlib.pyplot
import seaborn

seaborn.set_style("white")
seaborn.set_context("talk")

mass = 1
gravity_acceleation = numpy.array([0, -9.8])

start_position = numpy.array([0, 10])
start_vector = numpy.array([0, 0])
start_time = 0

time_index = 0.01

axis_times = []
axis_positions = []

while start_position[1] >= 0:
    axis_times.append(start_time)
    axis_positions.append(start_position)

    start_position = start_position + start_vector * start_time + 0.5 * gravity_acceleation * start_time**2
    start_time += time_index


fig, axs = matplotlib.pyplot.subplots(ncols=2, figsize=(8, 4), constrained_layout=True)
directions = ["x", "y"]
for i, (ax, direction) in enumerate(zip(axs, directions)):
    ax.scatter(axis_times, numpy.array(axis_positions)[:,i], alpha=0.3, c="k")
    ax.set_xlabel("time (s)")
    ax.set_title(f"{direction} position (m)", pad=12)

matplotlib.pyplot.show()
