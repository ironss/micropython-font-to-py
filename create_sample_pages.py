#! python3

"""
Generate sample pages
"""

import os
import importlib
import PIL.Image
import PIL.ImageDraw


def draw_text(draw, pos, text, font, scale):
    x0 = pos[0]
    y0 = pos[1] - font.height()

    for ch in text:
        ch_bitmap, ch_height, ch_width = font.get_ch(ch)
        
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
                draw.rectangle([((x0+x)*scale[0], (y0+y)*scale[1]), ((x0+x+1)*scale[0], (y0+y+1)*scale[1])], pxl, pxl, 0)
#            print()
            o += '\n'
#        print(o)
        x0 += ch_width


if __name__ == '__main__':
    import pages_1 as pages

    fonts = {}
    for title, page in pages.pages.items():
        for field in page['fields']:
            font = field[2]
            fonts[font] = True

    font_modulenames = []
    for font in sorted(fonts):
        font_modulenames.append('fonts.' + font)        

    fonts = {
        fmn.rsplit('.', 1)[1] : importlib.import_module(fmn) for fmn in font_modulenames
    }

    for title, page in pages.pages.items():
        page_size = page['size']

        for scale in page['scales']:
            im = PIL.Image.new('1', (page_size[0] * scale[0], page_size[1] * scale[1]), 1)
            draw = PIL.ImageDraw.Draw(im)

            for field in page['fields']:
                pos = field[0]
                text = field[1]
                fontname = field[2]
                font = fonts[fontname]
                draw_text(draw, pos, text, font, scale)

            filename = '{:s}-{:d}x{:d}-{:d}x{:d}'.format(title, page_size[0], page_size[1], scale[0], scale[1])
            try:
                os.mkdir('samples')
            except FileExistsError:
                 pass
            im.save('samples/' + filename + '.png')

