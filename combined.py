#! python3

# Interesting characters
#    ASCII
#    'Engineering' symbols such as ohm sign, micro sign, degree sign, etc
#    ISO8859-1, -15
#    CP-437, including range 01--1F
#    IBM-1038, with lots of mathematical symbols, Greek letters, etc
#    ballot-check, ballot-cross, etc
#    media symbols
#
# Note that a single font usually does not include the entire character
# set. Either combine fonts when generating the bitmaps, or combine fonts
# when displaying the symbols
#
# Bigger charset leads to bigger bitmap fonts
# * DejaVuSans  16  ascii      96  10K
# * DejaVuSans  16  iso8859-1 190  20K
# * DejaVuSans  16  cp437     253  26K
# * DejaVuSans  16  specials   45   7K
# * DejaVuSans  16  a+i+c+s   325  34K
# * DejaVuSans  16  all       431  45K
#
# Bigger font size gives bigger bitmap fonts
# * DejaVuSans  12  a+i+c+s   325   27K
# * DejaVuSans  16  a+i+c+s   325   34K
# * DejaVuSans  20  a+i+c+s   325   54K
# * DejaVuSans  24  a+i+c+s   325   65K
# * DejaVuSans  32  a+i+c+s   325  135K
# * Symbola     20  a+i+c+s   325   61K
# * Symbola     24  a+i+c+s   325   97K
# * Symbola     32  a+i+c+s   325  135K
# * Symbola     40  a+i+c+s   325  250K

import unicodedata

ascii_charset = [
    bytes((b,)).decode('ascii') for b in range(0, 128)
]


iso8859_1_charset = [
    bytes((b,)).decode('iso8859-1') for b in range(0, 256) 
]
 
cp437_charset = [
    bytes((b,)).decode('cp437') for b in range(0, 256) 
] + [
# Python decodes CP437 00--1F as themselves, rather than these symbols
    '\u2302',
    '\u263A',
    '\u263B',
    '\u2665',
    '\u2666',
    '\u2663',
    '\u2660',
    '\u2022',
    '\u25DB',
    '\u25CB',
    '\u25D9',
    '\u2642',
    '\u2640',
    '\u266A',
    '\u266B',
    '\u263C',
    '\u25BA',
    '\u25C4',
    '\u2195',
    '\u203C',
    '\u00B5',
    '\u00A7',
    '\u25AC',
    '\u21A8',
    '\u2191',
    '\u2193',
    '\u2192',
    '\u2190',
    '\u221F',
    '\u25B2',
    '\u25BC',

# Python decodes xx as itself, rather than this symbol
    '\u2302',
]

ibm1038_charset = [
    '\u2200',
    '\u2203',
    '\u220D',
    '\u2212',

    '\u2245',
    '\u0391',
    '\u0392',
    '\u03A7',
    '\u0394',
    '\u0395',
    '\u03A6',
    '\u0393',
    '\u0397',
    '\u0399',
    '\u03D1',
    '\u039B',
    '\u039C',
    '\u039D',
    '\u039E',
    '\u039F',
    
    '\u03A0',
    '\u0398',
    '\u03A1',
    '\u03A3',
    '\u03A4',
    '\u03A5',
    '\u03C2',
    '\u03A9',
    '\u039E',
    '\u03A8',
    '\u0396',
    '\u2234',
    '\u22A5',
    
#    '\uF8E5',
    '\u03B1',
    '\u03B2',
    '\u03C7',
    '\u03B4',
    '\u03B5',
    '\u03C6',
    '\u03B3',
    '\u03B7',
    '\u03B9',
    '\u03D5',
    '\u03BB',
    '\u03BC',
    '\u03BD',
    '\u03BE',
    '\u03BF',
    
    '\u03C0',
    '\u03B8',
    '\u03C1',
    '\u03C3',
    '\u03C4',
    '\u03C5',
    '\u03D6',
    '\u03C9',
    '\u03BE',
    '\u03C8',
    '\u03B6',
    
    '\u20AC',
    '\u03D2',
    '\u2032',
    '\u2264',
    '\u2044',
    '\u221E',
    '\u0192',
    '\u2663',
    '\u2665',
    '\u2666',
    '\u2660',
    '\u2194',
    '\u2190',
    '\u2191',
    '\u2192',
    '\u2103',
    
    '\u00B0',
    '\u00B1',
    '\u2033',
    '\u2265',
    '\u00D7',
    '\u221D',
    '\u2202',
    '\u2022',
    '\u00F7',
    '\u2260',
    '\u2261',
    '\u2248',
    '\u2026',
    '\u23D0',
    '\u23AF',
    '\u21B2',
    
    '\u2135',
    '\u2111',
    '\u211C',
    '\u2118',
    '\u2297',
    '\u2295',
    '\u2205',
    '\u2229',
    '\u222A',
    '\u2283',
    '\u2287',
    '\u2284',
    '\u2282',
    '\u2286',
    '\u2208',
    '\u2209',
    
    '\u2220',
    '\u2202',
    '\u00AE',
    '\u00A9',
    '\u2122',
    '\u220F',
    '\u221A',
    '\u22C5',
    '\u00AC',
    '\u2226',
    '\u2227',
    '\u21D4',
    '\u21D0',
    '\u21D1',
    '\u21D2',
    '\u21D3',
    
    '\u25CA',
    '\u3008',
    '\u00AE',
    '\u00A9',
    '\u2122',
    '\u2211',
    '\u239B',
    '\u239C',
    '\u239D',
    '\u23A1',
    '\u23A2',
    '\u23A3',
    '\u23A7',
    '\u23A8',
    '\u23A9',
    '\u23AA',
    
#   '\uF8FF',
    '\u3009',
    '\u222B',
    '\u2320',
    '\u23A3',
    '\u2321',
    '\u239E',
    '\u239F',
    '\u23A0',
    '\u23A4',
    '\u23A5',
    '\u23A6',
    '\u23AA',
    '\u23AB',
    '\u23AC',
]

specials = [
        '\N{DEGREE SIGN}',
        '\N{MICRO SIGN}',
        '\N{OHM SIGN}',
        '\N{DIAMETER SIGN}',
        '\N{MULTIPLICATION SIGN}',
        '\N{DIVISION SIGN}',
        '\N{PLUS-MINUS SIGN}',

        '\N{CHECK MARK}',
        '\N{BALLOT X}',
        '\N{BALLOT BOX}'
        '\N{BALLOT BOX WITH CHECK}',
        '\N{BALLOT BOX WITH X}',
        
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
        
        '\N{EJECT SYMBOL}',
        '\N{BLACK RIGHT-POINTING DOUBLE TRIANGLE}',
        '\N{BLACK LEFT-POINTING DOUBLE TRIANGLE}',
        '\N{BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR}',
        '\N{BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR}',
        '\N{BLACK RIGHT-POINTING TRIANGLE WITH DOUBLE VERTICAL BAR}',
        '\N{BLACK MEDIUM LEFT-POINTING TRIANGLE}',
        '\N{BLACK MEDIUM RIGHT-POINTING TRIANGLE}',
        '\N{DOUBLE VERTICAL BAR}',
        '\N{BLACK SQUARE FOR STOP}',
        '\N{BLACK CIRCLE FOR RECORD}',
        '\N{POWER SYMBOL}',
        '\N{POWER ON-OFF SYMBOL}',
        '\N{POWER ON SYMBOL}',
]


lookup = unicodedata.lookup
name = unicodedata.name

charset = sorted(c for c in set(
    []
    + ascii_charset
    + iso8859_1_charset
    + cp437_charset
    + ibm1038_charset
    + specials
) if c.isprintable())

if __name__ == '__main__':
    text = ''.join(charset)
    print(text)

