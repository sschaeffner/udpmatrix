#!/usr/bin/env python3

import socket
from time import sleep

import numpy as np
from PIL import Image
from PIL.Image import Resampling

UDP_IP = "10.100.205.85"
UDP_PORT = 1234
SIZE = (16, 16)


def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=float)

    for i, (start, stop, is_horizontal) in enumerate(
            zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height,
                                          is_horizontal)

    return result


# on macOS: sudo sysctl -w net.inet.udp.maxdgram=65535
# net.inet.udp.maxdgram: 9216 -> 65535

class Matrix:
    def __init__(self, width, height):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.width = width
        self.height = height

    def display_image(self, im):
        # im = Image.open("./album.jpg")
        # im = im.transpose(Transpose.FLIP_LEFT_RIGHT)
        # im = im.transpose(Image.FLIP_TOP_BOTTOM)
        im.thumbnail((self.width, self.height), Resampling.BICUBIC)

        background = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        background.paste(im, (
            int((self.width - im.size[0]) / 2),
            int((self.height - im.size[1]) / 2)
        ))

        for i in range(16):
            self.sock.sendto(bytes([i]) + background.tobytes(), (UDP_IP, UDP_PORT))

    def display_bytes(self, byte_arr: bytearray):
        self.sock.sendto(byte_arr, (UDP_IP, UDP_PORT))

    def get_center(self):
        return round(self.width / 2), round(self.height / 2)


print("hello, world")

matrix = Matrix(SIZE[0], SIZE[1])

array = get_gradient_3d(
    matrix.width,
    matrix.height,
    (0, 0, 192),
    (255, 255, 64),
    (True, False, False)
)

fullR = Image.new('RGB', (matrix.width, matrix.height), (255, 0, 0))
fullG = Image.new('RGB', (matrix.width, matrix.height), (0, 255, 0))
fullB = Image.new('RGB', (matrix.width, matrix.height), (0, 0, 255))

matrix.display_image(Image.fromarray(np.uint8(fullR)))
sleep(1)
matrix.display_image(Image.fromarray(np.uint8(fullG)))
sleep(1)
matrix.display_image(Image.fromarray(np.uint8(fullB)))
sleep(1)
matrix.display_image(Image.fromarray(np.uint8(array)))
