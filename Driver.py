from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import matplotlib.pyplot as plt

import Retriever

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('startup.html')

#48 HOUR DATA
file_name = "data/48hours_temp.txt"
timeseries = np.genfromtxt(file_name, skip_header = 2, delimiter="\t")
h = [] #hours (x-axis)
t = [] #temperature (y-axis)
for entry in timeseries:
    h.append(entry[0] - 24)
    t.append(entry[1])
fig = plt.figure()
plt.plot(h, t, linewidth=2)
plt.grid(linewidth=0.5, alpha=0.8)
plt.xlim(-48, 0)
plt.xticks([-48, -42, -36, -30, -24, -18, -12, -6, 0])
plt.ylabel('Temperature')
plt.xlabel('Hour')
plt.title('48 Hour Forecast')
fig.savefig("static/48hourplot.png")
plt.close(fig)
#7DAY PLOT 
file_name = "data/forecast_weather.txt"
timeseries = np.genfromtxt(file_name, skip_header = 1, delimiter="\t")
hi_t = [] #high temp (y-axis)
lo_t = [] #low temp (y-axis)
for entry in timeseries:
    hi_t.append(entry[0])
    lo_t.append(entry[1])
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
plt.grid(linewidth=0.5, alpha=0.8)
plt.xticks([0,1,2,3,4,5,6], date)
plt.gcf().autofmt_xdate()
plt.ylabel('Temperature')
plt.xlabel('Date')
plt.title('7 Day Forecast')
plt.legend()
fig.savefig("static/7dayplot.png")
plt.close(fig)
@app.route("/currentWeather")
def home_to_today_page():
    Retriever.get_current_weather()
    Retriever.get_48hours_temperatures()
    Retriever.get_week_forecast()
    Retriever.get_yesterday_weather()

    #CURRENT DATA
    file_name = "data/current_weather.txt"
    f = open(file_name, 'r')
    next(f)
    line = f.readline()
    forecast = line.split()
    c_temp = forecast[0]
    c_apparent_temp = forecast[1]
    c_precipitation = forecast[2]
    c_wind_speed = forecast[3]
    c_humidity = forecast[4]
    c_date = forecast[5]
    c_time = forecast[6]
    f.close()

    #YESTERDAY DATA
    file_name = "data/yesterday_weather.txt"
    f = open(file_name, 'r')
    next(f)
    line = f.readline()
    forecast = line.split()
    y_hi_temp = forecast[0]
    y_lo_temp = forecast[1]
    y_precipitation = forecast[2]
    y_wind_speed = forecast[3]
    y_humidity = forecast[4]
    y_date = forecast[5]
    f.close()

    
    
    #7 DAY FORECAST
    file_name = "data/forecast_weather.txt"
    f = open(file_name, 'r')
    next(f)
    line = f.readline()
    forecast = line.split()
    hi_temp1 = forecast[0]
    lo_temp1 = forecast[1]
    precipitation1 = forecast[2]
    wind_speed1 = forecast[3]
    humidity1 = forecast[4]
    date1 = forecast[5]

    line = f.readline()
    forecast = line.split()
    hi_temp2 = forecast[0]
    lo_temp2 = forecast[1]
    precipitation2 = forecast[2]
    wind_speed2 = forecast[3]
    humidity2 = forecast[4]
    date2 = forecast[5]

    line = f.readline()
    forecast = line.split()
    hi_temp3 = forecast[0]
    lo_temp3 = forecast[1]
    precipitation3 = forecast[2]
    wind_speed3 = forecast[3]
    humidity3 = forecast[4]
    date3 = forecast[5]

    line = f.readline()
    forecast = line.split()
    hi_temp4 = forecast[0]
    lo_temp4 = forecast[1]
    precipitation4 = forecast[2]
    wind_speed4 = forecast[3]
    humidity4 = forecast[4]
    date4 = forecast[5]

    line = f.readline()
    forecast = line.split()
    hi_temp5 = forecast[0]
    lo_temp5 = forecast[1]
    precipitation5 = forecast[2]
    wind_speed5 = forecast[3]
    humidity5 = forecast[4]
    date5 = forecast[5]

    line = f.readline()
    forecast = line.split()
    hi_temp6 = forecast[0]
    lo_temp6 = forecast[1]
    precipitation6 = forecast[2]
    wind_speed6 = forecast[3]
    humidity6 = forecast[4]
    date6 = forecast[5]

    line = f.readline()
    forecast = line.split()
    hi_temp7 = forecast[0]
    lo_temp7 = forecast[1]
    precipitation7 = forecast[2]
    wind_speed7 = forecast[3]
    humidity7 = forecast[4]
    date7 = forecast[5]
    f.close()




    return render_template('currentWeather.html', c_temp = c_temp, c_apparent_temp = c_apparent_temp, c_precipitation = c_precipitation, c_wind_speed = c_wind_speed, c_humidity = c_humidity, c_date = c_date, c_time = c_time,
                           y_hi_temp = y_hi_temp, y_lo_temp = y_lo_temp, y_precipitation = y_precipitation, y_wind_speed = y_wind_speed, y_humidity = y_humidity, y_date = y_date,
                            hi_temp1 = hi_temp1, lo_temp1 = lo_temp1, precipitation1 = precipitation1, wind_speed1 = wind_speed1, humidity1 = humidity1, date1 = date1,
                            hi_temp2 = hi_temp2, lo_temp2 = lo_temp2, precipitation2 = precipitation2, wind_speed2 = wind_speed2, humidity2 = humidity2, date2 = date2,
                            hi_temp3 = hi_temp3, lo_temp3 = lo_temp3, precipitation3 = precipitation3, wind_speed3 = wind_speed3, humidity3 = humidity3, date3 = date3,
                            hi_temp4 = hi_temp4, lo_temp4 = lo_temp4, precipitation4 = precipitation4, wind_speed4 = wind_speed4, humidity4 = humidity4, date4 = date4,
                            hi_temp5 = hi_temp5, lo_temp5 = lo_temp5, precipitation5 = precipitation5, wind_speed5 = wind_speed5, humidity5 = humidity5, date5 = date5,
                            hi_temp6 = hi_temp6, lo_temp6 = lo_temp6, precipitation6 = precipitation6, wind_speed6 = wind_speed6, humidity6 = humidity6, date6 = date6,
                            hi_temp7 = hi_temp7, lo_temp7 = lo_temp7, precipitation7 = precipitation7, wind_speed7 = wind_speed7, humidity7 = humidity7, date7 = date7)


# create a main method
if __name__ == "__main__":
    app.run()
