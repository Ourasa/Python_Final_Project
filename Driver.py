from flask import Flask
from flask import render_template
from flask import request

import Retriever

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('startup.html')

@app.route("/todayWeather")
def home_to_today_page():
    Retriever.get_current_weather()
    Retriever.get_48hours_temperatures()
    Retriever.get_week_forecast()
    Retriever.get_yesterday_weather()

    return render_template('todayWeather.html')


# create a main method
if __name__ == "__main__":
    app.run()