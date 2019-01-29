# -*- coding: utf-8 -*-

from lib.classes.wall import Wall
from lib.game import game
from player import Player

def main():
    game.init()
    game.camera.follow('player')

    Player(100, 100).add_tag('player')

    for i in range(200):
        Wall(48 + i * 16, 132)

    game.run()

if __name__ == '__main__':
    main()
