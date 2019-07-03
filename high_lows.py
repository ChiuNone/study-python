import csv

from matplotlib import pyplot as plt

from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    '''打开文件并将文件对象储存在f中，读取它'''
    weather = csv.reader(f)
    '''next()函数读取文件中的下一行，这里调用一次所以读取第一行'''
    header_row = next(weather)

    '''打印第一行的位置索引和对应的值'''
    for index, column_header in enumerate(header_row):
        print(index, column_header)

#获取最高和最低温度数据
#csv中每一行便是一个列表对象,注意得到的数据时字符串格式
with open(filename) as f:
    weather = csv.reader(f)
    header_row = next(weather)

    #温度获取
    highs = []
    lows = []
    for row in weather:
        high = int(row[1])
        highs.append(high)

    #最低温度
        low = int(row[3])
        lows.append(low)

#绘制最高气温图

fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(highs, c = 'red', linewidth = 4)

plt.title('Daily high temperatures, July 2014', fontsize =24)
plt.xlabel('', fontsize = 16)
plt.ylabel('temperature(F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

#上述程序没有加入时间坐标，使用模块datetime添加日期，导入datetime模块中的datetime类
#并使用datetime类中的方法strptime()，接受一个日期字符串，将其转换成时间格式yy-mm-dd。
with open(filename) as f:
    weather = csv.reader(f)
    header_row = next(weather)

    #提取最高温度和时间数据
    highs, dates = [], []
    for row in weather:
        high = int(row[1])
        highs.append(high)

        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

#绘制时间-高温图
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = 'red')

plt.title('Daily high temperatures, July 2014', fontsize =24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('temperature(F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()

#涵盖更长时间
file2name = 'sitka_weather_2014.csv'

with open(file2name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = 'red')

plt.title('Month high temperatures -2014', fontsize = 24)
plt.xlabel('', fontsize = 14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize = 14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

#加入最低气温，绘制图表
#修改原图。在高低区域间着色
with open(file2name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

fig = plt.figure(dpi = 128, figsize = (10, 6))
#着色
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
#填充高低温之间的区域，alpha=指定颜色透明度
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

plt.title('Month high and low temperatures -2014', fontsize = 26)
plt.xlabel('', fontsize = 14)
fig.autofmt_xdate()
plt.ylabel('Temperatures(F)', fontsize = 14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()






