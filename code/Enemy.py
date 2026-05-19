import random
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.rect.center = position
        self.center_y_f = float(self.rect.centery)

        self.mask = pygame.mask.from_surface(self.surf)

    def move(self):
        self.center_y_f += ENTITY_SPEED[self.name]
        self.rect.centery = round(self.center_y_f)