from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os

import Retriever

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('startup.html')

@app.route("/landing")
def landing_page():
    Retriever.get_current_weather()
    Retriever.get_48hours_temperatures()
    Retriever.get_week_forecast()
    Retriever.get_yesterday_weather()
    return render_template('landing.html')


@app.route("/48hourtables")
def tables_48_hour():
    #CURRENT DATA
    file_name = os.path.join("data", "current_weather.txt")
    f = open(file_name, 'r')
    next(f)
    line = f.readline()
    forecast = line.split('\t')
    c_temp = forecast[0]
    c_apparent_temp = forecast[1]
    c_precipitation = forecast[2]
    c_wind_speed = forecast[3]
    c_humidity = forecast[4]
    date_time = forecast[5].split()
    c_date = date_time[0]
    c_time = date_time[1]
    c_forecast_type = forecast[6]
    f.close()
    #YESTERDAY DATA
    file_name = os.path.join("data", "yesterday_weather.txt")
    f = open(file_name, 'r')
    next(f)
    line = f.readline()
    forecast = line.split('\t')
    y_hi_temp = forecast[0]
    y_lo_temp = forecast[1]
    y_precipitation = forecast[2]
    y_wind_speed = forecast[3]
    y_humidity = forecast[4]
    y_date = forecast[5]
    f.close()
    return render_template('48hourtables.html', c_temp = c_temp, c_apparent_temp = c_apparent_temp, c_precipitation = c_precipitation, c_wind_speed = c_wind_speed, c_humidity = c_humidity, c_date = c_date, c_time = c_time, c_forecast_type = c_forecast_type,
                           y_hi_temp = y_hi_temp, y_lo_temp = y_lo_temp, y_precipitation = y_precipitation, y_wind_speed = y_wind_speed, y_humidity = y_humidity, y_date = y_date)


@app.route("/48hourplot")
def plot_48_hour():
    #48 HOUR PLOT
    file_name = os.path.join("data", "48hours_temp.txt")
    timeseries = np.genfromtxt(file_name, skip_header = 2, delimiter="\t")
    h = [] #hours (x-axis)
    t = [] #temperature (y-axis)
    for entry in timeseries:
        h.append(entry[0])
        t.append(entry[1])
    temps = np.array(t)
    hours = np.array(h)

    indices = np.logical_and(timeseries[:,0] <= 0, timeseries[:,1] )
    subset_timeseries_1 = timeseries[indices, :]
    subset_coefficients_1 = np.polyfit(subset_timeseries_1[:,0], subset_timeseries_1[:,1], 1)
    subset_f_1 = np.poly1d(subset_coefficients_1)
    subset_trend_line_1 = subset_f_1(subset_timeseries_1[:,0])

    indices = np.logical_and(timeseries[:,0] >= 0, timeseries[:,1] )
    subset_timeseries_2 = timeseries[indices, :]
    subset_coefficients_2 = np.polyfit(subset_timeseries_2[:,0], subset_timeseries_2[:,1], 1)
    subset_f_2 = np.poly1d(subset_coefficients_2)
    subset_trend_line_2 = subset_f_2(subset_timeseries_2[:,0])
    min_temp_y = temps.min()
    max_temp_y = temps.max()
    max_temp_x = 0
    min_temp_x = 0
    for i in range (len(temps)):
        if (temps[i] == max_temp_y):
            max_temp_x = i
        if (temps[i] == min_temp_y):
            min_temp_x = i
    max_temp_x = hours[max_temp_x]
    min_temp_x = hours[min_temp_x]

    fig = plt.figure()
    plt.plot(h, t, 'k', linewidth=2)
    plt.plot(max_temp_x, max_temp_y, marker='o', markersize = 10, markeredgecolor = "black", markerfacecolor = "red")
    plt.plot(min_temp_x, min_temp_y, marker='o', markersize = 10, markeredgecolor = "black", markerfacecolor = "blue")
    plt.text(max_temp_x + 2, max_temp_y, 'Highest Temperature')
    plt.text(min_temp_x + 2, min_temp_y, 'Lowest Temperature')
    plt.plot(subset_timeseries_1[:,0], subset_trend_line_1, linestyle='--', linewidth=1.0, label='First 24 hours', color='Orange')
    plt.plot(subset_timeseries_2[:,0], subset_trend_line_2, linestyle='--', linewidth=1.0, label='Second 24 hours', color='Purple')
    
    plt.grid(linewidth=0.5, alpha=0.8)
    plt.xlim(-24, 24)
    plt.xticks([-24, -18, -12, -6, 0, 6, 12, 18, 24])
    plt.ylabel('Temperature (F)')
    plt.xlabel('Hour')
    plt.title('48 Hour Forecast')
    plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
    fig.savefig("static/48hourplot.png", bbox_inches='tight')
    plt.close(fig)
    return render_template('48hourplot.html')


@app.route("/7daytable")
def tables_7_day():
    #7 DAY FORECAST
    file_name = os.path.join("data", "forecast_weather.txt")
    f = open(file_name, 'r')
    next(f)
    line = f.readline()
    forecast = line.split('\t')
    hi_temp1 = forecast[0]
    lo_temp1 = forecast[1]
    precipitation1 = forecast[2]
    wind_speed1 = forecast[3]
    humidity1 = forecast[4]
    date1 = forecast[5]
    condition1 = forecast[6]

    line = f.readline()
    forecast = line.split('\t')
    hi_temp2 = forecast[0]
    lo_temp2 = forecast[1]
    precipitation2 = forecast[2]
    wind_speed2 = forecast[3]
    humidity2 = forecast[4]
    date2 = forecast[5]
    condition2 = forecast[6]

    line = f.readline()
    forecast = line.split('\t')
    hi_temp3 = forecast[0]
    lo_temp3 = forecast[1]
    precipitation3 = forecast[2]
    wind_speed3 = forecast[3]
    humidity3 = forecast[4]
    date3 = forecast[5]
    condition3 = forecast[6]

    line = f.readline()
    forecast = line.split('\t')
    hi_temp4 = forecast[0]
    lo_temp4 = forecast[1]
    precipitation4 = forecast[2]
    wind_speed4 = forecast[3]
    humidity4 = forecast[4]
    date4 = forecast[5]
    condition4 = forecast[6]

    line = f.readline()
    forecast = line.split('\t')
    hi_temp5 = forecast[0]
    lo_temp5 = forecast[1]
    precipitation5 = forecast[2]
    wind_speed5 = forecast[3]
    humidity5 = forecast[4]
    date5 = forecast[5]
    condition5 = forecast[6]

    line = f.readline()
    forecast = line.split('\t')
    hi_temp6 = forecast[0]
    lo_temp6 = forecast[1]
    precipitation6 = forecast[2]
    wind_speed6 = forecast[3]
    humidity6 = forecast[4]
    date6 = forecast[5]
    condition6 = forecast[6]

    line = f.readline()
    forecast = line.split('\t')
    hi_temp7 = forecast[0]
    lo_temp7 = forecast[1]
    precipitation7 = forecast[2]
    wind_speed7 = forecast[3]
    humidity7 = forecast[4]
    date7 = forecast[5]
    condition7 = forecast[6]
    f.close()
    return render_template('7daytable.html', hi_temp1 = hi_temp1, lo_temp1 = lo_temp1, precipitation1 = precipitation1, wind_speed1 = wind_speed1, humidity1 = humidity1, date1 = date1, condition1 = condition1,
                            hi_temp2 = hi_temp2, lo_temp2 = lo_temp2, precipitation2 = precipitation2, wind_speed2 = wind_speed2, humidity2 = humidity2, date2 = date2, condition2 = condition2,
                            hi_temp3 = hi_temp3, lo_temp3 = lo_temp3, precipitation3 = precipitation3, wind_speed3 = wind_speed3, humidity3 = humidity3, date3 = date3, condition3 = condition3,
                            hi_temp4 = hi_temp4, lo_temp4 = lo_temp4, precipitation4 = precipitation4, wind_speed4 = wind_speed4, humidity4 = humidity4, date4 = date4, condition4 = condition4,
                            hi_temp5 = hi_temp5, lo_temp5 = lo_temp5, precipitation5 = precipitation5, wind_speed5 = wind_speed5, humidity5 = humidity5, date5 = date5, condition5 = condition5,
                            hi_temp6 = hi_temp6, lo_temp6 = lo_temp6, precipitation6 = precipitation6, wind_speed6 = wind_speed6, humidity6 = humidity6, date6 = date6, condition6 = condition6,
                            hi_temp7 = hi_temp7, lo_temp7 = lo_temp7, precipitation7 = precipitation7, wind_speed7 = wind_speed7, humidity7 = humidity7, date7 = date7, condition7 = condition7)

@app.route("/7dayplot")
def plot_7_day():
    file_name = os.path.join("data", "forecast_weather.txt")
    timeseries = np.genfromtxt(file_name, skip_header = 1, delimiter="\t")
    hi_t = [] #high temp (y-axis)
    lo_t = [] #low temp (y-axis)
    for entry in timeseries:
        hi_t.append(entry[0])
        lo_t.append(entry[1])
    hi_temps = np.array(hi_t)
    lo_temps = np.array(lo_t)
    hi_temps_min = hi_temps.min()
    hi_temps_max = hi_temps.max()
    lo_temps_min = lo_temps.min()
    lo_temps_max = lo_temps.max()
    hi_max = 0
    hi_min = 0
    lo_max = 0
    lo_min = 0
    for i in range (len(hi_temps)):
        if (hi_temps[i] == hi_temps_max):
            hi_max = i
        if (hi_temps[i] == hi_temps_min):
            hi_min = i
        if (lo_temps[i] == lo_temps_max):
            lo_max = i
        if (lo_temps[i] == lo_temps_min):
            lo_min = i

    sum_arr = np.add(hi_temps,lo_temps)
    avg_temps = sum_arr/2
    fig = plt.figure()
    date = []
    f = open(file_name, 'r')
    next(f)
    for line in f:
        x = line.split()
        date.append(x[5])
    f.close()
    fig = plt.figure()
    plt.plot([0,1,2,3,4,5,6], hi_t, 'r', linewidth=2, label = 'High Temperatures')
    plt.plot([0,1,2,3,4,5,6], lo_t, 'b', linewidth=2, label = 'Low Temperatures')
    plt.plot(hi_max, hi_temps_max, marker='o', markersize = 10, markeredgecolor = "black", markerfacecolor = "red")
    plt.plot(hi_min, hi_temps_min, marker='o', markersize = 10, markeredgecolor = "black", markerfacecolor = "blue")
    plt.plot(lo_max, lo_temps_max, marker='o', markersize = 10, markeredgecolor = "black", markerfacecolor = "red")
    plt.plot(lo_min, lo_temps_min, marker='o', markersize = 10, markeredgecolor = "black", markerfacecolor = "blue")
    
    plt.plot([0,1,2,3,4,5,6], avg_temps, 'g', linestyle = '--', label = 'Average Temperatures')
    plt.grid(linewidth=0.5, alpha=0.8)
    plt.xticks([0,1,2,3,4,5,6], date)
    plt.gcf().autofmt_xdate()
    plt.ylabel('Temperature (F)')
    plt.xlabel('Date')
    plt.title('7 Day Forecast')
    plt.legend(bbox_to_anchor=(1.02, 0.1), loc='upper left', borderaxespad=0)
    fig.savefig("static/7dayplot.png", bbox_inches='tight')
    plt.close(fig)
    return render_template("7dayplot.html")


# @app.route("/currentWeather")
# def home_to_today_page():

#     Retriever.get_current_weather()
#     Retriever.get_48hours_temperatures()
#     Retriever.get_week_forecast()
#     Retriever.get_yesterday_weather()

#     #48 HOUR PLOT
#     file_name = os.path.join("data", "48hours_temp.txt")
#     timeseries = np.genfromtxt(file_name, skip_header = 2, delimiter="\t")
#     h = [] #hours (x-axis)
#     t = [] #temperature (y-axis)
#     for entry in timeseries:
#         h.append(entry[0])
#         t.append(entry[1])
#     fig = plt.figure()
#     plt.plot(h, t, linewidth=2)
#     plt.grid(linewidth=0.5, alpha=0.8)
#     plt.xlim(-24, 24)
#     plt.xticks([-24, -18, -12, -6, 0, 6, 12, 18, 24])
#     plt.ylabel('Temperature (C)')
#     plt.xlabel('Hour')
#     plt.title('48 Hour Forecast')
#     fig.savefig("static/48hourplot.png")
#     plt.close(fig)
    
#     #7DAY PLOT 
#     file_name = os.path.join("data", "forecast_weather.txt")
#     timeseries = np.genfromtxt(file_name, skip_header = 1, delimiter="\t")
#     hi_t = [] #high temp (y-axis)
#     lo_t = [] #low temp (y-axis)
#     for entry in timeseries:
#         hi_t.append(entry[0])
#         lo_t.append(entry[1])
#     fig = plt.figure()
#     date = []
#     f = open(file_name, 'r')
#     next(f)
#     for line in f:
#         x = line.split()
#         date.append(x[5])
#     f.close()
#     fig = plt.figure()
#     plt.plot([0,1,2,3,4,5,6], hi_t, 'r', linewidth=2, label = 'High Temperatures')
#     plt.plot([0,1,2,3,4,5,6], lo_t, 'b', linewidth=2, label = 'Low Temperatures')
#     plt.grid(linewidth=0.5, alpha=0.8)
#     plt.xticks([0,1,2,3,4,5,6], date)
#     plt.gcf().autofmt_xdate()
#     plt.ylabel('Temperature (F)')
#     plt.xlabel('Date')
#     plt.title('7 Day Forecast')
#     plt.legend()
#     fig.savefig("static/7dayplot.png")
#     plt.close(fig)


#     #CURRENT DATA
#     file_name = os.path.join("data", "current_weather.txt")
#     f = open(file_name, 'r')
#     next(f)
#     line = f.readline()
#     forecast = line.split('\t')
#     c_temp = forecast[0]
#     c_apparent_temp = forecast[1]
#     c_precipitation = forecast[2]
#     c_wind_speed = forecast[3]
#     c_humidity = forecast[4]
#     date_time = forecast[5].split()
#     c_date = date_time[0]
#     c_time = date_time[1]
#     c_forecast_type = forecast[6]
#     f.close()

#     #YESTERDAY DATA
#     file_name = os.path.join("data", "yesterday_weather.txt")
#     f = open(file_name, 'r')
#     next(f)
#     line = f.readline()
#     forecast = line.split('\t')
#     y_hi_temp = forecast[0]
#     y_lo_temp = forecast[1]
#     y_precipitation = forecast[2]
#     y_wind_speed = forecast[3]
#     y_humidity = forecast[4]
#     y_date = forecast[5]
#     f.close()

    
    
#     #7 DAY FORECAST
#     file_name = os.path.join("data", "forecast_weather.txt")
#     f = open(file_name, 'r')
#     next(f)
#     line = f.readline()
#     forecast = line.split('\t')
#     hi_temp1 = forecast[0]
#     lo_temp1 = forecast[1]
#     precipitation1 = forecast[2]
#     wind_speed1 = forecast[3]
#     humidity1 = forecast[4]
#     date1 = forecast[5]
#     condition1 = forecast[6]

#     line = f.readline()
#     forecast = line.split('\t')
#     hi_temp2 = forecast[0]
#     lo_temp2 = forecast[1]
#     precipitation2 = forecast[2]
#     wind_speed2 = forecast[3]
#     humidity2 = forecast[4]
#     date2 = forecast[5]
#     condition2 = forecast[6]

#     line = f.readline()
#     forecast = line.split('\t')
#     hi_temp3 = forecast[0]
#     lo_temp3 = forecast[1]
#     precipitation3 = forecast[2]
#     wind_speed3 = forecast[3]
#     humidity3 = forecast[4]
#     date3 = forecast[5]
#     condition3 = forecast[6]

#     line = f.readline()
#     forecast = line.split('\t')
#     hi_temp4 = forecast[0]
#     lo_temp4 = forecast[1]
#     precipitation4 = forecast[2]
#     wind_speed4 = forecast[3]
#     humidity4 = forecast[4]
#     date4 = forecast[5]
#     condition4 = forecast[6]

#     line = f.readline()
#     forecast = line.split('\t')
#     hi_temp5 = forecast[0]
#     lo_temp5 = forecast[1]
#     precipitation5 = forecast[2]
#     wind_speed5 = forecast[3]
#     humidity5 = forecast[4]
#     date5 = forecast[5]
#     condition5 = forecast[6]

#     line = f.readline()
#     forecast = line.split('\t')
#     hi_temp6 = forecast[0]
#     lo_temp6 = forecast[1]
#     precipitation6 = forecast[2]
#     wind_speed6 = forecast[3]
#     humidity6 = forecast[4]
#     date6 = forecast[5]
#     condition6 = forecast[6]

#     line = f.readline()
#     forecast = line.split('\t')
#     hi_temp7 = forecast[0]
#     lo_temp7 = forecast[1]
#     precipitation7 = forecast[2]
#     wind_speed7 = forecast[3]
#     humidity7 = forecast[4]
#     date7 = forecast[5]
#     condition7 = forecast[6]
#     f.close()




#     return render_template('currentWeather.html', c_temp = c_temp, c_apparent_temp = c_apparent_temp, c_precipitation = c_precipitation, c_wind_speed = c_wind_speed, c_humidity = c_humidity, c_date = c_date, c_time = c_time, c_forecast_type = c_forecast_type,
#                            y_hi_temp = y_hi_temp, y_lo_temp = y_lo_temp, y_precipitation = y_precipitation, y_wind_speed = y_wind_speed, y_humidity = y_humidity, y_date = y_date,
#                             hi_temp1 = hi_temp1, lo_temp1 = lo_temp1, precipitation1 = precipitation1, wind_speed1 = wind_speed1, humidity1 = humidity1, date1 = date1, condition1 = condition1,
#                             hi_temp2 = hi_temp2, lo_temp2 = lo_temp2, precipitation2 = precipitation2, wind_speed2 = wind_speed2, humidity2 = humidity2, date2 = date2, condition2 = condition2,
#                             hi_temp3 = hi_temp3, lo_temp3 = lo_temp3, precipitation3 = precipitation3, wind_speed3 = wind_speed3, humidity3 = humidity3, date3 = date3, condition3 = condition3,
#                             hi_temp4 = hi_temp4, lo_temp4 = lo_temp4, precipitation4 = precipitation4, wind_speed4 = wind_speed4, humidity4 = humidity4, date4 = date4, condition4 = condition4,
#                             hi_temp5 = hi_temp5, lo_temp5 = lo_temp5, precipitation5 = precipitation5, wind_speed5 = wind_speed5, humidity5 = humidity5, date5 = date5, condition5 = condition5,
#                             hi_temp6 = hi_temp6, lo_temp6 = lo_temp6, precipitation6 = precipitation6, wind_speed6 = wind_speed6, humidity6 = humidity6, date6 = date6, condition6 = condition6,
#                             hi_temp7 = hi_temp7, lo_temp7 = lo_temp7, precipitation7 = precipitation7, wind_speed7 = wind_speed7, humidity7 = humidity7, date7 = date7, condition7 = condition7)


# create a main method
if __name__ == "__main__":
    app.run()
