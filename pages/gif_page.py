from PIL import Image, ImageSequence

from matrix import Matrix
from pages.page import Page


class GifPage(Page):
    def __init__(self, matrix: Matrix, gif_path: str):
        super().__init__(matrix)
        self.frame = 0
        self.image = Image.open(gif_path)
        self.size = self.image.size
        self.frames = self.image.n_frames
        print("frames: ", self.frames)

    def update(self):
        self.image.seek(self.frame)
        self.im = Image.new("RGB", self.size)
        self.im.paste(self.image)
        self.frame += 1
        if self.frame >= self.frames:
            self.frame = 0
