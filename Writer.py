import os


def update_current_weather_file(cur_temp, apparent_temp, precip, humidity, dt, alerts): 
    if data_file_exists('current_weather.txt'): 
        os.remove(os.path.join('data','current_weather.txt'))

    try:
        file = open(os.path.join('data','current_weather.txt'), 'w')
        file.write('CTemp\tApTemp\tPrecip\tHmdity\tDate\t\tAlerts\n')
        
        data = (convert_num_to_2d(cur_temp), convert_num_to_2d(apparent_temp), 
                convert_num_to_2d(precip), convert_num_to_2d(humidity), str(dt), str(alerts))
        data_string = '\t'.join(data)
        
        file.write(data_string)
        file.close()

    except Exception: 
        print('Something went wrong trying to update current_weather.txt')
    


def update_yesterday_weather_file(temp_high, temp_low, precip, humidity, dt): 
    if data_file_exists('yesterday_weather.txt'): 
        os.remove(os.path.join('data','yesterday_weather.txt'))

    try:
        file = open(os.path.join('data','yesterday_weather.txt'), 'w')
        file.write('HiTmp\tLoTmp\tPrecip\tHmdity\tDate\n')

        data = (convert_num_to_2d(temp_high), convert_num_to_2d(temp_low), 
                convert_num_to_2d(precip), convert_num_to_2d(humidity), str(dt))
        data_string = '\t'.join(data)
        
        file.write(data_string)
        file.close()

    except Exception: 
        print('Something went wrong trying to update yesterday_weather.txt')

def update_forecast_weather_file(output): 
    if data_file_exists('forecast_weather.txt'): 
        os.remove(os.path.join('data','forecast_weather.txt'))
    try:
        file = open(os.path.join('data','forecast_weather.txt'), 'w')
        file.write('HiTmp\tLoTmp\tPrecip\tHmdity\tDate\n')

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

    except Exception: 
        print('Something went wrong trying to update forecast_weather.txt')


def data_file_exists(file_name):
    path = os.path.join('data', file_name)
    return os.path.isfile(path)



def convert_num_to_2d(number):
    return "{:.2f}".format(number)