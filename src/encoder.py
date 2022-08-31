# || py2img ||
# Encodes python source files/text to images and or saves them to a file.

import numpy as np
from PIL import Image
from os.path import getsize
import base64
import sys
from sys import argv
from . import settings

def encode_debug(dbg):
    if settings.debug:
        print(dbg)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def encode_loadfile(file):
    with open(file, "rb") as f:
        data = f.read()
    while (len(base64.b64encode(data))) % 3 != 0:
        data += b'\0'
    beflen = len(data)
    data = base64.b64encode(data)
    encode_debug(f"py2png [INFO] Sucessfully base64 encoded data (+ {len(data) - beflen} bytes)")
    return data

def encode_data2array(data, img_mode = 'RGB'):
    shp = np.array(Image.new(img_mode, (1,1))).shape
    channels = 1 if len(shp)==2 else shp[-1]

    img_bytes = list(map(lambda b: [b[i] for i in range(channels)], chunks(data, channels)))
    size = len(img_bytes)
    sqrtf = np.sqrt(size)
    sqrt  = int(np.ceil(sqrtf))
    sqrt_h = sqrt
    sqrt_w = sqrt
    if (sqrt_h * sqrt_w) > size:
        if ((sqrt_h - 1) * sqrt_w) >= size:
          sqrt_h -= 1
          encode_debug("py2png [INFO] Last row is empty, removed!")
    bb = [sqrt_h, sqrt_w]
    if channels > 1:
      bb.append(channels)
    n_arr = np.zeros(tuple(bb), dtype=np.uint8)

    encode_debug(f"py2png [DEBUG] Copying {size} bytes to image")
    for i in range(0, size):
        dat = img_bytes[i]
        if channels == 1:
            n_arr[i // sqrt, i % sqrt] = dat[0]
        else:
            for c in range(channels):
                n_arr[i // sqrt, i % sqrt, c] = dat[c]

    return n_arr

def encode_savefile(file, out='out.png', img_mode = 'RGB'):
    data = encode_loadfile(file)
    n_arr = encode_data2array(data, img_mode)
    img = Image.fromarray(n_arr)
    extension = '.' + out.split('.')[-1]
    out = '.'.join(out.split('.')[:-1])
    img.save(out + extension)
    imsz = getsize(out + extension)
    pysz = len(data)

    if settings.debug: print("py2png [SUCESS]",imsz, 'bytes written! (', end='')
    if imsz > pysz:
        encode_debug(f'+ {imsz-pysz} bytes)')
    else:
        encode_debug(f'- {pysz-imsz} bytes)')

def main():
    global argv
    argv = argv[1:]
    if len(argv) < 1:
        print("Usage: <file> [<out>] [<colormode>]")
        return 1
    file = argv[0]
    output = 'out.png'
    img_mode = 'RGB'
    if len(argv) == 2:
        output = argv[1]
    if len(argv) == 3:
        img_mode = argv[2]

    print("Converting file \"{}\" with colormode {} to file \"{}\".".format(file, img_mode, output))
    encode_savefile(file, output, img_mode)
    return 0
if __name__ == '__main__':
    sys.exit(main())