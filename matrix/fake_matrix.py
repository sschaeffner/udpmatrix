from time import sleep

import pygame
from PIL import Image
from PIL.Image import Resampling

from matrix import Matrix


class FakeMatrix(Matrix):
    # noinspection PyMissingConstructor
    def __init__(self):
        self.width = 64
        self.height = 64

        self.upscale_factor = 4

        pygame.init()
        self.window = pygame.display.set_mode((
            self.width * self.upscale_factor,
            self.height * self.upscale_factor
        ))
        self.clock = pygame.time.Clock()
        self.run = True
        self.pygame_surface = None

    def display_image(self, im):
        im.thumbnail((self.width, self.height), Resampling.BICUBIC)
        im = im.resize((
            self.width * self.upscale_factor,
            self.height * self.upscale_factor
        ), resample=Resampling.BOX)

        self.pygame_surface = self._pil_image_to_surface(im)

    def pygame_loop(self):
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        while not self.pygame_surface:
            sleep(0.01)

        self.window.fill(0)
        self.window.blit(
            self.pygame_surface,
            self.pygame_surface.get_rect(center=(
                int(((self.width * self.upscale_factor) / 2)),
                int(((self.height * self.upscale_factor) / 2))
            ))
        )

        pygame.display.flip()

    @staticmethod
    def _pil_image_to_surface(pil_image: Image):
        return pygame.image.fromstring(
            pil_image.tobytes(),
            pil_image.size,
            pil_image.mode
        ).convert()
