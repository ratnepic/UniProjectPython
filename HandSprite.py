import pygame as pg


class HandSprite(pg.sprite.Sprite):
    def __init__(self, coordinates, radius):
        super().__init__()
        self.serf = pg.Surface((radius*2, radius*2))
        self.serf.fill((255, 255, 255))
        pg.draw.circle(self.serf, (0, 0, 0), (radius, radius), radius)
        self.serf.set_colorkey((255, 255, 255), pg.RLEACCEL)
        self.rect = self.serf.get_rect(center=coordinates)

    def update(self):
        self.kill()
