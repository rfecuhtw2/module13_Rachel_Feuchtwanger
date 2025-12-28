import os
import matplotlib.pyplot as plt

PATH_WEATHER = os.path.join('docs','weather_data_flatbush.csv')
PATH_EXTREMES = os.path.join('docs','flatbush_extremes.csv')

months = []
high_temps = []
low_temps = []
rains = []

record_highs = []
record_lows = []
snows = []

ranges = []

colors = ('#219ebc', '#ffafcc','#06d6a0', '#bdb2ff', '#ffd6a5','#15616d','#ffd500', '#ffc6ff'
          ,'#e2ece9', '#f72585','#a4c3b2','#081c15')

def read_weather():
    with open(PATH_WEATHER, 'r') as f:
        header = f.readline()
        for line in f:
            line = line.strip()
            line = line.split(',')

            month = line[0]
            high_temp = int(line[1])
            low_temp = int(line[2])
            rain = float(line[3])

            months.append(month)
            high_temps.append(high_temp)
            low_temps.append(low_temp)
            rains.append(rain)


def extremes():
    with open(PATH_EXTREMES, 'r') as f:
        header = f.readline()
        for line in f:
            line = line.strip()
            line = line.split(',')


            record_high = int(line[1])
            record_low= int(line[2])
            snow = float(line[3])

            record_highs.append(record_high)
            record_lows.append(record_low)
            snows.append(snow)


def linechart():
    x_coords = list(range(len(months)))
    y_coords = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]

    plt.xticks(x_coords, months)
    plt.yticks(y_coords)

    plt.plot(x_coords, high_temps, color=colors[0], marker = 'o')
    plt.plot(x_coords, low_temps, color=colors[1], marker = 'o')
    plt.grid(True)
    plt.xlabel('Month')
    plt.ylabel('Temperature')
    plt.title('Average Temperature Per Month')

    plt.show()

    max_high = max(high_temps)
    max_low = max(low_temps)

    max_month = months[high_temps.index(max_high)]
    min_months = months[low_temps.index(max_low)]

    print("---Graph 1:---")
    print(f"the month with the highest value is {max_month}")
    print(f"the month with the lowest value is {min_months}")
    print(f'the difference between the highest and lowest temperatures is {max(high_temps) - min(high_temps)}')

def barchart():
    x_coords = list(range(len(months)))
    bar_width =0.3

    plt.bar([x - bar_width/2 for x in x_coords],
            record_lows,
            bar_width,
            color=colors[1])

    plt.bar([x + bar_width/2 for x in x_coords],
            record_highs,
            bar_width,
            color=colors[2])

    plt.xticks(x_coords, months)
    plt.grid(True)
    plt.xlabel('Month')
    plt.ylabel('Temperature')
    plt.title('Record High Temperatures Per Month')

    plt.show()

    max_high = max(record_highs)
    max_low = max(record_lows)

    max_month = months[record_highs.index(max_high)]
    min_months = months[record_lows.index(max_low)]

    print("---Graph 2:---")
    print(f"the month with the highest value is {max_month}")
    print(f"the month with the lowest value is {min_months}")
    print(f"The difference between the highest and lowest temperatures is {max(record_highs) - min(record_lows)}")


def pie_chart():
    plt.pie(snows, labels= months, colors = colors, autopct='%1.1f%%')
    plt.title('Snowfall Per Month')
    plt.axis('equal')

    plt.show()

    max_snow = max(snows)
    min_snow = min(snows)

    max_month = months[snows.index(max_snow)]
    min_months = months[snows.index(min_snow)]

    print("---Graph 3:---")
    print(f"the month with the highest value is {max_month}")
    print(f"the month with the lowest value is {min_months}")
    print(f"the difference between the highest and lowest snowfall is {max(snows) - min(snows)}")

def largest_temp_range():
    for i in range(len(months)):
        temp_range = record_highs[i] - record_lows[i]
        ranges.append(temp_range)

    x_coords = list(range(len(months)))
    y_coords = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

    plt.xticks(x_coords, months)
    plt.yticks(y_coords)

    plt.plot(x_coords, ranges, color=colors[9], marker='o')
    plt.grid(True)
    plt.xlabel('Month')
    plt.ylabel('Temperature')
    plt.title('Temperature Ranges Per Month')

    plt.show()

    max_range = max(ranges)
    min_range = min(ranges)

    max_month = months[ranges.index(max_range)]
    min_months = months[ranges.index(min_range)]

    print("---Graph 4:---")
    print(f"the month with the highest value is {max_month}")
    print(f"the month with the lowest value is {min_months}")
    print(f"the difference between the highest and lowest value is {max(ranges) - min(ranges)}")

def main():
    read_weather()
    extremes()
    linechart()
    barchart()
    pie_chart()
    largest_temp_range()
if __name__ == "__main__":
    main()