#绘制散点图并设置不同颜色的点显示不同大小的值

#绘制单个点
#设置修改输出点的样式
import matplotlib.pyplot as plt

plt.scatter(2, 4, edgecolor = 'none', s = 200)#传入单个点的坐标(x,y)，s= 设置绘制图形时使用点的尺寸大小

#设置图表标题并给坐标添加标签
plt.title('one point', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('yValue', fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
#which = 'major'：设置主刻度线

plt.show()


