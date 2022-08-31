# py2img
The official GitHub repository for the Python source code to image converter.
## Why use py2img?
py2img features stabile image en- or decoding and aims at converting Python source into pure images while also being able to safely execute them without writing any temporary files or other unneeded cache.
## How does it work?
### decoder
The decoder reads the image colors and converts them to bytes and base64 decodes them which achieves a stronger source code protection rather than storing the source code openly, and optionally executes the code stored in it.
### encoder
The encoder is a bit more complicated compared to the decoder, it first of all calculates necessary height and width for a square, optionally removing the last row if empty to achieve a comfortably read image. It then converts the data inputted to bytes and base64 encodes it to not store source openly as described before, to then copy the char codes to the image. Due to the base64 encoding UTF8 characters may be safely stored without losing data. Notice that UTF16 characters are not recommended. After copying data it optionally saves the image or returns a PIL/numpy object based on the function called.

## Examples
### Converting a Python Source file into an image
##### foo.py
```py
print("Hello world from the image side!")
```

##### main.py
```py
import py2img
py2img.encode.from_file("foo.py", output="bar.png")
```
Run main.py, and you should have an image saved like this:<br>
![foo.py as an image](https://i.imgur.com/c9c1W9J.png)
<br>Congrats! You have now converted your Python Source code to an image.
### Converting images to Python source code
So, now that we've converted our Python source code into an image, how do we make use of it?<br>
It's very straight forward, simply call the decoder function as following:
```py
>>> import py2png
>>> py2png.decode.file('bar.png')
print("Hello world from the image side!")
```
#### Executing the image:
```py
>>> import py2png
>>> py2png.decode.exec('bar.png')
Hello world from the image side!
```

### Converting strings to image objects vice versa
Let's say you would want to get a numpy array or a Pillow image returned instead of the file being saved, you can do this easily:
```py
>>> import py2img
>>> py2img.encode.from_file_to_numpy("foo.py")
[[[ 99  72  74]
  [112  98 110]
  [ 81 111  73]
  [107 104 108]
  [ 98  71 120]]

 [[118  73  72]
  [100 118  99]
  [109 120 107]
  [ 73  71  90]
  [121  98  50]]

 [[ 48 103 100]
  [ 71 104 108]
  [ 73  71 108]
  [116  89  87]
  [100 108  73]]

 [[ 72  78 112]
  [ 90  71  85]
  [104  73 105]
  [107  65  65]
  [ 65  61  61]]]
```
File to Pillow image:
```py
>>> import py2img
>>> py2img.encode.from_file_to_PIL("foo.py")
<PIL.Image.Image image mode=RGB size=5x4 at 0x20223FA3700>
```
String to file:
```py
import py2img
py2img.encode.from_str('print("Hello world from the image side!")', output='bar.png')
```
String to numpy array:
```py
>>> import py2img
>>> py2img.encode.from_str_to_numpy('print("Hello world from the image side!")')
[[[ 99  72  74]
  [112  98 110]
  [ 81 111  73]
  [107 104 108]
  [ 98  71 120]]

 [[118  73  72]
  [100 118  99]
  [109 120 107]
  [ 73  71  90]
  [121  98  50]]

 [[ 48 103 100]
  [ 71 104 108]
  [ 73  71 108]
  [116  89  87]
  [100 108  73]]

 [[ 72  78 112]
  [ 90  71  85]
  [104  73 105]
  [107  65  65]
  [ 65  61  61]]]
```
String to Pillow image:
```py
>>> import py2img
>>> py2img.encode.from_str_to_PIL('print("Hello world from the image side!")')
<PIL.Image.Image image mode=RGB size=5x4 at 0x2BDCF463700>
```
## Using other image modes
What if you wanted an image in grayscale or RGBA?<br>
It is quite simple, simply modify the img_mode argument to your choice:
```py
import py2img
py2img.encode.from_file("foo.py", output="bar.png", img_mode='L')
# Note: The 1 colormode is not supported.
```
This gives an image looking like this:<br>
![The image of foo.py in grayscale](https://i.imgur.com/YRFShLu.png)
<br><b>Notice: Image modes with less channels will have a larger aspect ratio, but commonly smaller size.</b>
## Contact
For contact please refer to <b>Itzsten#3103</b> or <b>itzsten@gmail.com</b>.
