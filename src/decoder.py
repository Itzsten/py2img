# || py2img ||
# Decodes and or executes images created by py2img.

from PIL import Image
import numpy as np
import base64
from sys import argv
import sys
from . import settings

def decode_img(img):
	bobj = base64.b64decode(np.array(img).tobytes()).replace(b'\0',b'')
	return bobj.decode('utf').replace('\r', '')

def decode_file(target_file):
	return decode_img(Image.open(target_file))

def decode_compile_img(img, name="py2png result"):
	return compile(decode_img(img), name, "exec")

def decode_execute_img(img, globals=None):
	if globals == None:
		globals = {'__name__': '__main__'}
	else:
		globals = globals.copy()
	bytecode = decode_compile_img(img)
	exec(bytecode, globals, globals)

def decode_execute_file(file, globals=None):
	decode_execute_img(Image.open(file), globals)


def main():
	global argv
	argv = argv[1:]
	if len(argv) < 1:
		print("Usage: <file> [<view>]")
		return 1
	file = argv[0]
	if len(argv) == 2:
		if argv[1] == 'view':
			print(decode_file(file).encode('utf8'))
			return 0

	print("Executing file \"" + file + "\"")
	decode_execute_file(file)
	return 0
argv = ['out.png']
if __name__ == '__main__':
	sys.exit(main())