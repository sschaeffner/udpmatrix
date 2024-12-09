from datetime import datetime

from PIL import ImageFont, Image, ImageDraw
from PIL.ImageFont import FreeTypeFont

from matrix import Matrix
from pages.page import Page


class ClockPage(Page):
    def __init__(
            self,
            matrix: Matrix,
            font: FreeTypeFont | tuple[FreeTypeFont, FreeTypeFont] | tuple[
                FreeTypeFont, FreeTypeFont, FreeTypeFont],
            x: int | tuple[int, int] | tuple[int, int, int],
            y: int | tuple[int, int] | tuple[int, int, int],
            seconds: bool = False,
            background=(0, 0, 0),
            color=(255, 255, 255)
    ):
        super().__init__(matrix)

        self.font = font if type(font) is tuple else (font, font, font)

        self.x = x if type(x) is tuple else (x,)
        self.y = y if type(y) is tuple else (y,)
        self.seconds = seconds
        self.background = background
        self.color = color

        self.im = Image.new(
            'RGB',
            (self.matrix.width, self.matrix.height),
            self.background
        )

    def update(self):
        self.im = Image.new(
            'RGB',
            (self.matrix.width, self.matrix.height),
            self.background
        )
        draw = ImageDraw.Draw(self.im)

        dt = datetime.now()

        if len(self.x) == 1:
            time_string = (
                f"{dt.hour:02}:{dt.minute:02}:{dt.second:02}"
                if self.seconds
                else f"{dt.hour:02}:{dt.minute:02}"
            )
            draw.text((self.x[0], self.y[0]), time_string, self.color,
                      font=self.font[0])

        if len(self.x) >= 2:
            hour_string = f"{dt.hour:02}"
            minute_string = f"{dt.minute:02}"

            draw.text((self.x[0], self.y[0]), hour_string, self.color,
                      font=self.font[0])

            draw.text((self.x[1], self.y[1]), minute_string, self.color,
                      font=self.font[1])

        if len(self.x) == 3 and self.seconds:
            second_string = f"{dt.second:02}"
            draw.text((self.x[2], self.y[2]), second_string, self.color,
                      font=self.font[2])
