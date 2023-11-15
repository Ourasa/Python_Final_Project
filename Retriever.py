import requests
import datetime
import os
import Writer
#import time

# Read API_Key from secret.txt. This method should always be used first to set the global variable with the API_KEY.
def set_API_KEY():
    global API_KEY
    try:
        path = os.path.join('data', 'secret.txt')
        file = open(path)
        API_KEY = file.read()
        file.close()
    except: 
        print('Something went wrong opening/reading the secret file')


# Gets information regarding the current weather and alerts - Author 1
def get_current_weather():
    
    response = requests.get("https://api.pirateweather.net/forecast/"+API_KEY+"/37.338207%2C-121.886330?exclude=minutely%2Chourly%2Cdaily")
    data_json = response.json()

    cur_temp = data_json['currently']['temperature']                # Current Temperature
    apparent_temp = data_json['currently']['apparentTemperature']   # Current Feeling Temperature
    precip = data_json['currently']['precipProbability']       # Current Chance of Precipitation
    humidity = data_json['currently']['humidity']                   # Current Humidity
    dt = datetime.datetime.fromtimestamp(data_json['currently']['time'])    # Date
    alerts = data_json['alerts']

    Writer.update_current_weather_file(cur_temp, apparent_temp, precip, humidity, dt, alerts)
    return (cur_temp, apparent_temp, precip, humidity, dt, alerts)



# Gets information regarding yesterday's weather - Author 1    
def get_yesterday_weather(): 
    response = requests.get("https://api.pirateweather.net/forecast/"+API_KEY+"/37.338207%2C-121.886330%2C-86400?exclude=minutely%2Chourly")
    data_json = response.json()

    temp_high = data_json['daily']['data'][0]['temperatureHigh']            # Highest temperature
    temp_low = data_json['daily']['data'][0]['temperatureLow']              # Lowest temperature
    precip = data_json['daily']['data'][0]['precipProbability']             # Chance of precipitation
    humidity = data_json['daily']['data'][0]['humidity']                    # Humidity
    temp_dt = datetime.datetime.fromtimestamp(data_json['daily']['data'][0]['time']) # Date 
    dt = str(temp_dt.year) + '-'+str(temp_dt.month)+'-'+str(temp_dt.day)
    
    Writer.update_yesterday_weather_file(temp_high, temp_low, precip, humidity, dt)

    return (temp_high, temp_low, precip, humidity, dt)


#Gets information this week's forecast - Author 1
def get_week_forecast(): 
    output = []
    
    for i in range (1, 8): 
        response = requests.get("https://api.pirateweather.net/forecast/"+API_KEY+"/37.338207%2C-121.886330%2C?exclude=minutely%2Chourly%2Calerts")
        data_json = response.json()

        temp_high = data_json['daily']['data'][i]['temperatureHigh']            # Predicted Highest temperature
        temp_low = data_json['daily']['data'][i]['temperatureLow']              # Predicted Lowest temperature
        precip = data_json['daily']['data'][i]['precipProbability']             # Predicted Chance of precipitation
        humidity = data_json['daily']['data'][i]['humidity']                    # Predicted Humidity
        temp_dt = datetime.datetime.fromtimestamp(data_json['daily']['data'][i]['time']) # Date for prediction
        dt = str(temp_dt.year) + '-'+str(temp_dt.month)+'-'+str(temp_dt.day)
        day_data = (temp_high, temp_low, precip, humidity, dt)
        output.append(day_data)
        
    Writer.update_forecast_weather_file(output)

    return output


# --- Starts Running here ---

set_API_KEY()

print('Testing get_current_weather()')
print(get_current_weather())


print('Testing get_yesterday_weather()')
print(get_yesterday_weather())


print('Testing get_week_forecast()')
forecast = get_week_forecast()
for day in forecast:
    print(day)







# --- Irrelevant or older code ---

    # print("Right now (raw form), it is " + str(dt) + ".")
    # print("The temperature is " + str(cur_temp) + "C, but it apparently feels like " + str(apparent_temp) + " C.")
    # print("Today is " + str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year) + ".")

    # print("\nNote that when taking the month, day, and year, they are of the following types:")
    # print('Month: ' + str(type(dt.month))) # Integer
    # print('Day: ' + str(type(dt.day))) # Integer
    # print('Year: ' + str(type(dt.year))) # Integer



# The below does not work, likely due to a problem on the API end (They do not have data for time machine no matter what)
# Get the historic records for the past 1 week(s). It is sorted from oldest to most recent. - Author 1
# def get_weather_history(): 
#     prev_day_const = -86400
#     cur_time = int(time.time())
#     output = []

# 
# Test get_weather_history()
# history = get_weather_history()
# for day in history:
#     print(day)