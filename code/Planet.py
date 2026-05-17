
import pygame
from code.Entity import Entity


class Planet(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.original_image = self.image
        self.angle = 0  # Ângulo inicial da rotação

    def move(self):
        self.angle += 0.05
        if self.angle >= 360:
            self.angle = 0

        self.surf = pygame.transform.rotozoom(self.original_surf, self.angle, 1.0)

        self.rect = self.surf.get_rect(center=(self.center_x_f, self.center_y_f))