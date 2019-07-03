import pygal

from dice import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(500):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

max_num = die_1.num_sides + die_2.num_sides
for value in range(2, max_num + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Result of rolling two D6 500 times'
hist.x_title = 'Result'
hist.y_title = 'Frquence of Result'
hist.x_labels = list(range(2, max_num + 1))

hist.add('Two D6', frequencies)
hist.render_to_file('Two_D6.svg')