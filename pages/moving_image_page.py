from PIL import Image

from matrix import Matrix
from pages.page import Page


class MovingImagePage(Page):
    def __init__(
            self,
            matrix: Matrix,
            image: Image,
            background=(0, 0, 0),
            max_i: int = 64,
            x_init: int = 0,
            y_init: int = 0,
            x_delta: float = 0,
            y_delta: float = 0,
    ):
        super().__init__(matrix)

        self.image = image.copy()
        self.background = background

        self.i = 0
        self.max_i = max_i
        self.x_init = x_init
        self.y_init = y_init
        self.x_delta = x_delta
        self.y_delta = y_delta

        self.im = Image.new(
            "RGB",
            (self.matrix.width, self.matrix.height),
            self.background
        )

    def update(self):
        self.i += 1
        if self.i >= self.max_i:
            self.i = 0

        self.im = Image.new(
            "RGB",
            (self.matrix.width, self.matrix.height),
            self.background
        )

        x = int(self.x_init + (self.x_delta * self.i))
        y = int(self.y_init + (self.y_delta * self.i))

        self.im = self.image.crop((
            x,
            y,
            x + self.matrix.width,
            y + self.matrix.height
        ))
