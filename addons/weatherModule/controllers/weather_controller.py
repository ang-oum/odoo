'''

import requests
from odoo import http

class WeatherController(http.Controller):
    @http.route('/weather/fetch', type='http', auth='user')
    def fetch_weather(self, city, duration):
        #fetch data from weather API
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY&q={city}&days={duration}')
        data = response.json()

        #create a new record in the weather model with the fetched data
        weather = self.env['weather.weather'].create({
            'city': city,
            'duration': duration
        })


'''