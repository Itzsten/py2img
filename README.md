# py2img
The official GitHub repository for the Python source code to image converter.
## Why use py2img?
py2img features stabile image en- or decoding and aims at converting Python source into pure images while also being able to safely execute them without writing any temporary files or other unneeded cache.
## How does it work?
### decoder
The decoder reads the image colors and converts them to bytes and base64 decodes them which achieves a stronger source code protection rather than storing the source code openly, and optionally executes the code stored in it.
### encoder
The encoder is a bit more complicated compared to the decoder, it first of all calculates necessary height and width for a square, optionally removing the last row if empty to achieve a comfortably read image. It then converts the data inputted to bytes and base64 encodes to not store source openly as described before, to then copy the char codes to the image. Due to the base64 encoding UTF8 characters may be safely stored without losing data. Notice that UTF16 characters are not recommended. After copying data it optionally saves the image or returns a PIL/numpy object based on the function called.
