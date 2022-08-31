# || py2img ||
# Initializes all functions

from . import decoder as _decoder
from . import encoder as _encoder
import base64
from PIL import Image
from os.path import getsize
from . import settings

settings.init()

def set_debug(value):
    global debug
    debug = value

class encode:
    def from_file(file: str, output: str = 'out.png', img_mode: str = 'RGB'):
        _encoder.encode_savefile(file, output, img_mode)
    def from_file_to_PIL(file: str, img_mode: str = 'RGB'):
        data = _encoder.encode_loadfile(file)
        n_arr = _encoder.encode_data2array(data, img_mode)
        return Image.fromarray(n_arr)
    def from_file_to_numpy(file: str, img_mode: str = 'RGB'):
        data = _encoder.encode_loadfile(file)
        return _encoder.encode_data2array(data, img_mode)
    def from_str(data: str, output: str = 'out.png', img_mode: str = 'RGB'):
        data = data.encode('utf8')
        while (len(base64.b64encode(data))) % 3 != 0:
            data += b'\0'
        beflen = len(data)
        data = base64.b64encode(data)
        n_arr = _encoder.encode_data2array(data, img_mode)
        img = Image.fromarray(n_arr)
        extension = '.' + output.split('.')[-1]
        output = '.'.join(output.split('.')[:-1])
        img.save(output + extension)
        imsz = getsize(output + extension)
        pysz = len(data)

        if debug: print("py2png [SUCESS]",imsz, 'bytes written! (', end='')
        if imsz > pysz:
            _encoder.encode_debug(f'+ {imsz-pysz} bytes)')
        else:
            encode_debug(f'- {pysz-imsz} bytes)')
    def from_str_to_PIL(data: str, output: str = 'out.png', img_mode: str = 'RGB'):
        data = data.encode('utf8')
        while (len(base64.b64encode(data))) % 3 != 0: data += b'\0'
        beflen = len(data)
        data = base64.b64encode(data)
        n_arr = _encoder.encode_data2array(data, img_mode)
        return Image.fromarray(n_arr)
    def from_str_to_numpy(data: str, output: str = 'out.png', img_mode: str = 'RGB'):
        data = data.encode('utf8')
        while (len(base64.b64encode(data))) % 3 != 0: data += b'\0'
        beflen = len(data)
        data = base64.b64encode(data)
        return _encoder.encode_data2array(data, img_mode)

class decode:
    def PIL(img):
        return _decoder.decode_img(img)
    def numpy(img):
        return _decoder.decode_img(Image.fromarray(img))
    def file(target_img):
        return _decoder.decode_file(target_img)
    def exec(target_img, globals=None):
        if type(target_img) == str:
            _decoder.decode_execute_file(target_img, globals)
        else:
            _decoder.decode_execute_img(target_img, globals)