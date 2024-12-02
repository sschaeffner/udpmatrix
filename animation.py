from time import sleep

import numpy as np
from PIL import Image, ImageDraw

from gradient import get_gradient_3d
from matrix import Matrix


def hello_world(mat: Matrix):
    bg_gradient = get_gradient_3d(mat.width, mat.height)

    for t in list(range(96)) + list(range(96, 0, -1)):
        im = Image.new("RGB", (mat.width, mat.height), (0, 0, 0))
        # im.paste(bg_gradient, (0, 0))
        d = ImageDraw.Draw(im)
        d.multiline_text((t - 32, 0), "Hello\nWorld", fill=(255, 255, 255))
        # textImg.show()
        mat.display_image(Image.fromarray(np.uint8(im)))
        sleep(0.01)
