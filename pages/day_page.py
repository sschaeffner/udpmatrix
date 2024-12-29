from datetime import datetime, date

from PIL import ImageFont, Image, ImageDraw
from PIL.ImageFont import FreeTypeFont

from matrix import Matrix
from pages.page import Page


class DayPage(Page):
    def __init__(
            self,
            matrix: Matrix,
            day_font: FreeTypeFont | tuple[FreeTypeFont, FreeTypeFont] | tuple[FreeTypeFont, FreeTypeFont, FreeTypeFont],
            number_font: FreeTypeFont | tuple[FreeTypeFont, FreeTypeFont] | tuple[FreeTypeFont, FreeTypeFont, FreeTypeFont],
            background=(0, 0, 0),
            color=(255, 255, 255)
    ):
        super().__init__(matrix)

        self.day_font = day_font
        self.number_font = number_font

        self.background = background
        self.color = color

        self.im = Image.new(
            'RGB',
            (self.matrix.width, self.matrix.height),
            self.background
        )

    def add_text_centered(
            self,
            pos: tuple[float, float],
            text: str,
            color=(255, 255, 255),
            font=None
    ):
        font = font if font else self.font
        pixels = self.draw.textlength(text, font=font)
        (x, y) = pos
        pos = (round(x - pixels / 2 + 0.5), y)
        self.draw.text(pos, text, color, font=font)

    def update(self):
        self.im = Image.new(
            'RGB',
            (self.matrix.width, self.matrix.height),
            self.background
        )
        draw = ImageDraw.Draw(self.im)

        day_zero = datetime(year=2024, month=12, day=26)

        dt = datetime.now()

        day = str((dt - day_zero).days)

        draw.text((2, 3), "DAY", self.color, font=self.day_font)

        x_number = 32
        x_number_width = draw.textlength(day, font=self.number_font)
        pos = (round(x_number - x_number_width / 2 + 0.5), 10)
        draw.text(pos, day, self.color, font=self.number_font)
