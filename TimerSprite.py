import pygame as pg
from time import time


class TimerSprite(pg.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.serf = pg.Surface(size)
        self.rect = self.serf.get_rect()
        self.p_time = time()
        self.m_timer = 10
        self.timer = self.m_timer

    def update(self):
        self.timer -= time() - self.p_time
        self.p_time = time()
        self.serf.fill((255, 255, 255))
        rel = self.timer / self.m_timer
        pg.draw.rect(self.serf, (0, 0, 0),
                     pg.Rect(0, 0, self.serf.get_width() * rel, self.serf.get_height()))

    def add_time(self, amount):
        self.timer += amount
        if self.timer > self.m_timer:
            self.timer = self.m_timer
