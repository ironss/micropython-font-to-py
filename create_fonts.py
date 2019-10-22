#! python3

import os
import subprocess

font_specs = [
    # Sans
    ( 'DejaVuSans_{size}.py'                , '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'                , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    ( 'DejaVuSans_Bold_{size}.py'           , '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'           , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    ( 'DejaVuSansCondensed_{size}.py'       , '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf'       , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    ( 'DejaVuSansCondensed_Bold_{size}.py'  , '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'  , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),

    # Serif
    ( 'DejaVuSerif_{size}.py'               , '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'               , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    ( 'DejaVuSerif_Bold_{size}.py'          , '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'          , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    ( 'DejaVuSerifCondensed_{size}.py'      , '/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf'      , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    ( 'DejaVuSerifCondensed_Bold_{size}.py' , '/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf' , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),

    # Mono
    ( 'DejaVuSansMono_{size}.py'            , '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'            , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    ( 'DejaVuSansMono_Bold_{size}.py'       , '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'       , [ 10, 12, 16, 20, 24, 32, 40 ], 'extended.charset' ),
    
    # WeatherIcons
    ( 'WeatherIcons_{size}.py'              , '/home/ironsst/Downloads/weathericons-regular-webfont.ttf'       , [ 10, 12, 16, 20, 24, 32, 40 ], 'weathericons.charset' ),
]

opath = 'fonts'
os.mkdir(opath)

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

