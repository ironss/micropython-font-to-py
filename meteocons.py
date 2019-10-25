#! python3

_names = {
    'meteo-sun-rise'                    : 'A',
    'meteo-sun'                         : 'B',
    'meteo-moon'                        : 'C',
    'meteo-eclipse'                     : 'D',
    'meteo-haze'                        : 'E',
    'meteo-wind'                        : 'F',
    'meteo-snowflake'                   : 'G',
    'meteo-cloud-sun'                   : 'H',
    'meteo-cloud-moon'                  : 'I',
    'meteo-fog-sun'                     : 'J',
    'meteo-fog-moon'                    : 'K',
    'meteo-fog-cloud'                   : 'L',
    'meteo-fog'                         : 'M',
    'meteo-cloud'                       : 'N',
    'meteo-cloud-lightning-1'           : 'O',
    'meteo-cloud-lightning-2'           : 'P',
    'meteo-cloud-rain-1'                : 'Q',
    'meteo-cloud-rain-2'                : 'R',
    'meteo-cloud-wind'                  : 'S',
    'meteo-cloud-wind-rain'             : 'T',
    'meteo-cloud-snow-1'                : 'U',
    'meteo-cloud-snow-2'                : 'V',
    'meteo-cloud-snow-3'                : 'W',
    'meteo-cloud-snow-4'                : 'X',
    'meteo-clouds'                      : 'Y',
    'meteo-clouds-lightning-1'          : 'Z',
    'meteo-clouds-lightning-2'          : '0',
    
    'meteo-sun-f'                       : '1',
    'meteo-moon-f'                      : '2',
    'meteo-cloud-sun-f'                 : '3',
    'meteo-cloud-moon-f'                : '4',
    'meteo-cloud-f'                     : '5',
    'meteo-cloud-lightning-1-f'         : '6',
    'meteo-cloud-rain-1-f'              : '7',
    'meteo-cloud-rain-2-f'              : '8',
    'meteo-cloud-wind-f'                : '9',
    'meteo-cloud-wind-rain-f'           : '!',
    'meteo-cloud-snow-1-f'              : '"',
    'meteo-cloud-snow-3-f'              : '#',
    'meteo-cloud-snow-4-f'              : '$',
    'meteo-clouds-f'                    : '%',
    'meteo-clouds-lightning-1-f'        : '&',
    
    'meteo-thermometer'                 : '\'',
    'meteo-compass'                     : '(',
    'meteo-na'                          : ')',
    'meteo-centigrade'                  : '*',
    'meteo-farenheit'                   : '+',
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

charset = sorted(_names.values())

if __name__ == '__main__':
    text = ''.join(charset)
    print(text)

