# Demo of live updating a plot in matlab
# Adapted from Parul Pandey's article on Towards Data Science
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c

import matplotlib.pyplot as plt
import matplotlib.animation as animation

filename = 'data.txt'

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open(filename,'r')
    lines = data.readlines()
    xs = []
    ys = []

    for line in lines:
        x, y = line.split(',') # Delimiter is comma
        xs.append(float(x))
        ys.append(float(y))

    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Interval')
    plt.ylabel('Value')
    plt.title('Live graph with matplotlib')

print(f"Add lines to the file {filename}")
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()