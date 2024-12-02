#!/usr/bin/env python3
from time import sleep

from animation import hello_world
from gif import display_gif
from gradient import get_gradient_3d
from matrix import Matrix

UDP_IP = "10.100.205.85"
UDP_PORT = 1234
SIZE = (64, 64)

print("hello, world")

mat = Matrix(UDP_IP, UDP_PORT, SIZE[0], SIZE[1])

mat.display_color((255, 0, 0))
sleep(0.3)
mat.display_color((0, 255, 0))
sleep(0.3)
mat.display_color((0, 0, 255))
sleep(0.3)

gradient = get_gradient_3d(*SIZE)
mat.display_image(gradient)

sleep(0.6)

hello_world(mat)

display_gif(mat)

