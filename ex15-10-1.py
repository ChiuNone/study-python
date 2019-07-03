import matplotlib.pyplot as plt

from dice import Die

d = Die()

results = []
for roll_num in range(500):
    result = d.roll()
    results.append(result)

frequencies = []
for value in range(1, d.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, d.num_sides + 1))
y_values = frequencies

plt.plot(x_values, y_values, linewidth = 2)

plt.title('Result of Rolling D6 500 times', fontsize = 24)
plt.xlabel('Result', fontsize = 14)
plt.ylabel('Frequency of Rusult', fontsize = 14)

plt.axis([0,6,0,200])

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
plt.show()