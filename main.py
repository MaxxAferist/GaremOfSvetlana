import pygame as pg
import sys
from ctypes import *


pg.init()
FPS = 60
WIDTH = windll.user32.GetSystemMetrics(0)
HEIGHT = windll.user32.GetSystemMetrics(1)
KOEF = WIDTH / 1920
if WIDTH <= 1920:
    WIDTH = 1920
    HEIGHT = 1080
    KOEF = 1


def terminate():
    pg.quit()
    sys.exit()


class Field():
    def __init__(self, screen, x, y, n, m):
        self.field = [[' ' for i in range(n)] for j in range(m)]
        self.x, self.y = x, y
        self.screen = screen

    def draw(self):
        pass


class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()

        self.running = True

    def run(self):
        while self.running:
            self.screen.fill('darkcyan')

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        terminate()
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()

            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    ex = Game()
    ex.run()