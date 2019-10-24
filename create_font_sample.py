"""
Generate font samples

"""

import os
import importlib
import PIL.Image
import PIL.ImageDraw

font_filenames = [
    'fonts/DejaVuSans_10.py',
    'fonts/DejaVuSans_12.py',
    'fonts/DejaVuSans_16.py',
    'fonts/DejaVuSans_20.py',
    'fonts/DejaVuSans_24.py',
    'fonts/DejaVuSans_32.py',
    'fonts/DejaVuSans_40.py',

    'fonts/DejaVuSans_Bold_10.py',
    'fonts/DejaVuSans_Bold_12.py',
    'fonts/DejaVuSans_Bold_16.py',
    'fonts/DejaVuSans_Bold_20.py',
    'fonts/DejaVuSans_Bold_24.py',
    'fonts/DejaVuSans_Bold_32.py',
    'fonts/DejaVuSans_Bold_40.py',
    
    'fonts/WeatherIcons_10.py',
    'fonts/WeatherIcons_12.py',
    'fonts/WeatherIcons_16.py',
    'fonts/WeatherIcons_20.py',
    'fonts/WeatherIcons_24.py',
    'fonts/WeatherIcons_32.py',
    'fonts/WeatherIcons_40.py',
]

font_modulenames = [ 
    os.path.splitext(ffn)[0].replace('/', '.') for ffn in font_filenames 
]

fonts = {
    fmn.rsplit('.', 1)[1] : importlib.import_module(fmn) for fmn in font_modulenames
}

def create_text_sample(text, font, px_size):
    text_width = 0
    for ch in text:
        text_width += font.get_ch(ch)[2]
    text_height = font.height()
    im = PIL.Image.new('1', (text_width * px_size[0], text_height * px_size[1]), 1)
    draw = PIL.ImageDraw.Draw(im)

    ch_x_offset = 0
    for ch in text:
#        print('{c:5d} {c:04X} {ch:s}'.format(c=ord(ch), ch=ch))
        ch_bitmap, ch_height, ch_width = font.get_ch(ch)
#        print(ch_x_offset)
        
        o = ''
        for y in range(ch_height):
            for x in range(ch_width):
                bmp_byten, bmp_bitn = divmod(y, 8)
                bmp_byten += x * (((ch_height-1) // 8)+1)
                bmp_byte = ch_bitmap[bmp_byten]
                bmp_bit = (bmp_byte >> bmp_bitn) & 0x01
                pxl = not bmp_bit
                txl = '#' if bmp_bit else '.'
#                print(bmp_byten, bmp_bitn, txl)
                o += txl
                draw.rectangle([((ch_x_offset + x)*px_size[0], y*px_size[1]), ((ch_x_offset + x + 1)*px_size[0], (y+1)*px_size[1])], pxl, pxl, 0)
#            print()
            o += '\n'
#        print(o)
        ch_x_offset += ch_width
    return im, o

texts = [
    'The quick brown fox jumps over the lazy dog',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'abcdefghijklmnopqrstuvwxyz',
    ''.join(chr(c) for c in range(32, 127)),
    ''.join(chr(c) for c in range(128, 256)),
]

text = texts[4]

for fn in sorted(fonts):
    font = fonts[fn]
    
    # Find all characters in the font
    text = ''.join(chr(font.ifb(font._mvsp[m:])) for m in range(0, len(font._mvsp), 4))
    
    im, txt = create_text_sample(text, font, (1, 1))
    im2, txt2 = create_text_sample(text, font, (4, 4))

#    im.show()
    im.save('samples/' + fn + '-sample-' + '1' + '.pdf')
    im2.save('samples/' + fn + '-sample-' + '2' + '.pdf')

