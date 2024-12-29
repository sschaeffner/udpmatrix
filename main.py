#!/usr/bin/env python3

from threading import Thread
from time import sleep

from PIL import Image, ImageDraw

from congress import color_green, color_red, color_blue, color_background, \
    color_primary, font_headline, font_numbers
from matrix import Matrix
from matrix.fake_matrix import FakeMatrix
from pages.clock_page import ClockPage
from pages.color_page import ColorPage
from pages.day_page import DayPage
from pages.gif_page import GifPage
from pages.gradient_page import GradientPage
from pages.moving_image_page import MovingImagePage
from pages.text_page import StaticTextPage

UDP_IP = "151.217.193.74"
UDP_PORT = 1234
SIZE = (64, 64)

print("hello, world")

mat = Matrix(UDP_IP, UDP_PORT, SIZE[0], SIZE[1])
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
    page_text_38c3 = StaticTextPage(mat)
    page_text_38c3.add_text_centered(
        (mat.width / 2, 0),
        "38",
        color=color_primary,
        font=font_headline(size=36)
    )
    page_text_38c3.add_text_centered(
        (mat.width / 2, 32),
        "C3",
        color=color_primary,
        font=font_headline(size=36)
    )

    page_text_fabulous = StaticTextPage(mat, background=color_background)
    page_text_fabulous.draw.multiline_text(
        (3, 4),
        "Fab\nulous\nLab\nMunich",
        font=font_headline(12),
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

    # clock_page = ClockPage(
    #     mat,
    #     font=(
    #         font_numbers(38),
    #         font_numbers(38),
    #         font_numbers(16),
    #     ),
    #     x=(1, 1, 44),
    #     y=(-12, 18, 44),
    #     seconds=False,
    #     background=color_background,
    #     color=color_primary
    # )

    clock_page = ClockPage(
        mat,
        font=font_numbers(38),
        x=(10, 10, 0),
        y=(-12, 18, 0),
        background=color_background,
        color=color_primary
    )

    day_page = DayPage(
        mat,
        day_font=font_headline(24),
        number_font=font_numbers(42),
        background=color_background,
        color=color_primary
    )

    while run:
        page_text_38c3.display()
        sleep(5)

        for _ in range(5):
            day_page.display()
            sleep(1)

        # for page in fabulous_lab_munich_pages:
        #     page.display()
        #     sleep(1)

        for _ in range(20):
            clock_page.display()
            sleep(0.5)

        page_text_fabulous.display()
        sleep(5)


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
