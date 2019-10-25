#! python3

_names = {
   'iv-ff-night'          : '\uf100',
   'iv-ff-day'            : '\uf101',
   'iv-ff-frosty'         : '\uf102',
   'iv-ff-windysnow'      : '\uf103',
   'iv-ff-showers'        : '\uf104',
   'iv-ff-basecloud'      : '\uf105',
   'iv-ff-cloud'          : '\uf106',
   'iv-ff-rainy'          : '\uf107',
   'iv-ff-mist'           : '\uf108',
   'iv-ff-windysnowcloud' : '\uf109',
   'iv-ff-drizzle'        : '\uf10a',
   'iv-ff-snowy'          : '\uf10b',
   'iv-ff-sleet'          : '\uf10c',
   'iv-ff-moon'           : '\uf10d',
   'iv-ff-windyrain'      : '\uf10e',
   'iv-ff-hail'           : '\uf10f',
   'iv-ff-sunset'         : '\uf110',
   'iv-ff-windyraincloud' : '\uf111',
   'iv-ff-sunrise'        : '\uf112',
   'iv-ff-sun'            : '\uf113',
   'iv-ff-thunder'        : '\uf114',
   'iv-ff-windy'          : '\uf115',
}



"""
clear-day     sun
clear-night   moon
cloudy        cloud
cloudy-day    cloud + day
cloudy-night  cloud + night
drizzle       basecloud + drizzle
drizzle-day   basecloud + drizzle + day
drizzle-night 
"""



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

