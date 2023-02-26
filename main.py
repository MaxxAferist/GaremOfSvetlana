import pygame as pg
import sys
from ctypes import *
import os
from math import tan, radians


pg.init()
FPS = 60
WIDTH = windll.user32.GetSystemMetrics(0)
HEIGHT = windll.user32.GetSystemMetrics(1)
KOEF = WIDTH / 1280


def load_image(name): #Загрузка картинки
    filename = os.path.join('data', name)
    if not os.path.isfile(filename):
        print(f'Image is not found: {filename}')
        sys.exit()
    image = transform_image(pg.image.load(filename))
    return image


def transform_image(image): #Трансформация картинки
    rect = image.get_rect()
    w = rect.w
    h = rect.h
    koef = WIDTH / 1280
    image = pg.transform.scale(image, (int(w * koef), int(h * koef)))
    return image


def terminate():
    pg.quit()
    sys.exit()


class Field():
    def __init__(self, x, y, n, m):
        self.field = [[' ' for i in range(n)] for j in range(m)]
        self.field_gecs = [[' ' for i in range(n)] for j in range(m)]
        self.x, self.y = x, y
        self.gecs_image = load_image('background/gecs.png')
        self.gecs_cur_image = load_image('background/gecs big.png')
        self.w, self.h = self.gecs_image.get_rect()[2:4]
        self.gecs_image = pg.transform.scale(self.gecs_image, (self.w, self.h))
        self.gecs_cur_image = pg.transform.scale(self.gecs_cur_image, (self.w, self.h))
        self.w, self.h = self.gecs_image.get_rect()[2:4]
        self.thick = 5 * KOEF


    def adds_gecs(self):
        for i in range(len(self.field)):
            t = 0
            if i % 2 == 1:
                t = self.w // 2
            for j in range(len(self.field[0])):
                self.field_gecs[i][j] = pg.sprite.Sprite()
                self.field_gecs[i][j].image = self.gecs_image.copy()
                self.field_gecs[i][j].rect = self.gecs_image.get_rect()
                self.field_gecs[i][j].rect.x = self.x + j * self.w + t - self.thick * j * 0.75
                self.field_gecs[i][j].rect.y = self.y + i * self.h - (self.h * tan(radians(30)) // 2 + self.thick * 0.55) * i


class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()

        n, m = 11, 9

        self.field = Field(0, 0, n, m)
        self.field.x = (WIDTH - (n + 0.5) * self.field.w + self.field.thick * n) // 2
        self.field.y = (HEIGHT - m * self.field.h + m * (self.field.h * tan(radians(30)) // 2 + self.field.thick * 0.55)) // 2
        self.field.adds_gecs()

        self.field_sprites = pg.sprite.Group()
        for sprites in self.field.field_gecs:
            self.field_sprites.add(sprites)
            self.all_sprites.add(sprites)

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