from PIL import Image

from matrix import Matrix


class Page:
    def __init__(self, matrix: Matrix):
        self.matrix = matrix
        self.im = Image.new('RGB', (self.matrix.width, self.matrix.height))

    def get_image(self):
        return self.im.copy()

    def update(self):
        """update animation here"""
        pass

    def display(self):
        self.update()
        self.matrix.display_image(self.im)
