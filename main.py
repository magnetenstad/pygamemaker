# -*- coding: utf-8 -*-

import pygame
pygame.init()

#from functions import *
from classes import *

player = Player(100, 100)
for i in range(10):
    Wall(48 + i*16, 132)

while True:
    game.step()
