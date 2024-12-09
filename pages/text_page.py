from PIL import ImageFont, Image, ImageDraw

from matrix import Matrix
from pages.page import Page


class StaticTextPage(Page):
    def __init__(
            self,
            matrix: Matrix,
            background=(0, 0, 0)
    ):
        super().__init__(matrix)
        self.font = ImageFont.load_default()
        self.background = background
        self.im = Image.new(
            'RGB',
            (self.matrix.width, self.matrix.height),
            self.background
        )
        self.draw = ImageDraw.Draw(self.im)

    def add_text(
            self,
            pos: tuple[float, float],
            text: str,
            color=(255, 255, 255),
            font=None
    ) -> int:
        font = font if font else self.font
        pixels = self.draw.textlength(text, font=font)
        self.draw.text(pos, text, color, font=font)
        return int(round(pixels))

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

    def add_text_right_aligned(
            self,
            pos: tuple[float, float],
            text: str,
            color=(255, 255, 255),
            bg=None
    ):
        pixels = self.draw.textlength(text, font=self.font)
        (x, y) = pos
        pos = (round(x - pixels), y)
        if bg:
            self.draw.rectangle([(x - pixels - 1, y), (x, y + 6)], fill=bg)
        self.draw.text(pos, text, color, font=self.font)
