from odoo import models, fields

class Weather(models.Model):
    _name = 'weather.weather'

    city = fields.Char(string='City')
    duration = fields.Integer(string='Duration')
    weather_data = fields.Text(string='Weather Data')