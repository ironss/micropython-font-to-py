#! python3

import os
import subprocess

sizes = [ 
    10,
    12,
    16,
    20,
    24,
    32,
    40,
]

font_specs = [
    # DejaVu Sans
    ( 'DejaVuSans_{size}.py'                  , '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'                , sizes, 'charsets/combined.charset' ),
    ( 'DejaVuSans_Bold_{size}.py'             , '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'           , sizes, 'charsets/combined.charset' ),
#    ( 'DejaVuSansCondensed_{size}.py'         , '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf'       , sizes, 'charsets/combined.charset' ),
#    ( 'DejaVuSansCondensed_Bold_{size}.py'    , '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'  , sizes, 'charsets/combined.charset' ),

    # DejaVu Serif
#    ( 'DejaVuSerif_{size}.py'                 , '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'               , sizes, 'charsets/combined.charset' ),
#    ( 'DejaVuSerif_Bold_{size}.py'            , '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'          , sizes, 'charsets/combined.charset' ),
#    ( 'DejaVuSerifCondensed_{size}.py'        , '/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf'      , sizes, 'charsets/combined.charset' ),
#    ( 'DejaVuSerifCondensed_Bold_{size}.py'   , '/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf' , sizes, 'charsets/combined.charset' ),

    # DejaVu Sans Mono
#    ( 'DejaVuSansMono_{size}.py'              , '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'            , sizes, 'charsets/combined.charset' ),
#    ( 'DejaVuSansMono_Bold_{size}.py'         , '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'       , sizes, 'charsets/combined.charset' ),
    
    # Freefont Sans
#    ( 'FreeSans_{size}.py'                    , '/usr/share/fonts/truetype/freefont/FreeSans.ttf'                , sizes, 'charsets/combined.charset' ),
#    ( 'FreeSansBold_{size}.py'               , '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'           , sizes, 'charsets/combined.charset' ),

    # IBM Plex Sans
#    ( 'IBMPlexSans_Regular_{size}.py'         , 'ttf/IBMPlexSans-Regular.ttf'                , sizes, 'charsets/combined.charset' ),
#    ( 'IBMPlexSans_Bold_{size}.py'            , 'ttf/IBMPlexSans-Bold.ttf'           , sizes, 'charsets/combined.charset' ),
#    ( 'IBMPlexSansCondensed_Regular_{size}.py'         , 'ttf/IBMPlexSansCondensed-Regular.ttf'                , sizes, 'charsets/combined.charset' ),
#    ( 'IBMPlexSansCondensed_Bold_{size}.py'            , 'ttf/IBMPlexSansCondensed-Bold.ttf'           , sizes, 'charsets/combined.charset' ),

    # Droid Sans Fallback
#    ( 'DroidSansFallback_{size}.py'           , '/usr/share/fonts-droid-fallback/truetype/DroidSansFallback.ttf'                , sizes, 'charsets/combined.charset' ),


    # Symbola
    ( 'Symbola_{size}.py'                     , 'ttf/Symbola.ttf'                , sizes, 'charsets/combined.charset' ),
#    ( 'Symbola_hint_{size}.py'                , 'ttf/Symbola_hint.ttf'                , sizes, 'charsets/combined.charset' ),

    # Tahoma
    ( 'Tahoma_{size}.py'                      , 'ttf/Tahoma.ttf'                , sizes, 'charsets/combined.charset' ),
    ( 'Tahoma_Bold_{size}.py'                 , 'ttf/Tahoma Bold.ttf'                , sizes, 'charsets/combined.charset' ),

    # Verdana
#    ( 'Verdana_{size}.py'                     , 'ttf/Verdana.ttf'                , sizes, 'charsets/combined.charset' ),
#    ( 'Verdana_Bold_{size}.py'                , 'ttf/Verdana Bold.ttf'                , sizes, 'charsets/combined.charset' ),

    # WeatherIcons
    ( 'WeatherIcons_{size}.py'                , 'ttf/weathericons-regular-webfont.ttf'       , sizes, 'charsets/weathericons.charset' ),

    # Pixeden Icon Set Weather
    ( 'PE_Icon_Set_Weather_{size}.py'         , 'ttf/pe-icon-set-weather.ttf'       , sizes, 'charsets/pe_icon_set_weather.charset' ),

    # Meteocons
#    ( 'Meteocons_{size}.py'                   , 'ttf/meteocons.ttf'       , sizes, 'charsets/meteocons.charset' ),

    # Iconvault ForecastFont elements
#    ( 'Iconvault_ForecastFont_parts_{size}.py', 'ttf/iconvault_forecastfont.ttf'       , sizes, 'charsets/iconvault_forecastfont_parts.charset' ),

    # Font Awesome (free) - weather iconss only
    ( 'Font_Awesome_weather_{size}.py', 'ttf/fa-solid-900.ttf'       , sizes, 'charsets/font_awesome_weather.charset' ),
]

opath = 'fonts'
try:
    os.mkdir(opath)
except FileExistsError:
    pass

for font_spec in font_specs:
    ffmt = font_spec[0]
    ffile = font_spec[1]
    fsizes = font_spec[2]
    charset_file = font_spec[3]
    
    for fs in fsizes:
        ofn = opath + '/' + ffmt.format(size=fs)
        print(ffile, fs, ofn)
        proc = subprocess.run(
            [
                '.venv/bin/python', 
                'font_to_py.py',
                '-k', charset_file,
                '-v',
                ffile,
                str(fs),
                ofn,
            ],
        )

