import weathericons
wi_day = weathericons.lookup(['wi-day-sunny', 'wi-day-sunny-overcast', 'wi-day-cloudy', 'wi-day-showers', 'wi-day-rain', 'wi-day-sleet', 'wi-day-hail', 'wi-day-snow'])

import pe_icon_set_weather
pe_day = pe_icon_set_weather.lookup(['pe-is-w-sun-1', 'pe-is-w-partly-cloudy-1', 'pe-is-w-mostly-cloudy-1', 'pe-is-w-rain-1', 'pe-is-w-rain-and-snow', 'pe-is-w-hail-day-1', 'pe-is-w-snow-day-1'])

import meteocons
meteocons_day = meteocons.lookup(['meteo-sun', 'meteo-cloud-sun', 'meteo-clouds', 'meteo-cloud-rain-1', 'meteo-cloud-rain-2', 'meteo-cloud-snow-4', 'meteo-cloud-snow-1'])

import iconvault_forecastfont
iv_ff_parts = iconvault_forecastfont.lookup(['iv-ff-sun', 'iv-ff-cloud', 'iv-ff-windysnowcloud', 'iv-ff-windyraincloud', 'iv-ff-mist', 'iv-ff-rainy', 'iv-ff-windyrain'])



pages = {
    "Screen_1" : {
        'size': (320, 240),
        'fields': [
            ((0, 30),   "Big text",    'DejaVuSans_24'),
            ((0, 55),  "Medium text", 'DejaVuSans_20'),
            ((0, 75), "Small text",  'DejaVuSans_16'),
            ((0, 100), wi_day, 'WeatherIcons_20'),
            ((0, 140), wi_day, 'WeatherIcons_32'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "WeatherIcons" : {
        'size': (320, 240),
        'fields': [
            ((0,  20), wi_day, 'WeatherIcons_20'),
            ((0,  60), wi_day, 'WeatherIcons_32'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "PE_Icon_Set_Weather" : {
        'size': (320, 240),
        'fields': [
            ((0,  20), pe_day, 'PE_Icon_Set_Weather_20'),
            ((0,  60), pe_day, 'PE_Icon_Set_Weather_32'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "Meteocons" : {
        'size': (320, 240),
        'fields': [
            ((0,  20), meteocons_day, 'Meteocons_20'),
            ((0,  60), meteocons_day, 'Meteocons_32'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "Iconvault ForecastFont" : {
        'size': (320, 240),
        'fields': [
            ((0,  20), iv_ff_parts, 'Iconvault_ForecastFont_parts_20'),
            ((0,  60), iv_ff_parts, 'Iconvault_ForecastFont_parts_32'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
}

