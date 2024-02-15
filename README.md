# IMG_TO_ASCII

This is a simple script that converts an image to ASCII art. It uses the OpenCV library to read and manipulate the image, and it uses argparse to parse command-line arguments.

## Usage

```bash
python3 ascii.py [-h] [-o OUTPUT] [-s WIDTH HEIGHT] [-c] [image_file_path]

```
Here is a brief description of the command-line arguments:

```
-o, --output: The output file name for the ASCII art. Default is ascii_art.txt.

-s, --size: The size of the output ASCII art (width height). Default is 50 50.

-c, --color: Enable color mode. Default is black and white.

image_file_path: The path to the image file that you want to convert to ASCII art.
```
