#colormap简写cmap
#颜色映射是一系列渐变颜色，如可能用较浅的颜色表示较小的值，较浓的颜色表示较大的值
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 40)
#y_values的值赋给C，表示随着Y值的大小而改变颜色
#cmap参数告诉python该使用哪个颜色映射

plt.title('Square of Value', fontsize = 24)
plt.xlabel('Values', fontsize = 14)
plt.ylabel('Square', fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

#自动保存图表，用plt.saving()替换plt.show()
#plt.saving('square_plot.png', bbox_inches = 'tight')
#第一实参指定要以什么样的文件名保存图表，第二个实参指定将图表多余的空白区域裁剪掉。