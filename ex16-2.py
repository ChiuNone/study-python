import csv
from datetime import datetime

from matplotlib import pyplot as plt

file_1 = 'sitka_weather_2014.csv'
with open(file_1) as f:
    reader  = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red', alpha = 0.6)
    plt.plot(dates, lows, c = 'green', alpha = 0.6)
    plt.fill_between(dates, highs, lows, facecolor = 'Blue', alpha = 0.1)

    plt.title('Daily high and low temperatures -2014\nSitka, CA', fontsize = 26)
    plt.xlabel('', fontsize = 14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize = 14)
    plt.ylim(0, 120)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

    plt.show()


file_2 = 'death_valley_2014.csv'
with open(file_2) as f:
    reader  = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red', alpha = 0.6)
    plt.plot(dates, lows, c = 'green', alpha = 0.6)
    plt.fill_between(dates, highs, lows, facecolor = 'Blue', alpha = 0.1)

    plt.title('Daily high and low temperatures -2014\nSitka, CA', fontsize = 26)
    plt.xlabel('', fontsize = 14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize = 14)
    plt.ylim(0, 120)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

    plt.show()


#把两个图像绘制在一个图表中
def get_weather_date(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing date.')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

#先画sitka
dates, highs, lows = [], [], []
get_weather_date('sitka_weather_2014.csv', dates, highs, lows)

fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = 'red', alpha = 0.6)
plt.plot(dates, lows, c = 'green', alpha = 0.6)
plt.fill_between(dates, highs, lows, facecolor = 'Blue', alpha = 0.1)

#再画death_valley
dates, highs, lows = [], [], []
get_weather_date('death_valley_2014.csv', dates, highs, lows)

plt.plot(dates, highs, c = 'red', alpha = 0.4)
plt.plot(dates, lows, c = 'green', alpha = 0.4)
plt.fill_between(dates, highs, lows, facecolor = 'Blue', alpha = 0.05)

#设置图表格式
title = 'Daily high and low temperature -2014 '
title += '\n Sitka and Death Valley'
plt.title(title, fontsize = 26)
plt.xlabel('', fontsize = 14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize = 14)
plt.ylim(0, 120)
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()