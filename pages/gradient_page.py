from gradient import get_gradient_3d
from matrix import Matrix
from pages.page import Page


class GradientPage(Page):
    def __init__(self, matrix: Matrix):
        super().__init__(matrix)
        self.im = get_gradient_3d(matrix.width, matrix.height)
