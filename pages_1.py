import weathericons
wi_icons = weathericons.lookup(['wi-day-sunny', 'wi-night-clear', 'wi-day-cloudy', 'wi-night-cloudy', 'wi-cloudy', 'wi-fog', 'wi-rain', 'wi-sleet', 'wi-hail', 'wi-snow', 'wi-thunderstorm', 'wi-strong-wind' ])

import pe_icon_set_weather
pe_icons = pe_icon_set_weather.lookup(['pe-is-w-sun-1', 'pe-is-w-moon-1', 'pe-is-w-partly-cloudy-1', 'pe-is-w-partly-cloudy-2', 'pe-is-w-mostly-cloudy-1', 'pe-is-w-fog-1', 'pe-is-w-rain-1', 'pe-is-w-rain-and-snow', 'pe-is-w-hail-2', 'pe-is-w-snow', 'pe-is-w-thunderstorm', 'pe-is-w-wind' ])

pe_icons_f = pe_icon_set_weather.lookup(['pe-is-w-sun-1-f', 'pe-is-w-moon-1-f', 'pe-is-w-partly-cloudy-1-f', 'pe-is-w-partly-cloudy-2-f', 'pe-is-w-mostly-cloudy-1-f', 'pe-is-w-fog-1-f', 'pe-is-w-rain-1-f', 'pe-is-w-rain-and-snow-f', 'pe-is-w-hail-2-f', 'pe-is-w-snow-f', 'pe-is-w-thunderstorm-f', 'pe-is-w-wind' ])

import meteocons
meteocons_icons = meteocons.lookup(['meteo-sun', 'meteo-moon', 'meteo-cloud-sun', 'meteo-cloud-moon', 'meteo-cloud', 'meteo-fog', 'meteo-cloud-rain-2', 'meteo-cloud-snow-4', 'meteo-cloud-snow-1', 'meteo-cloud-lightning-1', 'meteo-wind' ])

meteocons_icons_f = meteocons.lookup(['meteo-sun-f', 'meteo-moon-f', 'meteo-cloud-sun-f', 'meteo-cloud-moon-f', 'meteo-cloud-f', 'meteo-fog', 'meteo-cloud-rain-2-f', 'meteo-cloud-snow-4-f', 'meteo-cloud-snow-1-f', 'meteo-cloud-lightning-1-f', 'meteo-wind' ])

import iconvault_forecastfont_parts
iv_ff_parts = iconvault_forecastfont_parts.lookup(['iv-ff-sun', 'iv-ff-cloud', 'iv-ff-windysnowcloud', 'iv-ff-windyraincloud', 'iv-ff-mist', 'iv-ff-rainy', 'iv-ff-windyrain'])

import font_awesome_weather
fa_weather_icons = font_awesome_weather.lookup([ 'fa-sun', 'fa-moon', 'fa-cloud-sun', 'fa-cloud-moon', 'fa-cloud', 'fa-smog', 'fa-cloud-rain', 'fa-cloud-showers-heavy', 'fa-snowflake', 'fa-bolt', 'fa-wind' ])


pages = {
    "Screen_1" : {
        'size': (320, 240),
        'fields': [
            ((0,  30),   "Big text",    'DejaVuSans_24'),
            ((0,  55),  "Medium text", 'DejaVuSans_20'),
            ((0,  75), "Small text",  'DejaVuSans_16'),
            ((0, 100), wi_icons, 'WeatherIcons_20'),
            ((0, 130), wi_icons, 'WeatherIcons_24'),
            ((0, 170), wi_icons, 'WeatherIcons_32'),
            ((0, 210), wi_icons, 'WeatherIcons_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "WeatherIcons" : {
        'size': (320, 240),
        'fields': [
            ((0,  18), wi_icons, 'WeatherIcons_16'),
            ((0,  40), wi_icons, 'WeatherIcons_20'),
            ((0,  66), wi_icons, 'WeatherIcons_24'),
            ((0,  98), wi_icons, 'WeatherIcons_32'),
            ((0, 140), wi_icons, 'WeatherIcons_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "PE_Icon_Set_Weather" : {
        'size': (320, 240),
        'fields': [
            ((0,  18), pe_icons, 'PE_Icon_Set_Weather_16'),
            ((0,  40), pe_icons, 'PE_Icon_Set_Weather_20'),
            ((0,  66), pe_icons, 'PE_Icon_Set_Weather_24'),
            ((0,  98), pe_icons, 'PE_Icon_Set_Weather_32'),
            ((0, 140), pe_icons, 'PE_Icon_Set_Weather_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "PE_Icon_Set_Weather filled" : {
        'size': (320, 240),
        'fields': [
            ((0,  18), pe_icons_f, 'PE_Icon_Set_Weather_16'),
            ((0,  40), pe_icons_f, 'PE_Icon_Set_Weather_20'),
            ((0,  66), pe_icons_f, 'PE_Icon_Set_Weather_24'),
            ((0,  98), pe_icons_f, 'PE_Icon_Set_Weather_32'),
            ((0, 140), pe_icons_f, 'PE_Icon_Set_Weather_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "Meteocons" : {
        'size': (320, 240),
        'fields': [
            ((0,  18), meteocons_icons, 'Meteocons_16'),
            ((0,  40), meteocons_icons, 'Meteocons_20'),
            ((0,  66), meteocons_icons, 'Meteocons_24'),
            ((0,  98), meteocons_icons, 'Meteocons_32'),
            ((0, 140), meteocons_icons, 'Meteocons_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "Meteocons filled" : {
        'size': (320, 240),
        'fields': [
            ((0,  18), meteocons_icons_f, 'Meteocons_16'),
            ((0,  40), meteocons_icons_f, 'Meteocons_20'),
            ((0,  66), meteocons_icons_f, 'Meteocons_24'),
            ((0,  98), meteocons_icons_f, 'Meteocons_32'),
            ((0, 140), meteocons_icons_f, 'Meteocons_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "Iconvault ForecastFont parts" : {
        'size': (320, 240),
        'fields': [
            ((0,  18), iv_ff_parts, 'Iconvault_ForecastFont_parts_16'),
            ((0,  40), iv_ff_parts, 'Iconvault_ForecastFont_parts_20'),
            ((0,  66), iv_ff_parts, 'Iconvault_ForecastFont_parts_24'),
            ((0,  98), iv_ff_parts, 'Iconvault_ForecastFont_parts_32'),
            ((0, 140), iv_ff_parts, 'Iconvault_ForecastFont_parts_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    },
    "Font Awesome - weather only" : {
        'size': (320, 240),
        'fields': [
            ((0,  18), fa_weather_icons, 'Font_Awesome_weather_16'),
            ((0,  40), fa_weather_icons, 'Font_Awesome_weather_20'),
            ((0,  66), fa_weather_icons, 'Font_Awesome_weather_24'),
            ((0,  98), fa_weather_icons, 'Font_Awesome_weather_32'),
            ((0, 140), fa_weather_icons, 'Font_Awesome_weather_40'),
        ],
        'scales': [
            (1, 1), #(4, 4),
        ],
    }
}

