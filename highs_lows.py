import csv

from matplotlib import pyplot as plt

from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print(current_date, 'missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    fig = plt.figure(dpi = 128, figsize = (10, 6))
    plt.plot(dates, highs, c = 'red', alpha = 0.4)
    plt.plot(dates, lows, c = 'green', alpha = 0.4)
    plt.fill_between(dates, highs, lows, facecolor = 'green', alpha = 0.1)

    title = 'Daily high and low temperatures -2014\nDeath Valley, CA'
    plt.title(title, fontsize = 20)
    plt.xlabel('', fontsize = 12)
    fig.autofmt_xdate()
    plt.ylabel('Temerature(F)', fontsize = 12)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 12)

    plt.show()



