import pygal

from random_walk import RandomWalk

rw = RandomWalk(100)
rw.fill_walk()

hist = pygal.Bar()

hist.title = 'Random Walk'

hist.x_labels = rw.x_values
hist.y_labels = rw.y_values

hist.add('RW', rw.y_values)
hist.render_to_file('Random Walk.svg')