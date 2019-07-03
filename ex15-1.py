#5个点
import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c = 'red', s = 60)

plt.title('Cube of Value', fontsize = 22)
plt.xlabel('value', fontsize = 12)
plt.ylabel('cube', fontsize = 12)

plt.tick_params(axis = 'both', which = 'major', labelsize = 10)
plt.show()

#5000个点
import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c = 'yellow', s = 60)

plt.title('Cube of Value', fontsize = 22)
plt.xlabel('value', fontsize = 12)
plt.ylabel('cube', fontsize = 12)

plt.tick_params(axis = 'both', which = 'major', labelsize = 10)
plt.show()
