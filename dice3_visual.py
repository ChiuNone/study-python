import pygal

from dice import Die

d7 =Die(7)
d9 = Die(9)

results = []
for roll_num in range(2000):
    result = d7.roll() + d9.roll()
    results.append(result)

frequencies = []
max_result = d7.num_sides + d9.num_sides
for value in range(2, max_result +1 ):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Result of rolling D7 and D8 2000times'
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'
hist.x_labels = list(range(2, max_result + 1))

hist.add('D7 and D9', frequencies)
hist.render_to_file('D7 and D9.svg')