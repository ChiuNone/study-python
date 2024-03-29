import pygal

from dice import Die

die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_2.num_sides + die_1.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Result of rolling Two D8 1000times'
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.x_labels = list(range(2, max_result + 1))

hist.add('Two D8', frequencies)
hist.render_to_file('Two D8.svg')