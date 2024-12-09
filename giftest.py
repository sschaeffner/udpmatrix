import sys

from PIL import Image, ImageSequence
from PIL.Image import Resampling

im = Image.open(
    "/Users/sschaeffner/Downloads/giphy-5.gif"
)

for frame in ImageSequence.Iterator(im):
    print(f"im size: {im.size}")

    imn = Image.new("RGB", im.size)
    imn.paste(frame)
    print(f"imn size: {imn.size}")

    imn.thumbnail((64, 64), Resampling.BICUBIC)
    print(f"imn size after thumbnail: {imn.size}")

    imm = Image.new("RGB", (64, 64), (0, 0, 0))
    imm.paste(imn, (
        int((64 - imn.size[0]) / 2),
        int((64 - imn.size[1]) / 2)
    ))

    imm.show()
