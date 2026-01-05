#!/usr/bin/env python3

from threading import Thread
from time import sleep

from PIL import Image, ImageDraw, ImageFont

from congress import color_green, color_red, color_blue, color_background, \
    color_primary, font_headline, font_numbers
from matrix import Matrix, SerialMatrix
from matrix.fake_matrix import FakeMatrix
from pages.clock_page import ClockPage
from pages.color_page import ColorPage
from pages.gif_page import GifPage
from pages.gradient_page import GradientPage
from pages.moving_image_page import MovingImagePage
from pages.text_page import StaticTextPage

UDP_IP = "10.100.205.85"
UDP_PORT = 1234
SIZE = (64, 64)

SERIAL_PORT = "/dev/cu.usbserial-0001"

print("hello, world")

# mat = Matrix(UDP_IP, UDP_PORT, SIZE[0], SIZE[1])
mat = SerialMatrix(SERIAL_PORT, 921600, SIZE[0], SIZE[1])
sleep(1)
# mat = FakeMatrix()
run = True


def fabulous_scroller() -> MovingImagePage:
    text = "Fabulous Lab Munich"
    font = font_headline(size=60)

    image = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(image)
    text_width = int(draw.textlength(text, font=font))

    image = Image.new("RGB", (text_width, 64), color_background)
    draw = ImageDraw.Draw(image)
    draw.text((0, 5), text, font=font, fill=color_primary)

    return MovingImagePage(
        mat,
        image,
        max_i=int((text_width + 64) / 4),
        x_init=-64,
        x_delta=4
    )


def content():
    page_gradient = GradientPage(mat)

    page_color_r = ColorPage(mat, color_red)
    page_color_g = ColorPage(mat, color_green)
    page_color_b = ColorPage(mat, color_blue)

    page_text_1 = StaticTextPage(mat)
    page_text_1.add_text((0, 0), "hello, world")

    page_text_2 = StaticTextPage(mat)
    page_text_2.add_text((0, 0), "another hello")

    page_text_3 = StaticTextPage(mat, background=color_background)
    page_text_3.draw.multiline_text(
        (3, 4),
        "Fab\nulous\nLab\nMunich",
        font=font_headline(12),
        fill=color_primary
    )

    page_text_4 = StaticTextPage(mat, background=color_background)
    page_text_4.draw.multiline_text(
        (2, 5),
        "Fab\nulous\nLab",
        font=font_headline(16),
        fill=color_primary
    )

    fabulous_lab_munich_pages = []

    for char in "Fabulous Lab Munich":
        p = StaticTextPage(mat, background=color_background)
        p.add_text_centered(
            (mat.width / 2, 5),
            char,
            color=color_primary,
            font=font_headline(size=60)
        )
        fabulous_lab_munich_pages.append(p)

    fab_scroller = fabulous_scroller()

    gif_page1 = GifPage(mat, "/Users/sschaeffner/Downloads/giphy.gif")
    gif_page2 = GifPage(mat, "/Users/sschaeffner/Downloads/giphy-2.gif")
    gif_page3 = GifPage(mat, "/Users/sschaeffner/Downloads/giphy-3.gif")
    gif_page4 = GifPage(mat, "/Users/sschaeffner/Downloads/giphy-4.gif")
    gif_page5 = GifPage(mat, "/Users/sschaeffner/Downloads/giphy-5.gif")
    gif_page6 = GifPage(mat, "/Users/sschaeffner/Downloads/giphy-6.gif")

    clock_page = ClockPage(
        mat,
        font=(
            font_numbers(38),
            font_numbers(38),
            font_numbers(16),
        ),
        x=(1, 1, 44),
        y=(-12, 18, 44),
        seconds=True,
        background=color_background,
        color=color_primary
    )

    while run:
        page_color_r.display()
        sleep(0.2)
        page_color_g.display()
        sleep(0.2)
        page_color_b.display()
        sleep(0.2)

        page_gradient.display()
        sleep(0.5)
        page_text_1.display()
        sleep(0.5)
        page_text_2.display()
        sleep(0.5)

        page_text_3.display()
        sleep(0.5)

        page_text_4.display()
        sleep(0.5)

        for page in fabulous_lab_munich_pages:
            page.display()
            sleep(0.2)

        for _ in range(fab_scroller.max_i):
            fab_scroller.display()
            sleep(0.1)

        for page in [gif_page1, gif_page2, gif_page3, gif_page4, gif_page5,
                     gif_page6]:
            for _ in range(page.frames):
                page.display()
                sleep(0.1)

        for _ in range(10):
            clock_page.display()
            sleep(0.2)


def content_clock():
    clock_page_1 = ClockPage(
        mat,
        font=font_numbers(20),
        x=2,
        y=14,
        background=color_background,
        color=color_primary
    )

    clock_page_2 = ClockPage(
        mat,
        font=font_numbers(13),
        x=1,
        y=18,
        seconds=True,
        background=color_background,
        color=color_primary
    )

    clock_page_3 = ClockPage(
        mat,
        font=font_numbers(32),
        x=(12, 12),
        y=(-8, 22),
        seconds=True,
        background=color_background,
        color=color_primary
    )

    clock_page_4 = ClockPage(
        mat,
        font=font_numbers(26),
        x=(16, 16, 16),
        y=(-9, 11, 31),
        seconds=True,
        background=color_background,
        color=color_primary
    )

    clock_page_5 = ClockPage(
        mat,
        font=(
            font_numbers(38),
            font_numbers(38),
            font_numbers(16),
        ),
        x=(1, 1, 44),
        y=(-12, 18, 44),
        seconds=True,
        background=color_background,
        color=color_primary
    )

    while run:
        # for _ in range(10):
        #     clock_page_1.display()
        #     sleep(0.2)
        #
        # for _ in range(10):
        #     clock_page_2.display()
        #     sleep(0.2)

        # for _ in range(10):
        #     clock_page_3.display()
        #     sleep(0.2)

        # for _ in range(10):
        #     clock_page_5.display()
        #     sleep(0.2)

        for _ in range(10):
            clock_page_5.display()
            sleep(0.2)


if __name__ == "__main__":
    thread = Thread(target=content)
    thread.start()

    while run:
        if mat is FakeMatrix:
            mat.pygame_loop()
            run = mat.run
    run = False

# display_gif(mat)
