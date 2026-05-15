#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_HEIGHT


class Planet(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Salva a imagem original para rotacionar sem perder qualidade
        # Nota: Ajuste 'self.image' caso a sua classe Entity use outro nome (ex: self.surf)
        self.original_image = self.image
        self.angle = 0  # Ângulo inicial da rotação

    def move(self):
        # ... resto do código anterior do Planeta ...

        # Rotaciona a imagem a partir da original
        # 1. Ângulo sutil
        self.angle += 0.05
        if self.angle >= 360:
            self.angle = 0

        # --- LINHA CORRIGIDA AQUI ---
        # Antes: self.surf = pygame.transform.rotate(self.original_surf, self.angle)
        # Agora: Usamos rotozoom com escala 1.0 (sem zoom) para ativar a suavização
        self.surf = pygame.transform.rotozoom(self.original_surf, self.angle, 1.0)
        # -----------------------------

        # Atualiza o rect com a nova imagem, mantendo o centro no mesmo lugar
        self.rect = self.surf.get_rect(center=(self.center_x_f, self.center_y_f))