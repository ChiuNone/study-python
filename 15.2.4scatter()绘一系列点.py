#向scatter()传递两个分别包含x值,y值得列表

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s = 100)

plt.title('Squares of values', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square', fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

#以上程序都是直接计算出相关x，y得值然后绘图，效率较低
#可以使用循环来计算，例子：绘制1000个点的平方数，具体看下
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c = 'red', edgecolor = 'none', s = 40)
#在matplotlib2.0以上版本scatter()函数的实参edgecolor默认为'none'
#默认数据点颜色为蓝色，可向函数scatter()传递参数c来修改数据点颜色
#还可以使用RGB颜色模式自定义颜色，传递参数c = (红蓝绿的分量)，注意其为一个元组

plt.title('Squares of values', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square', fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0,1001,0,1100000])
#axis()函数提供四个值：x和y的最小值和最大值

plt.show()
