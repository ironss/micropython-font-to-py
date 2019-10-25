#! python3

import unicodedata

ascii_charset = [
    bytes((b,)).decode('ascii') for b in range(0, 128)
]


iso8859_1_charset = [
    bytes((b,)).decode('iso8859-1') for b in range(0, 256) 
]
 
cp437_charset = [
    bytes((b,)).decode('cp437') for b in range(0, 256) 
]

specials = [
        '\N{DEGREE SIGN}',
        '\N{MICRO SIGN}',
        '\N{OHM SIGN}',
        '\N{DIAMETER SIGN}',
        '\N{MULTIPLICATION SIGN}',
        '\N{DIVISION SIGN}',
        '\N{PLUS-MINUS SIGN}',
        
        '\N{EURO SIGN}',
        '\N{POUND SIGN}',
        '\N{YEN SIGN}',
        
        '\N{BULLET}',
        '\N{REFERENCE MARK}',
        '\N{SECTION SIGN}',
        '\N{COPYRIGHT SIGN}',
        '\N{REGISTERED SIGN}',
        
        '\N{FIGURE DASH}',
        '\N{EM DASH}',
        '\N{EN DASH}',
        '\N{SWUNG DASH}',
        '\N{HORIZONTAL ELLIPSIS}',
        '\N{MIDLINE HORIZONTAL ELLIPSIS}',

        '\N{SINGLE LEFT-POINTING ANGLE QUOTATION MARK}',
        '\N{SINGLE RIGHT-POINTING ANGLE QUOTATION MARK}',
        '\N{LEFT-POINTING DOUBLE ANGLE QUOTATION MARK}',
        '\N{RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK}',
]


lookup = unicodedata.lookup
name = unicodedata.name

charset = sorted(c for c in set(
    ascii_charset +
    iso8859_1_charset + 
    cp437_charset +
    specials
) if c.isprintable())

if __name__ == '__main__':
    text = ''.join(charset)
    print(text)

