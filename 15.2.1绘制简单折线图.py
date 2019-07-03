#matplotlib是库，pyplot是模块，函数plot()根据数值生成有意义的图表
#.show()打开matplotlib查看器，查看绘制而成图表

##自定义，调整可视化图表的各个方面

import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares, linewidth = 5)#linewidth决定绘制线条的粗细

#设置图表标题，并给坐标加上标签
plt.title('Square Numbers', fontsize = 24)#给图标指定标题，字体大小
plt.xlabel('Value', fontsize = 14)#x轴名称
plt.ylabel('Square of Value', fontsize = 14)#y轴名称

#设置刻度标记大小
plt.tick_params(axis= 'both', labelsize = 14)#设置刻度样式
#axis = 'both'：同时设置x，y轴
#labelsize=14:设置刻度标记字号大小
plt.show()

#校正图形
#在上述代码绘制出的图形并不正确，折线图终点指出4的平方等于25
#因为向plot()提供一串数字时，它假设的第一个x坐标是0，而提供的列表是1开头
#同时向plot()提供输入值和输出值(x,y)，可以改变这种默认行为。






