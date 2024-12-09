from PIL import Image

from matrix import Matrix
from pages.page import Page


class ColorPage(Page):
    def __init__(self, matrix: Matrix, color: (0, 0, 0)):
        super().__init__(matrix)
        self.im = Image.new("RGB", (matrix.width, matrix.height), color)
