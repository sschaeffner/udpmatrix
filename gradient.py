import numpy as np
from PIL import Image


def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradient_3d(
        width,
        height,
        start_list = (0, 0, 192),
        stop_list = (255, 255, 64),
        is_horizontal_list = (True, False, False)
):
    result = np.zeros((height, width, len(start_list)), dtype=float)

    for i, (start, stop, is_horizontal) in enumerate(
            zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height,
                                          is_horizontal)

    return Image.fromarray(np.uint8(result))
