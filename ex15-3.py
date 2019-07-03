import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.figure(dpi = 128, figsize = (10, 6))

plt.plot(rw.x_values, rw.y_values, linewidth = 1)

plt.scatter(0, 0, c = 'red', s = 30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'green', s =40)

plt.show()

