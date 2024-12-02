from time import sleep

from PIL import Image, ImageSequence

from matrix import Matrix


def display_gif(mat: Matrix):
    im = Image.open(
        "/Users/sschaeffner/Downloads/8BD1D6A20961281D42ECDBCC752A36E9B3278B46.gif"
        # "/Users/sschaeffner/Downloads/giphy.gif"
    )

    for frame in ImageSequence.Iterator(im):
        mat.display_image(frame)
        sleep(0.05)
