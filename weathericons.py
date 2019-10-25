#! python3

_names = {
   'wi-day-cloudy-gusts'        : '\uf000',
   'wi-day-cloudy-windy'        : '\uf001',
   'wi-day-cloudy'              : '\uf002',
   'wi-day-fog'                 : '\uf003',
   'wi-day-hail'                : '\uf004',
   'wi-day-lightning'           : '\uf005',
   'wi-day-rain-mix'            : '\uf006',
   'wi-day-rain-wind'           : '\uf007',
   'wi-day-rain'                : '\uf008',
   'wi-day-showers'             : '\uf009',
   'wi-day-snow'                : '\uf00a',
   'wi-day-sprinkle'            : '\uf00b',
   'wi-day-sunny-overcast'      : '\uf00c',
   'wi-day-sunny'               : '\uf00d',
   'wi-day-storm-showers'       : '\uf00e',
   'wi-day-thunderstorm'        : '\uf010',
   'wi-cloudy-gusts'            : '\uf011',
   'wi-cloudy-windy'            : '\uf012',
   'wi-cloudy'                  : '\uf013',
   'wi-fog'                     : '\uf014',
   'wi-hail'                    : '\uf015',
   'wi-lightning'               : '\uf016',
   'wi-rain-mix'                : '\uf017',
   'wi-rain-wind'               : '\uf018',
   'wi-rain'                    : '\uf019',
   'wi-showers'                 : '\uf01a',
   'wi-snow'                    : '\uf01b',
   'wi-sprinkle'                : '\uf01c',
   'wi-storm-showers'           : '\uf01d',
   'wi-thunderstorm'            : '\uf01e',
   'wi-windy'                   : '\uf021',
   'wi-night-clear'             : '\uf02e',
   'wi-night-cloudy-gusts'      : '\uf02f',
   'wi-night-cloudy-windy'      : '\uf030',
   'wi-night-cloudy'            : '\uf031',
   'wi-night-hail'              : '\uf032',
   'wi-night-lightning'         : '\uf033',
   'wi-night-rain-mix'          : '\uf034',
   'wi-night-rain-wind'         : '\uf035',
   'wi-night-rain'              : '\uf036',
   'wi-night-showers'           : '\uf037',
   'wi-night-snow'              : '\uf038',
   'wi-night-sprinkle'          : '\uf039',
   'wi-night-storm-showers'     : '\uf03a',
   'wi-night-thunderstorm'      : '\uf03b',
   'wi-cloud-down'              : '\uf03d',
   'wi-cloud-refresh'           : '\uf03e',
   'wi-cloud-up'                : '\uf040',
   'wi-cloud'                   : '\uf041',
   'wi-direction-down-left'     : '\uf043',
   'wi-direction-down'          : '\uf044',
   'wi-horizon'                 : '\uf047',
   'wi-direction-left'          : '\uf048',
   'wi-_reserved_'              : '\uf049',
   'wi-night-fog'               : '\uf04a',
   'wi-refresh'                 : '\uf04c',
   'wi-direction-right'         : '\uf04d',
   'wi-sprinkles'               : '\uf04e',
   'wi-strong-wind'             : '\uf050',
   'wi-sunrise'                 : '\uf051',
   'wi-sunset'                  : '\uf052',
   'wi-thermometer-exterior'    : '\uf053',
   'wi-thermometer-internal'    : '\uf054',
   'wi-thermometer'             : '\uf055',
   'wi-tornado'                 : '\uf056',
   'wi-direction-up-right'      : '\uf057',
   'wi-direction-up'            : '\uf058',
   'wi-wind-west'               : '\uf059',
   'wi-wind-south-west'         : '\uf05a',
   'wi-wind-south-east'         : '\uf05b',
   'wi-wind-south'              : '\uf05c',
   'wi-wind-north-west'         : '\uf05d',
   'wi-wind-north-east'         : '\uf05e',
   'wi-wind-north'              : '\uf060',
   'wi-wind-east'               : '\uf061',
   'wi-smoke'                   : '\uf062',
   'wi-dust'                    : '\uf063',
   'wi-snow-wind'               : '\uf064',
   'wi-day-snow-wind'           : '\uf065',
   'wi-night-snow-wind'         : '\uf066',
   'wi-day-sleet-storm'         : '\uf068',
   'wi-night-sleet-storm'       : '\uf069',
   'wi-day-snow-thunderstorm'   : '\uf06b',
   'wi-night-snow-thunderstorm' : '\uf06c',
   'wi-solar-eclipse'           : '\uf06e',
   'wi-lunar-eclipse'           : '\uf070',
   'wi-meteor'                  : '\uf071',
   'wi-hot'                     : '\uf072',
   'wi-hurricane'               : '\uf073',
   'wi-smog'                    : '\uf074',
   'wi-alien'                   : '\uf075',
   'wi-snowflake-cold'          : '\uf076',
   'wi-stars'                   : '\uf077',
   'wi-night-partly-cloudy'     : '\uf083',
   'wi-umbrella'                : '\uf084',
   'wi-day-windy'               : '\uf085',
   'wi-direction-up-left'       : '\uf087',
   'wi-direction-down-right'    : '\uf088',
   'wi-moon-new'                : '\uf095',
   'wi-moon-first-quarter'      : '\uf09c',
   'wi-moon-full'               : '\uf0a3',
   'wi-moon-3rd-quarter'        : '\uf0aa',
   'wi-wind-default'            : '\uf0b1',
   'wi-day-sleet'               : '\uf0b2',
   'wi-night-sleet'             : '\uf0b3',
   'wi-sleet'                   : '\uf0b5',
   'wi-day-haze'                : '\uf0b6',
}

def lookup(data):
    if isinstance(data, str):
        data = [ data ]
    v = ''.join(_names[n] for n in data)
    return v

def name(char):
    for k, v in _names.items():
        if v == char:
            return k
    return None

charset = _names.values()

if __name__ == '__main__':
    text = ''.join(charset)
    print(text)
