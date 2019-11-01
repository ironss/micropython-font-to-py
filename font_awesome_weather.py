#! python3

# Font Awesome 5 Weather symbols

_names_free = {
   # Free
   "fa-bolt"                : "\uf0e7",
   "fa-cloud"               : "\uf0c2",
   "fa-cloud-meatball"      : "\uf73b",
   "fa-cloud-moon"          : "\uf6c3",
   "fa-cloud-moon-rain"     : "\uf73c",
   "fa-cloud-rain"          : "\uf73d",
   "fa-cloud-showers-heavy" : "\uf740",
   "fa-cloud-sun"           : "\uf6c4",
   "fa-cloud-sun-rain"      : "\uf743",
   "fa-meteor"              : "\uf753",
   "fa-moon"                : "\uf186",
   "fa-poo-storm"           : "\uf75a",
   "fa-rainbow"             : "\uf75b",
   "fa-smog"                : "\uf75f",
   "fa-snowflake"           : "\uf2dc",
   "fa-sun"                 : "\uf185",
   "fa-temperature-high"    : "\uf769",
   "fa-temperature-low"     : "\uf76b",
   "fa-umbrella"            : "\uf0e9",
   "fa-water"               : "\uf773",
   "fa-wind"                : "\uf72e",
}

_names_pro = {   
   # Pro
   "fa-cloud-drizzle"       : "\uf738",
   "fa-cloud-hail"          : "\uf739",
   "fa-cloud-hail-mixed"    : "\uf73a",
   "fa-cloud-rainbow"       : "\uf73e",
   "fa-cloud-showers"       : "\uf73f",
   "fa-cloud-sleet"         : "\uf741",
   "fa-cloud-snow"          : "\uf742",
   "fa-clouds"              : "\uf744",
   "fa-clouds-moon"         : "\uf745",
   "fa-clouds-sun"          : "\uf746",
   "fa-dewpoint"            : "\uf748",
   "fa-eclipse"             : "\uf749",
   "fa-eclipse-alt"         : "\uf74a",
   "fa-fire-smoke"          : "\uf74b",
   "fa-fog"                 : "\uf74e",
   "fa-house-flood"         : "\uf74f",
   "fa-humidity"            : "\uf750",
   "fa-hurricane"           : "\uf751",
   "fa-moon-cloud"          : "\uf754",
   "fa-moon-stars"          : "\uf755",
   "fa-raindrops"           : "\uf75c",
   "fa-smoke"               : "\uf760",
   "fa-snow-blowing"        : "\uf761",
   "fa-snowflakes"          : "\uf7cf",
   "fa-sparkles"            : "\uf890",
   "fa-stars"               : "\uf762",
   "fa-sun-cloud"           : "\uf763",
   "fa-sun-dust"            : "\uf764",
   "fa-sun-haze"            : "\uf765",
   "fa-sunrise"             : "\uf766",
   "fa-sunset"              : "\uf767",
   "fa-temperature-frigid"  : "\uf768",
   "fa-temperature-hot"     : "\uf76a",
   "fa-thunderstorm"        : "\uf76c",
   "fa-thunderstorm-moon"   : "\uf76d",
   "fa-thunderstorm-sun"    : "\uf76e",
   "fa-tornado"             : "\uf76f",
   "fa-volcano"             : "\uf770",
   "fa-water-lower"         : "\uf774",
   "fa-water-rise"          : "\uf775",
   "fa-wind-warning"        : "\uf776",
   "fa-windsock"            : "\uf777",
}

_names = { 
    **_names_free,
#    **_names_pro,
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

