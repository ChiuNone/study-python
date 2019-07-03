import pygal

from dice import Die

d1 = Die()
d2 = Die()

results = []
for roll_num in range(1000):
    result = d1.roll() * d2.roll()
    results.append(result)

frequencies = []
max_result = d1.num_sides * d2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Result of rolling D6*D6 1000times'
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.x_labels = list(range(1, max_result + 1))

hist.add('D6-D6', frequencies)
hist.render_to_file('D6-D6.svg')