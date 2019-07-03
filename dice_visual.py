import pygal

from dice import Die

#创建一个6面骰子
D6 = Die()
results = []

#投掷100次，并将结果保存到一个列表中
for roll_num in range(100):
    result = D6.roll()
    results.append(result)

#分析结果,分析1-6个数字出现的次数
frequencies = []

for value in range(1, D6.num_sides + 1):#取左不取右
    frequency = results.count(value)
    frequencies.append(frequency)

#对上面得到的结果进行可视化
hist = pygal.Bar()

#设置属性，注意这里是属性，不是方法函数
hist.title = 'Results of Rolling one D6 100 times'
hist.x_labels = list(range(1, D6.num_sides+1))
hist.x_title = 'Result'
hist.y_title = 'Frequence of Result'

#传递值
hist.add('D6', frequencies)#D6设置标签
hist.render_to_file('dice_visual.svg')