import socket

from PIL import Image
from PIL.Image import Resampling


class Matrix:
    def __init__(self, ip, port, width, height):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.ip = ip
        self.port = port
        self.width = width
        self.height = height

    def display_image(self, im):
        im.thumbnail((self.width, self.height), Resampling.BICUBIC)

        background = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        background.paste(im, (
            int((self.width - im.size[0]) / 2),
            int((self.height - im.size[1]) / 2)
        ))

        offsets_ix = [
            row * self.width + c
            for row in range(16)
            for c in range(16)
        ]

        for block in range(16):
            block_y = int(block / 4)
            block_x = int(block % 4)

            start_ix = ((block_y * 16) * self.width + (block_x * 16))

            im_bytes = background.tobytes()

            bytes_block = bytes(
                im_bytes[((start_ix + offset) * 3) + col]
                for offset in offsets_ix
                for col in range(3)
            )

            self.display_bytes(bytes([block]) + bytes_block)

    def display_bytes(self, bs: bytes):
        self.sock.sendto(bs, (self.ip, self.port))

    def get_center(self):
        return round(self.width / 2), round(self.height / 2)

    def display_color(self, color: (int, int, int)):
        full = Image.new('RGB', (self.width, self.height), color)
        self.display_image(full)
