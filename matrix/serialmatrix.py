from time import sleep

import serial

from PIL import Image
from PIL.Image import Resampling

from matrix import Matrix


class SerialMatrix(Matrix):
    # noinspection PyMissingConstructor
    def __init__(self, port, baud_rate=921600, width=64, height=64):
        self.ser = serial.Serial(port, baud_rate)
        self.width = width
        self.height = height

    def display_image(self, im):
        im.thumbnail((self.width, self.height), Resampling.BICUBIC)

        background = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        background.paste(im, (
            int((self.width - im.size[0]) / 2),
            int((self.height - im.size[1]) / 2)
        ))

        im_bytes = background.tobytes()
        # self.ser.write(im_bytes)
        for row in range(64):
            row_bytes = im_bytes[3 * 64 * row : 3 * 64 * (row + 1)]
            # print(f"row {row}: ({len(row_bytes)}) {row_bytes}")
            self.ser.write(row_bytes)
            # sleep(0.003)

    def display_color(self, color: (int, int, int)):
        full = Image.new('RGB', (self.width, self.height), color)
        self.display_image(full)
