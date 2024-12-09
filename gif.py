from time import sleep

from PIL import Image, ImageSequence

from matrix import Matrix


def display_gif(mat: Matrix):
    im = Image.open(
        # "/Users/sschaeffner/Downloads/8BD1D6A20961281D42ECDBCC752A36E9B3278B46.gif"
        "/Users/sschaeffner/Downloads/giphy-5.gif"
    )
    while True:
        for frame in ImageSequence.Iterator(im):
            imn = Image.new("RGB", im.size)
            imn.paste(frame)
            mat.display_image(imn)
            sleep(0.1)
