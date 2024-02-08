import cv2 as cv
import numpy
import argparse
import os

chars = [" "," ",".", "-", ":", "*", "+","!", "?","%", "&", "@", "#"]

class ConvertToASCII():
    def __init__(self, img_path, output_path, size=(50,50)):
        self.img_path=img_path
        self.size=size
        self.output_path=output_path

    def pixel_to_char(self, pixel):
        char_index = int(pixel / 255 * (len(chars) - 1))
        return chars[char_index]

    def resizeImage(self, img, size):
        dimensions = (int(size[0]), int(size[1]))
        return cv.resize(img, dimensions)

    def open_image(self):
        img_path = self.img_path
        img = cv.imread(img_path)
        return self.resizeImage(img, self.size)

    def gray_scale(self):
        try:
            img = self.open_image()
            img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            w, h = self.size
            ascii_image = ''
            for x in range(h):
                for y in range(w):
                    pixel = self.pixel_to_char(img[x,y])
                    ascii_image += pixel
                    print(pixel, end="")
                print()
                ascii_image += '\n' 

            with open(self.output_path, "w") as f:
                f.write(ascii_image)

        except FileNotFoundError as e:
            print(f"ERROR: file not found: {e}")
        except cv.error as e:
            print(f"ERROR: OpenCV error: {e}")

    def get_color_code(self, r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    def colored_ASCII(self):
        try:
            img = self.open_image()
            gray_scale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            gray_scale = self.resizeImage(gray_scale, self.size)
            w, h = self.size
            ascii_image = ''
            for x in range(h):
                for y in range(w):
                    r, g, b = img[x, y]
                    color_code = self.get_color_code(r, g, b)
                    pixel = self.pixel_to_char(gray_scale[x,y])
                    rgb_pixel = f"{color_code}{pixel}\033[0m"
                    ascii_image += rgb_pixel
                    print(rgb_pixel, end="")
                print()
                ascii_image += '\n'
            
            with open(self.output_path, "w") as f:
                f.write(ascii_image)

        except FileNotFoundError as e:
            print(f"ERROR: file not found: {e}")
        except cv.error as e:
            print(f"ERROR: OpenCV error: {e}")

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Convert an image to ASCII art")
        parser.usage = "ascii.py [-h] [-o OUTPUT] [-s WIDTH HEIGHT] [-c] [image_file_path]"
        parser.add_argument("-o", "--output", type=str, default="ascii_art.txt", help="Output file name for ASCII art")
        parser.add_argument("-s", "--size", type=int, nargs=2, default=[50, 50], help="Size of the output ASCII art (width height)")
        parser.add_argument("-c", "--color", action="store_true", help="Enable color mode")
        parser.add_argument("image_file_path", nargs="?", default=None, type=str, help="Path to the image file")
        args = parser.parse_args()

        if not args.image_file_path:
            raise ValueError("File not specified!")

        img_converter = ConvertToASCII(args.image_file_path, args.output, args.size)

        if args.color == True:
            img_converter.colored_ASCII()
        else:
            img_converter.gray_scale()

    except Exception as e:
        print(f"ERROR: {e}")
