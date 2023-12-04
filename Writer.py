import os


def update_current_weather_file(cur_temp, apparent_temp, precip, wind_speeds, humidity, dt, condition): 
    if data_file_exists('current_weather.txt'): 
        os.remove(os.path.join('data','current_weather.txt'))

    try:
        file = open(os.path.join('data','current_weather.txt'), 'w')
        file.write('CTemp\tApTemp\tPrecip\tWndSpd\tHmdity\tDate\tCondition\n')
        
        data = (convert_num_to_2d(cur_temp), convert_num_to_2d(apparent_temp), 
                convert_num_to_2d(precip), convert_num_to_2d(wind_speeds), convert_num_to_2d(humidity), str(dt), condition)
        data_string = '\t'.join(data)
        
        file.write(data_string)
        file.close()

        print("Today's current data successfully written")
    except Exception: 
        print('Something went wrong trying to update current_weather.txt')
    


def update_yesterday_weather_file(temp_high, temp_low, precip, wind_speeds, humidity, dt): 
    if data_file_exists('yesterday_weather.txt'): 
        os.remove(os.path.join('data','yesterday_weather.txt'))

    try:
        file = open(os.path.join('data','yesterday_weather.txt'), 'w')
        file.write('HiTmp\tLoTmp\tPrecip\tWndSpd\tHmdity\tDate\n')

        data = (convert_num_to_2d(temp_high), convert_num_to_2d(temp_low), convert_num_to_2d(precip),
                convert_num_to_2d(wind_speeds), convert_num_to_2d(humidity), str(dt))
        data_string = '\t'.join(data)
        
        file.write(data_string)
        file.close()
        print('Yesterday data successfully written')

    except Exception: 
        print('Something went wrong trying to update yesterday_weather.txt')

def update_forecast_weather_file(output): 
    if data_file_exists('forecast_weather.txt'): 
        os.remove(os.path.join('data','forecast_weather.txt'))
    try:
        file = open(os.path.join('data','forecast_weather.txt'), 'w')
        file.write('HiTmp\tLoTmp\tPrecip\tWndSpd\tHmdity\tDate\tCondition\n')

        data_string = ''

        for day in output: 
            day_data = ''
            temp_list = []

            for data in day: 
                try:
                    temp_list.append(convert_num_to_2d(data))
                except: 
                    temp_list.append(str(data))

            day_data = '\t'.join(temp_list) + "\n"
            data_string = data_string + day_data

        
        file.write(data_string)
        file.close()
        print('Week forecast data successfully written')
    except Exception: 
        print('Something went wrong trying to update forecast_weather.txt')


def update_48hours_temp_file(dt ,output): 
    if data_file_exists('48hours_temp.txt'): 
        os.remove(os.path.join('data','48hours_temp.txt'))

    try:
        file = open(os.path.join('data','48hours_temp.txt'), 'w')
        file.write('Time & Date Data obtained: '+ str(dt) + '\n')
        file.write('Hr\tTmp\n')

        data_string = ''

        for i in range(0, 49): 
            temp_list = [str(i-24)]
            temp_list.append(str(output[i]))
            
            hour_data = '\t'.join(temp_list) + "\n"
            data_string = data_string + hour_data
        
        #print(data_string)

        file.write(data_string)
        file.close()
        print('48 hour data successfully written')
    except Exception: 
        print('Something went wrong trying to update forecast_weather.txt')




def data_file_exists(file_name):
    path = os.path.join('data', file_name)
    return os.path.isfile(path)



def convert_num_to_2d(number):
    return "{:.2f}".format(number)