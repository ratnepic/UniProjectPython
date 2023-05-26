import pygame as pg
from time import time


class NoteSprite(pg.sprite.Sprite):
    def __init__(self, pos, radius, lifetime):
        super().__init__()

        self.serf = pg.Surface((radius*2, radius*2))
        self.serf.fill((255, 255, 255))
        pg.draw.circle(self.serf, (0, 0, 255), (radius, radius), radius)
        self.serf.set_colorkey((255, 255, 255), pg.RLEACCEL)
        self.rect = self.serf.get_rect(
            center=(pos[0], pos[1])
        )

        self.birth_time = time()
        self.lifetime = lifetime

    def update(self):
        if time() - self.birth_time >= self.lifetime:
            self.kill()
